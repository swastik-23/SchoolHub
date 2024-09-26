from app.utils.utils import get_or_none
from app.models import Admin
from app.models import Account
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BaseAccessor:
    model = None

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.model.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def create(cls, **kwargs):
        return cls.model.objects.create(**kwargs)

    @classmethod
    def update(cls, id, **kwargs):
        obj = cls.get_by_id(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    @classmethod
    def delete(cls, id):
        obj = cls.get_by_id(id)
        if obj:
            obj.delete()
            return True
        return False
    
    

class AdminAccessor(BaseAccessor):
    model = Admin
    
    @classmethod
    def get_admin(cls, **kwargs):
        try:
            return cls.model.objects.filter(**kwargs).first()
        except ObjectDoesNotExist:
            return None


class AccountAccessor(BaseAccessor):
    model = Account