from app.utils.utils import get_or_none
from app.models import Classes


class ClassesAccessor:
    
    @classmethod
    def get_classes(cls, **kwargs):
        return get_or_none(Classes,**kwargs)
    