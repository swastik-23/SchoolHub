from app.shared.response_builder import ResponseBuilder
from app.shared.serializers import LoginSerializer
from app.app_account.service import Account
from app.app_account.serializers import AccountSerializer
from rest_framework.decorators import api_view, authentication_classes
from app.services.authentication import AccountAuthentication

@api_view(["GET"])
@authentication_classes([AccountAuthentication])
def get_account_info(request):
    """
    Get account information
    """
    
    response_builder =ResponseBuilder()
    account= request.user
    serializer = AccountSerializer(account)
    return response_builder.get_200_success_response("Account Data Fetched",serializer.data)

@api_view(["POST"])
def login(request):
    """
    Login Account and generate auth token.
    """
    
    response_builder =ResponseBuilder()
    serializer= LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.get_400_bad_request_response("innvalid Input",serializer.errors)
    auth_token=Account.login(serializer.validate_data['email'],serializer.validate_data['password'])
    if not auth_token:
        return response_builder.get_400_bad_request_response("Invalid Credential")
    
    account=account.get_account_by_email(serializer.validate_data['email'])
    account_serialaizer =AccountSerializer(account)
    result={
        "access_token":auth_token,
        "account":account_serialaizer.data
    }
    return response_builder. get_200_success_response("Account logged in",result)