from django import forms
from django.db.models import fields
from django.forms.forms import Form
from .models import ContactForm

class ContactModelForm(forms.ModelForm):
   class Meta:
       model = ContactForm
       fields = "__all__"
