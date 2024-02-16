from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    """Form for sharing post."""

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Form for comment."""

    class Meta:

        model = Comment
        fields = ['name', 'email', 'body']
