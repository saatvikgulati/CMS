from .models import Content,Comment
from django import forms
import os
from django.core.exceptions import ValidationError
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
class ContentCreateForm(forms.ModelForm):
    class Meta:
        model=Content
        fields=['title','body','summary','categories','pdf']