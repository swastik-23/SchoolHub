from app.app_admin.accessor import AccountAccessor
from rest_framework_simplejwt.tokens import RefreshToken

class Account:
    def __init__ (self, account):
        self.account =account
        
        @staticmethod
        def get_account_by_id(id):
            return AccountAccessor.get_account(id=id)
        
        @staticmethod
        def get_email_by_email(email):
            return AccountAccessor.get_account(email=email)
        
        def generate_auth_token(self):
            refresh = RefreshToken.for_user(self.admin)
            return str(refresh.access_token)
        
        @classmethod
        def login(cls ,email ,raw_password):
            account = cls.get_account_by_email(email)
            if not account:
                return None
            if raw_password!=account.password:  
                return None
            return cls(account).generate_auth_token()      