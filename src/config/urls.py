from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from accounts.views import null_view, complete_view
from rest_framework.documentation import include_docs_urls
from allauth.account.views import ConfirmEmailView
from rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts', include('accounts.urls')),

    
    #Rest-auth
     # Override urls
    url(r'^rest-auth/registration/account-email-verification-sent/', 
        null_view, name='account_email_verification_sent'),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', 
        ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^rest-auth/registration/complete/$', 
        complete_view, name='account_confirm_complete'),
    path('rest-auth/password-reset/confirm/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    #api docs
    path(r'docs/', include_docs_urls(title='Whiteboard API')),


]

# for image i guess
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
