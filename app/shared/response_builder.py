from builtins import object
from rest_framework import status
from rest_framework.response import Response


class ResponseBuilder(object):
    """
    API response builder
    """

    def __init__(self):
        self.results = {}
        self.errors = {}
        self.page = {}
        self.status_code = 1
        self.status_message = ""
        self.status = status.HTTP_200_OK

    def fail(self):
        self.status_code = -1
        return self

    def message(self, status_message):
        self.status_message = status_message
        return self

    def success(self):
        self.status_code = 1
        return self

    def set_status_code(self, status_code):
        self.status_code = status_code
        return self

    def ok_200(self):
        self.status = status.HTTP_200_OK
        return self

    def created_201(self):
        self.status = status.HTTP_201_CREATED
        return self

    def accepted_202(self):
        self.status = status.HTTP_202_ACCEPTED
        return self

    def no_content_204(self):
        self.status = status.HTTP_204_NO_CONTENT
        return self

    def not_found_404(self):
        self.status = status.HTTP_404_NOT_FOUND
        return self

    def bad_request_400(self):
        self.status = status.HTTP_400_BAD_REQUEST
        return self

    def user_unauthorized_401(self):
        self.status = status.HTTP_401_UNAUTHORIZED
        return self

    def user_forbidden_403(self):
        self.status = status.HTTP_403_FORBIDDEN
        return self

    def page_object(self, page):
        self.page = page
        return self

    def result_object(self, result):
        self.results = result
        return self

    def error_object(self, errors):
        self.errors = errors
        return self

    def get_response(self):
        content = self.get_json()
        return Response(content, status=self.status)

    def get_json(self):
        status_message = self.status_message

        return {
            'status_code': self.status_code,
            'status_message': status_message,
            'data': self.results,
            'page': self.page,
            'error': self.errors,
        }

    def get_400_bad_request_response(self, message, errors={}):
        return self.bad_request_400().fail().message(message).error_object(errors).get_response()

    def get_404_not_found_response(self, message,errors={}):
        return self.not_found_404().fail().message(message).error_object(errors).get_response()

    def get_201_success_response(self, message, result={}):
        return self.success().created_201().message(message).result_object(result).get_response()

    def get_200_success_response(self, message, result={}, page_info={}):
        return self.success().ok_200().message(message).result_object(result).page_object(page_info).get_response()

    def get_204_success_response(self):
        return self.success().no_content_204().get_response()
