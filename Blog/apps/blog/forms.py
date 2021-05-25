from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField()
    publish = forms.DateField()
    class Meta:
        model = Comment
        fields = [
            'blogId',
            'text'
        ]
