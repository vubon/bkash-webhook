from rest_framework.exceptions import APIException


class CustomAPIException(APIException):
    status_code = 500
    default_message = {"message": "Unknown error", "error_code": "UE500"}

    def __init__(self, message=None):
        super().__init__(detail=message if message else self.default_message)


class ValidationError(CustomAPIException):
    status_code = 400
    default_message = {"message": "Unknown validation error", "error_code": "UVE400"}


class DataNotFound(CustomAPIException):
    status_code = 404
    default_message = {"message": "Data not found", "error_code": "DNF404"}


class PermissionDenied(CustomAPIException):
    status_code = 403
    default_message = {"message": "You have no permission to perform this action", "error_code": "PD403"}


class ServiceUnavailable(CustomAPIException):
    status_code = 503
    default_message = {"message": "Service Unavailable", "error_code": "SU503"}
