from app.app_admin.accessor import AdminAccessor
from rest_framework_simplejwt.tokens import RefreshToken

class Admin:
    def __init__(self, admin):
        self.admin = admin

    @staticmethod
    def get_admin_by_id(id):
        return AdminAccessor.get_admin(id=id)

    @staticmethod
    def get_admin_by_email(email):
        return AdminAccessor.get_admin(email=email)

    def generate_auth_token(self):
        refresh = RefreshToken.for_user(self.admin)
        return str(refresh.access_token)
    
    @classmethod
    def login(cls, email, raw_password):
        admin = cls.get_admin_by_email(email)
        if not admin:
            return None
        if raw_password!=admin.password:
            return None
        return  cls(admin).generate_auth_token()
    
