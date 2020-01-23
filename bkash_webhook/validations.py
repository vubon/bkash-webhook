"""
Descriptions: All kinds of validation will be write here for bKash web hook
usages:
    when valid url:
    In [4]: from applibs.bKash.validations import *
    In [5]: url = "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
    In [6]: url_validation(url)
    return nothing
    when invalid url:
    In [8]: invalid_url = "http://vubon.me/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem2"
    In [9]: url_validation(invalid_url)
    you will get validation error
"""
import logging
import re
from urllib.parse import urlparse

from bkash_webhook import exceptions
from bkash_webhook.error_codes import ERROR_CODE

logger = logging.getLogger("bkash_validation")

__all__ = [
    "url_validation", "type_validation",
    "signature_version_validation",
]

HOST_REGEX = re.compile(r'^sns\.[a-zA-Z0-9\-]{3,}\.amazonaws\.com(\.cn)?$')


def host_validation(url: str):
    """
    :param url:
    :return:
    """
    parse = urlparse(url=url)
    if not (HOST_REGEX.match(parse.netloc) and parse.scheme == "https"):
        logger.info(f"bkash invalid host error {url}")
        raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)
    return parse


def url_validation(argument):
    """
    :return: None
    :rtype: NoneType object
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            parse = host_validation(url=args[0].body.get(argument))
            if "SigningCertURL" == argument:
                path, pem = parse.path.split(".")
                if pem != "pem":
                    logger.info(f"bkash cert url error {path} or pem {pem}")
                    raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def signature_version_validation(argument):
    """
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            current_version = args[0].body.get(argument)
            if current_version != "1":
                logger.info(f"bkash signature version error {current_version}")
                raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def type_validation(argument):
    """
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            types = ["Notification", "SubscriptionConfirmation"]
            if not args[0].body.get(argument) in types:
                logger.info(f"bkash notification type error {args[0].body.get('Type')}")
                raise exceptions.ValidationError(ERROR_CODE.global_codes.VALUE_ERROR)
            return func(*args, **kwargs)

        return wrapper

    return decorator
