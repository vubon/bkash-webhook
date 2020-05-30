class CustomException(Exception):
    default_status_code = 500
    default_message = {"message": "Unknown error", "error_code": "UE500"}

    def __init__(self, message: dict, status_code: int = None):
        self.status_code = status_code if status_code else self.default_status_code
        self.message = message if message else self.default_message


class ValidationError(CustomException):
    default_status_code = 400
    default_message = {"message": "Unknown validation error", "error_code": "UVE400"}