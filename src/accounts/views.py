from .forms import CustomUserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response


############--Signup Views --##############
'''
https://medium.com/@blakeyang22/django-signup-with-activation-email-via-api-7384e6766710
'''
@api_view()
def null_view(request):
    # null_view is used to handle the url redirection from django-allauth.
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    # complete_view is used to provide the successfully feedback page to
    #  end-user once he/she clicks the activation link from email. 
    # You might want to change it rather than plain-text response.
    return Response("Email account is activated")
