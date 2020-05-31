"""
In this module will help to get bKash transactions data via bKash web hook.
Functionality:
Methods:
    - get_cert: Get certificate from bKash provide url
    - content: Create sign able content and make bytes
    - openssl_verification: Verify the content by certificate
    - subscribe_notification: Subscribe topic for getting payment notification from bKash end
    - bkash_response_process: Outer call receiver of this module
"""
import logging
import warnings

import requests
from OpenSSL.crypto import verify, load_certificate, FILETYPE_PEM

from bkash_webhook import exceptions
from bkash_webhook.validations import *
from bkash_webhook.error_codes import ERROR_CODE
from bkash_webhook.commons import decode_base64, force_bytes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bkash")


class BkashWebhookListener:

    def __init__(self, body: dict, header: str = None):
        self.body = body
        self.__header = header

    @url_validation("SigningCertURL")
    def __get_cert(self):
        """
        :return: cert data
        :rtype: str
        """
        cert_url = self.body.get('SigningCertURL')
        # getting cert data
        try:
            response = requests.get(cert_url)
            if 400 <= response.status_code <= 499:
                logger.info(f"bKash throw bad request response for SigningCertURL{response.text}")
                raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR, response.status_code)
            return response.text
        except (requests.ConnectionError, requests.Timeout) as err:
            logger.info(f"bKash SigningCertURL error {err}")
            raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)

    def __content(self) -> bytes:
        """
        :return:
        """

        default_sign_able_keys = [
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
        for key in default_sign_able_keys:
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
                logger.info(f"bKash throw bad request response for SubscribeURL {response.text}")
                raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR, response.status_code)
            logger.info(f"Subscribe response {response.text}")
        except (requests.ConnectionError, requests.Timeout) as err:
            logger.error(f"bKash subscribe url error {err}")
            raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)

    @type_validation("Type")
    @signature_version_validation("SignatureVersion")
    def bkash_response_process(self):
        """
        :return:
        """
        # call here data verification
        try:
            self.__openssl_verification()
        except Exception as err:
            logger.error(f"OpenSSL error {err}")
            raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)

        if self.body.get("Type") == "SubscriptionConfirmation":
            self.__subscribe_notification()
        elif self.body.get("Type") == "Notification":
            return self.body


class BKash(BkashWebhookListener):

    def __init__(self, body: dict, header: str = None):
        warnings.warn("Call to deprecated class Bkash. Use BkashWebhookListener. "
                      "Bkash class will completely remove from v1.0.0",
                      DeprecationWarning, stacklevel=2)
        BkashWebhookListener.__init__(self, body, header)
