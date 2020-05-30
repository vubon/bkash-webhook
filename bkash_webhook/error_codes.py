__all__ = ['ERROR_CODE']


class GlobalErrorCodes(object):
    """
    A set of constants representing validation errors.  Validation error messages can change, but the codes will not.
    See the source for a list of all errors codes.
    Codes can be used to check for specific validation errors
    """
    KEY_ERROR = dict(error_code="KE400", message="Key error")
    VALUE_ERROR = dict(error_code="VE400", message="Value error")


class ErrorCodes(object):

    def __init__(self):
        self.global_codes = GlobalErrorCodes()


# Instance
ERROR_CODE = ErrorCodes()
