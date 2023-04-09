from django import forms

class Contactform(forms.Form):
    your_name = forms.CharField(label="Your name:", max_length=100, required=True)
    your_email = forms.EmailField(label="Your email:", required=True)
    comentary = forms.CharField(label="Leave a comment:", widget=forms.Textarea)
