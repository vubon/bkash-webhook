# User Guide
## Getting started
### Installation
Install from PyPI:
```shell script
pip install bKashWebhook
```

## Example
### Django with Django Rest framework

```python
"""
Below endpoint as a basic example for Django and using Rest Framework. 
"""

import json

from rest_framework.views import APIView
from rest_framework.response import Response

from bkash_webhook import BKash, ValidationError


class Example(APIView):
    def post(self, request):
        try:
            bkash = BKash(json.loads(request.body))
            response = bkash.bkash_response_process()
            if response is not None:
                # save your payload
                # Remember one thing, their notification payload comes as nested. 
                # So you need to convert the message data as dictionary by using json module. 
               # example: 
               #     json.loads(response.get("Message"))
                pass 
            return Response(status=200) 
        except ValidationError as err:
            return Response(data=err.message, status=err.status_code)
```
Same process for other python web frameworks.

[Bkash Webhook Docs](https://developer.bka.sh/docs/webhooks)