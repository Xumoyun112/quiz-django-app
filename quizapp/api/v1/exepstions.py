from rest_framework.exceptions import APIException


class OldPasseordExepstions(APIException):
    status_code = 400
    default_detail = 'Bad Request'