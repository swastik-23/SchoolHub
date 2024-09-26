from app.app_teacher.accessor import TeacherAccessor

class Teacher:
    def __init__(self , teacher) :
        self.teacher = teacher
    
    @staticmethod
    def get_teacher_by_id(id):
        return TeacherAccessor.get_teacher(id=id)
    
    @staticmethod
    def get_teacher_by_email(email):
        return TeacherAccessor.get_teacher(email=email)
    
    