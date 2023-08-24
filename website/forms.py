from django import forms
from django.forms import ValidationError

from .models import ContactUs, JoinUs


class HoneypotField(forms.BooleanField):
    default_widget = forms.CheckboxInput(
        {"style": "display:none !important;", "tabindex": "-1", "autocomplete": "off"}
    )

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", HoneypotField.default_widget)
        kwargs["required"] = False
        super().__init__(*args, **kwargs)

    def clean(self, value):
        if cleaned_value := super().clean(value):
            raise ValidationError("")
        else:
            return cleaned_value



class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        asdf = HoneypotField()
        fields = ['name', 'phone', 'email', 'city', 'state','query_type', 'message']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'city':forms.TextInput(attrs={'class':'form-control'}),
                   'state':forms.Select(attrs={'class':'form-control'}),
                   'query_type':forms.Select(attrs={'class':'form-control'}),
                   
                   'message': forms.Textarea(attrs={'class': 'form-control'}),
                   }


class JoinUsForm(forms.ModelForm):
    class Meta:
        model = JoinUs
        fields = ['name', 'phone', 'email', 'qualification', 'city', 'state', 'applied_for', 'resume_file']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'applied_for':forms.Select(attrs={'class':'form-control'}),
            'resume_file':forms.FileInput(attrs={'class':'form-control'}),
        }