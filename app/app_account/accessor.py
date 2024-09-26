from app.utils.utils import get_or_none
from app.models import Account


class AccountAccessor:
    
    @classmethod
    def get_account(cls, **kwargs):
     return get_or_none(Account, **kwargs)
