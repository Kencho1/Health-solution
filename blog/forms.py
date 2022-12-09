from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=120)
    class Meta:
        model = Comment
        fields = ['content']