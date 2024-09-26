from app.utils.utils import get_or_none
from app.models import Teacher

class TeacherAccessor:
    
    @classmethod
    def get_teacher(cls, **kwargs):
        return get_or_none(Teacher, **kwargs)
