import unittest

from bkash_webhook.commons import is_protected_type, force_bytes


class TestCommon(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_is_protected_type(self):
        self.assertEqual(is_protected_type(2.0), True)

    def test_force_bytes(self):
        self.assertEqual(force_bytes(b"hello"), b"hello")
        self.assertEqual(force_bytes(s=b'hello', encoding='ascii'), b"hello")
        self.assertEqual(force_bytes(s=2.0, strings_only=True), 2.0)
        self.assertEqual(force_bytes(s=memoryview(b'Hello')), b'Hello')
