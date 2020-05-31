# bKash Webhook (Merchant Account)
[![PyPI version](https://badge.fury.io/py/bKashWebhook.svg)](https://badge.fury.io/py/bKashWebhook)
![Coverage](https://raw.githubusercontent.com/vubon/bkash-webhook/master/docs/coverage.svg)
[![GitHub version](https://badge.fury.io/gh/vubon%2Fbkash-webhook.svg)](https://badge.fury.io/gh/vubon%2Fbkash-webhook)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

## Introduction 
This package will help to receive Webhook notification from bKash end and the user can use this package of any kind of Python Web Frameworks.<br/>

**Note: Using area - Only Bangladesh** 

**If bKash complains about this package.Such as Logo and others. The author will remove from the package from PyPi and Github.**

![Coverage](https://raw.githubusercontent.com/vubon/bkash-webhook/master/docs/BKash.svg)
## Quickstart
### Installation
Install from pypi: 
```shell script
pip install bKashWebhook
```

## Security
bKashWebhook package does not provide any kind of security. But payload content security handle by **bKash** <br/>
N.B. You need to secure your API endpoint yourself. 
## Example 
```python
import json
from bkash_webhook import BKash
bkash = BKash(json.loads("bKash Webhook Payload"))
res = bkash.bkash_response_process()
print(res)
# You will get bKash Payload if everything is okay. 
```
To learn more [Documentation](./docs/GUIDE.md).

## Changelog
See [Changelog](CHANGELOG.md)

## Trade off
- Currently, Coverage result is 98%. Two test cases don't cover and those test cases are not possible to cover.
These test cases do not impact to core response. So don't worry. ValidationError Exception would manage that type error. 

## License
MIT