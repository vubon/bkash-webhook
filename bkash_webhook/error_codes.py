__all__ = ['ERROR_CODE']


class GlobalErrorCodes(object):
    """
    A set of constants representing validation errors.  Validation error messages can change, but the codes will not.
    See the source for a list of all errors codes.
    Codes can be used to check for specific validation errors
    """
    KEY_ERROR = dict(error_code="KE400", message="Key error")
    ALL_FIELDS_REQUIRED = dict(error_code="AFR400", message='All fields are required')
    VALUE_ERROR = dict(error_code="VE400", message="Value error")
    INVALID_REQUEST = dict(error_code="IR400", message="Invalid request")


class ErrorCodes(object):

    def __init__(self):
        self.global_error = GlobalErrorCodes()


# Instance
ERROR_CODE = ErrorCodes()
