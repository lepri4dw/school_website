from django import forms
from .models import Application
from django.core.exceptions import ValidationError
import re


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['parent_name', 'phone_number', 'full_name', 'birth_date', 'class_number', 'previous_school']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^(\+996)?\d{9}$', phone_number):
            raise ValidationError('Введите корректный номер телефона. Например, +996555555555.')
        return phone_number
