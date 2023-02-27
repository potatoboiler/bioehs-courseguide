from django import forms
from . import models
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class YearForm(forms.Form):
    sorted_semesters = models.Semester.semesters.all().order_by('-year', 'term')
    #sorted_semesters = models.Semester.semesters.all()[::-1]
    CHOICES = [(str(s), str(s)) for s in sorted_semesters]
    semesters = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
