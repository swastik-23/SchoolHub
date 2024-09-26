from app.app_classes.accessor import ClassesAccessor
from rest_framework_simplejwt.tokens import RefreshToken

class Class:
    def __init__ (self, classes):
        self.account = classes
        
        @staticmethod
        def get_class_by_id(id):
            return ClassesAccessor.get_class(id=id)
        
        def generate_auth_token(self):
            refresh = RefreshToken.for_user(self.admin)
            return str(refresh.access_token)
        
