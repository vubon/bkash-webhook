import base64
import datetime
from decimal import Decimal

_PROTECTED_TYPES = (
    type(None), int, float, Decimal, datetime.datetime, datetime.date, datetime.time,
)


def decode_base64(data: str) -> str:
    """
    :Description: Decode the base64 data
    :param data: encode data of base64
    :return: decoded data
    :rtype: str
    """
    return base64.b64decode(bytes(data, "utf-8"))


def is_protected_type(obj):
    """Determine if the object instance is of a protected type.

    Objects of protected types are preserved as-is when passed to
    force_str(strings_only=True).
    """
    return isinstance(obj, _PROTECTED_TYPES)


def force_bytes(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Similar to smart_bytes, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    # Handle the common case first for performance reasons.
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if strings_only and is_protected_type(s):
        return s
    if isinstance(s, memoryview):
        return bytes(s)
    return str(s).encode(encoding, errors)
