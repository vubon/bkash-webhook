INSTALLED_APPS = (
    'bkash_webhook',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
SECRET_KEY = "akdi1%$*&#@!asdrfskfsdbcl)(&^%sdjcbajk1#@!sdfkdsfplqisddhdhalxmndg"

BkASH_WEBHOOK_KEYS = [
    'Message',
    'MessageId',
    'Subject',
    'SubscribeURL',
    'Timestamp',
    'Token',
    'TopicArn',
    'Type'
]