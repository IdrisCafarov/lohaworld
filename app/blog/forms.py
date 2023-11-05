from django import forms
from .models import *




class CreateEmailForm(forms.ModelForm):


    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        'type':'text',
        'placeholder':'Your Email'
        }
    ))

   
    class Meta:
        model = Email
        fields = ('email',)




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class CreateContactForm(forms.ModelForm):


    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        'type':'text',
        'placeholder':'Your Email'
        }
    ))

    name = forms.CharField(widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':'Your Name'
        }
    ))

    number = forms.CharField(widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':'Your Phone Number'
        }
    ))

    text = forms.CharField(widget=forms.Textarea(
        attrs={
        'type':'text',
        'placeholder':'Your Message'
        }
    ))

   
    class Meta:
        model = Contact
        fields = '__all__'




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

