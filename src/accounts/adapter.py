from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from allauth.utils import build_absolute_uri

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.user_type = data.get('user_type')
        user.save()
        return user

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = settings.CUSTOM_ACCOUNT_CONFIRM_EMAIL_URL + emailconfirmation.key
        ret = build_absolute_uri(
            request,
            url)
        return ret
