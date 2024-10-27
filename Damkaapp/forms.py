from django import forms
from .models import *
from django.contrib.auth.models import User


class NewActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['Author', 'pub_date', 'author_profile','admin_profile', ]
        widgets = {
          'activity': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['Author', 'pub_date', 'author_profile','admin_profile', ]
        widgets = {
          'activity': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }