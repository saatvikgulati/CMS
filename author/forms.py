from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from validate_email import validate_email
from django.core.validators import RegexValidator
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=150)
    phone_regex=RegexValidator(regex=r'^\ ?1?\d{9,15}$',message="Phone no must be entered in format: Up to 10 digits allowed.")
    phone=forms.CharField(validators=[phone_regex],max_length=10)
    pincode_regex=RegexValidator(regex=r'^[1-9][0-9]{5}$',message="Pincode must be entered in format: Up to 6 digits allowed.")
    pincode=forms.CharField(validators=[pincode_regex],max_length=6)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone','pincode','password1','password2']
    def save(self,commit=True):
        user=super(UserRegisterForm,self).save(commit=False)
        user.save()
        user_profile=Profile(user=user,phone=self.cleaned_data.get('phone'))
        user_profile.save()
    def clean_email(self):
        email_passed=self.cleaned_data.get('email')
        is_valid=validate_email(email_passed,verify=True)
        if not is_valid:
            raise forms.ValidationError('Not a valid email')
        return email_passed

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=150)
    class Meta:
        model=User
        fields=['email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['country','city','state','phone','address','pincode','image']