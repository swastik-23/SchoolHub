from app.app_student.accessor import StudentAccessor

class Student:
    def __init__(self, student):
        self.student =student
        
        @staticmethod
        def get_student_by_id(id):
            return StudentAccessor.get_student(id=id)
        
        @staticmethod
        def get_student_by_email(email):
            return StudentAccessor.get_student(email=email)
        