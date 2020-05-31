import os
import json
import unittest

from bkash_webhook import *

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def file_reader(path: str) -> dict:
    with open(path) as reader:
        return json.loads(reader.read())


class BKashWebhookListenerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_notification = file_reader(BASE_DIR + '/dummy_notification.json')
        self.subscribe = file_reader(BASE_DIR + '/dummy_subscribe.json')

    def test_valid_notification(self):
        bkash = BkashWebhookListener(self.valid_notification)
        res = bkash.bkash_response_process()
        self.assertEqual(res, self.valid_notification)

    def test_dummy_subscribe(self):
        bkash = BkashWebhookListener(self.subscribe)
        bkash.bkash_response_process()

    def test_notification_http_connection_error(self):
        self.valid_notification[
            'SigningCertURL'] = "https://localhost:8000/SimpleNotificationService-9b8b327a734e4b5db66e525c2ac6ac6f.pem"
        notify = BkashWebhookListener(self.valid_notification)
        self.assertRaises(ValidationError, lambda: notify.bkash_response_process())

    def test_notification_bad_request(self):
        self.valid_notification['SigningCertURL'] = "http://localhost:8000/SimpleNotificationService.pem"
        notify = BkashWebhookListener(self.valid_notification)
        self.assertRaises(ValidationError, lambda: notify.bkash_response_process())
