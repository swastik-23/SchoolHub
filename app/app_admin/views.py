from app.shared.response_builder import ResponseBuilder
from app.shared.serializers import LoginSerializer
from app.app_admin.serializers import AdminSerializer
from app.app_student.serializers import StudentSerializer
from app.app_teacher.serializers import TeacherSerializer
from app.app_account.serializers import AccountSerializer
from app.app_course.serializers import CourseSerializer 
from app.app_classes.serializers import ClassSerializer  
from app.app_admin.service import Admin
from app.app_student.service import Student
from app.app_teacher.service import Teacher
from app.app_course.service import Course  
from app.app_classes.service import Class 
from rest_framework.decorators import api_view, authentication_classes
from app.services.authentication import AdminAuthentication



@api_view(["GET"])
@authentication_classes([AdminAuthentication])
def get_admin_info(request):
    """
    Get admin information
    """

    response_builder = ResponseBuilder()
    admin = request.user
    serializer = AdminSerializer(admin)
    return response_builder.get_200_success_response("Admin data fetched", serializer.data)

@api_view(["POST"])
def login(request):
    """
    Login admin and generate auth token.
    """

    response_builder = ResponseBuilder()
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.get_400_bad_request_response("Invalid Input", serializer.errors)
    auth_token = Admin.login(serializer.validated_data['email'], serializer.validated_data['password'])
    if not auth_token:
        return response_builder.get_400_bad_request_response("Invalid credentials")

    admin = Admin.get_admin_by_email(serializer.validated_data['email'])
    admin_serializer = AdminSerializer(admin)
    result = {
        "access_token": auth_token,
        "admin": admin_serializer.data
    }
    return response_builder.get_200_success_response("Admin logged in", result)

@api_view(["POST"])
def create_student(request):
    """
    Create student
    """
    response_builder = ResponseBuilder()
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.get_400_bad_request_response("Invalid Input", serializer.errors)
    student = serializer.save()
    student_serializer = StudentSerializer(student)
    return response_builder.get_201_created_response("Student created successfully", student_serializer.data)

@api_view(["POST"])
def create_teacher(request):
    """
    Create teacher
    """
    response_builder = ResponseBuilder()
    serializer = TeacherSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.get_400_bad_request_response("Invalid Input", serializer.errors)
    teacher = serializer.save()
    teacher_serializer = TeacherSerializer(teacher)
    return response_builder.get_201_created_response("Student created successfully", teacher_serializer.data)
    
@api_view(["POST"])
def create_account(request):
    """
    Create account
    """
    response_builder = ResponseBuilder()
    serializer = AccountSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.get_400_bad_request_response("Invalid Input", serializer.errors)
    account = serializer.save()
    account_serializer = AccountSerializer(account)
    return response_builder.get_201_created_response("Student created successfully", account_serializer.data)

@api_view(["GET"])
def get_all_students(request):
    """
    Get all students
    """
    response_builder = ResponseBuilder()
    students = StudentSerializer(Student.objects.all(), many=True)
    return response_builder.get_200_success_response("All students fetched", students.data)

@api_view(["GET"])
def get_students_by_class(request, class_id):
    """
    Get students by class
    """
    response_builder = ResponseBuilder()
    students = StudentSerializer(Student.objects.filter(class_id=class_id), many=True)
    return response_builder.get_200_success_response("Students fetched by class", students.data)

@api_view(["GET"])
def get_all_teachers(request):
    """
    Get all teachers
    """
    response_builder = ResponseBuilder()
    teachers = TeacherSerializer(Teacher.objects.all(), many=True)
    return response_builder.get_200_success_response("All teachers fetched", teachers.data)

@api_view(["GET"])
def get_teachers_by_course(request, course_id):
    """
    Get teachers by course
    """
    response_builder = ResponseBuilder()
    teachers = TeacherSerializer(Teacher.objects.filter(course_id=course_id), many=True)
    return response_builder.get_200_success_response("Teachers fetched by course", teachers.data)

@api_view(["GET"])
def get_all_courses(request):
    """
    Get all courses
    """
    response_builder = ResponseBuilder()
    courses = CourseSerializer(Course.objects.all(), many=True)  # Assuming CourseSerializer exists
    return response_builder.get_200_success_response("All courses fetched", courses.data)

@api_view(["GET"])
def get_course_by_class(request, class_id):
    """
    Get course by class
    """
    response_builder = ResponseBuilder()
    courses = CourseSerializer(Course.objects.filter(class_id=class_id), many=True)  # Assuming CourseSerializer exists
    return response_builder.get_200_success_response("Courses fetched by class", courses.data)

@api_view(["GET"])
def get_all_classes(request):
    """
    Get all classes
    """
    response_builder = ResponseBuilder()
    classes = ClassSerializer(Class.objects.all(), many=True)  # Assuming ClassSerializer exists
    return response_builder.get_200_success_response("All classes fetched", classes.data)
