import base64


def decode_base64(data: str) -> str:
    """
    :Description: Decode the base64 data
    :param data: encode data of base64
    :return: decoded data
    :rtype: str
    """
    return base64.b64decode(bytes(data, "utf-8"))