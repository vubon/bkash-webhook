# bKash Webhook
![Coverage](./docs/coverage.svg)

## Introduction
This package will help to receive Webhook notification from bKash end and the user can use this package of any kind of Python Web Frameworks 

**If bKash complains about this package.Such as Logo and others. The author will remove from the package from PyPi and Github.**

![Coverage](./docs/BKash.svg)
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
#### Timestamp or datetime object
```python
import json
from bkash_webhook import BKash
bkash = BKash(json.loads("Bkash Payload"))
res = bkash.bkash_response_process()
print(res)
# You will get bKash Payload if everything is okay. 
```
To learn more [Documentation](./docs/GUIDE.md).

## Changelog
See [Changelog](CHANGELOG.md)

## License
MIT