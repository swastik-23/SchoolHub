from app.utils.utils import get_or_none
from app.models import Student

class StudentAccessor:
    
     @classmethod
     def get_student(cls, **kwargs):
         return get_or_none(Student, **kwargs)