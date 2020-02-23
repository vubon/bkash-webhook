class CustomException(Exception):
    status_code = 500
    default_detail = {"message": "Unknown error", "error_code": "UE500"}

    def __init__(self, message: dict, status_code: int = None):
        self.status_code = status_code if status_code else self.status_code
        self.message = message if message else self.default_detail


class ValidationError(CustomException):
    status_code = 400
    default_detail = {"message": "Unknown validation error", "error_code": "UVE400"}


class DataNotFound(CustomException):
    status_code = 404
    default_detail = {"message": "Data not found", "error_code": "DNF404"}


class ServiceUnavailable(CustomException):
    status_code = 503
    default_detail = {"message": "Service Unavailable", "error_code": "SU503"}
