from app.shared.response_builder import ResponseBuilder
from app.app_classes.service import Classes
from app.app_classes.serializers import ClassesSerializer
from rest_framework.decorators import api_view, authentication_classes

@api_view(["GET"])
def get_classes_info(request):
    """
    Get classes information
    """
    
    response_builder = ResponseBuilder()
    account= request.user
    serializer = ClassesSerializer(account)
    return response_builder.get_200_success_response("Classes Data Fetched",serializer.data)

@api_view(["POST"])
def create_classes_info(request):
    """
    Create classes information
    """
    response_builder = ResponseBuilder()
    serializer = ClassesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response_builder.get_201_success_response("Classes Created", serializer.data)
    return response_builder.get_400_error_response("Invalid Data", serializer.errors)

