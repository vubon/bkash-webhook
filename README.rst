===========================
bKash Webhook
===========================

bKash Web hook will help to get instance notification from bKash merchant account.

Quick start
-----------

1. Install bkash_webhook from PyPy::

    pip install bkash_webhook

2. Include the polls URLconf in your project urls.py like this::

    from bkash_webhook import BKash
    bkash_payload = {}
    bkash = Bkash(bkash_payload)

