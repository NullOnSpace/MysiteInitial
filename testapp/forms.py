from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Validate Functions
def vali_username_exc(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(
            _('%(value)s already exists'),
            params={'value': value},
        )


# Customize Forms
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class UserForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass


class UserFormStrict(forms.Form):
    username = forms.CharField(min_length=3, max_length=12,
                               validators=[vali_username_exc])
    password = forms.CharField(min_length=8, max_length=16,
                               widget=forms.PasswordInput)
    email = forms.EmailField()


class PermissionGroupForm(forms.Form):
    Groups = (
        (2, 'Admin'),
        (1, 'Common')
    )
    group = forms.ChoiceField(choices=Groups)
