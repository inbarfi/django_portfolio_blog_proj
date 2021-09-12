from django import forms
from .models import ProjComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProjComment
        fields = ['name', 'email', 'body']