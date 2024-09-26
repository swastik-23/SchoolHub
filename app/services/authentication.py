from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from app.app_admin.service import Admin
from app.app_account.service import Account
from app.app_teacher.service import Teacher
from app.app_student.service import Student

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            raise NotAuthenticated("Authorization header missing")

        try:
            token = auth_header.split(" ")[1]
            payload = AccessToken(token).payload

            id = payload.get(settings.SIMPLE_JWT["USER_ID_CLAIM"])
            user = self.get_user_by_id(id) if id else None
            if not user:
                raise AuthenticationFailed("Invalid auth token")

            return user, None

        except AuthenticationFailed as e:
            raise e
        except Exception as e:
            raise AuthenticationFailed("Invalid auth token")

    def get_user_by_id(self, id):
        raise NotImplementedError("Subclasses must implement this method")

class AdminAuthentication(JWTAuthentication):
    def get_user_by_id(self, id):
        return Admin.get_admin_by_id(id)

class AccountAuthentication(JWTAuthentication):
    def get_user_by_id(self, id):
        return Account.get_account_by_id(id)

class TeacherAuthentication(JWTAuthentication):
    def get_user_by_id(self, id):
        return Teacher.get_teacher_by_id(id)
    
class StudentAuthentication(JWTAuthentication):
    def get_user_by_id(self, id):
        return Student.get_student_by_id(id)