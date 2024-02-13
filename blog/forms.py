from django import forms


class EmailPostForm(forms.Form):
    """Form for sharing post."""

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
