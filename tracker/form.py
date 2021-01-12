from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.forms import ModelForm
from .models import *


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields

class DateInput(forms.DateInput):
    input_type = 'date'

class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=['category','amount','comments','date_added']
        widgets = {
            'date_added': DateInput(),
        }