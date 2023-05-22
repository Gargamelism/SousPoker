from rest_framework.exceptions import APIException


class ProfileDoesNotExist(APIException):
    status_code = 400
    default_detail = "The requested profile does not exist."
    default_code = "profile_does_not_exist"