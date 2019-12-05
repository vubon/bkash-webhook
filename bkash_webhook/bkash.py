"""
In this module will help to get bKash transactions data via bKash web hook.
Functionality:
Methods:
    - get_cert
    - signature validation
    -
"""
import requests

from OpenSSL.crypto import verify, load_certificate, FILETYPE_PEM
from django.utils.encoding import force_bytes

from bkash_webhook import exceptions
from bkash_webhook.validations import *
from applibs.error_codes import ERROR_CODE
from bkash_webhook.commons import decode_base64
from applibs.loggers import log_exception, log_info


class BKash:

    def __init__(self, body: dict, header: str = None):
        self.body = body
        self.__header = header

    @url_validation("SigningCertURL")
    def __get_cert(self) -> object:
        """
        :return: cert data
        :rtype: str
        """
        cert_url = self.body.get('SigningCertURL')
        # getting cert data
        try:
            response = requests.get(cert_url)
            if 400 <= response.status_code <= 499:
                log_info().info(f"bKash throw bad request response {response.text}")
                raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)
            return response.text
        except Exception as err:
            log_exception().error(f"bKash cert url error {err}")
            raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)

    def __content(self) -> str:
        """
        :return:
        """

        sign_able_keys = [
            'Message',
            'MessageId',
            'Subject',
            'SubscribeURL',
            'Timestamp',
            'Token',
            'TopicArn',
            'Type'
        ]
        string_data = ""
        for key in sign_able_keys:
            if key in self.body.keys():
                string_data += f"{key}\n{self.body[key]}\n"
        return force_bytes(string_data)

    def __openssl_verification(self):
        """
        :return:
        """
        signature = decode_base64(self.body.get("Signature"))
        cert = load_certificate(FILETYPE_PEM, force_bytes(self.__get_cert()))
        verify(cert=cert, signature=signature, data=self.__content(), digest="SHA1")

    @url_validation("SubscribeURL")
    def __subscribe_notification(self):
        """
        :return:
        """
        # subscribe notification
        try:
            response = requests.get(self.body.get("SubscribeURL"))
            if 400 <= response.status_code <= 499:
                log_info().info(f"bKash throw bad request response {response.text}")
                raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)
            log_info().info(f"Subscribe response {response.text}")
        except requests.HTTPError as err:
            log_exception().error(f"bKash cert url error {err}")
            raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)

    @type_validation("Type")
    def bkash_response_process(self):
        """
        :return:
        """
        # call here data verification
        try:
            self.__openssl_verification()
        except Exception as err:
            log_exception().error(f"OpenSSL error {err}")
            raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)

        if self.body.get("Type") == "SubscriptionConfirmation":
            self.__subscribe_notification()
        elif self.body.get("Type") == "Notification":
            return self.body
        else:
            log_info().info("bKash does not send correct notification type")
