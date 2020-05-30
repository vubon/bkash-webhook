import os
import json
import unittest

from bkash_webhook import *

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def file_reader(path: str) -> dict:
    with open(path) as reader:
        return json.loads(reader.read())


class BkashTest(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_notification = file_reader(BASE_DIR + '/dummy_notification.json')

    def test_invalid_signing_cert_url(self):
        self.valid_notification['SigningCertURL'] = "https://vubon.me"
        bkash = BKash(self.valid_notification)
        self.assertRaises(ValidationError, lambda: bkash.bkash_response_process())

    def test_invalid_type(self):
        self.valid_notification['Type'] = "Unknown"
        bkash = BKash(self.valid_notification)
        self.assertRaises(ValidationError, lambda: bkash.bkash_response_process())

    def test_invalid_signature_version(self):
        self.valid_notification["SignatureVersion"] = "2"
        bkash = BKash(self.valid_notification)
        self.assertRaises(ValidationError, lambda: bkash.bkash_response_process())

    def test_invalid_pem_extension(self):
        self.valid_notification['SigningCertURL'] = "https://sns.ap-southeast-1.amazonaws.com/sdfsdfsdfsdf.txt"
        bkash = BKash(self.valid_notification)
        self.assertRaises(ValidationError, lambda: bkash.bkash_response_process())

    def test_missing_dot(self):
        self.valid_notification['SigningCertURL'] = "https://sns.ap-southeast-1.amazonaws.com/sdfsdfsdfsdftxt"
        bkash = BKash(self.valid_notification)
        self.assertRaises(ValidationError, lambda: bkash.bkash_response_process())
