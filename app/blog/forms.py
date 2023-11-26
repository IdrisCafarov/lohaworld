from django import forms
from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _lazy




class CreateEmailForm(forms.ModelForm):


    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        'type':'text',
        'placeholder':_lazy('E-poçt')
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
        'placeholder':_lazy('E-poçt')
        }
    ))

    name = forms.CharField(widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':_lazy('Adınız')
        }
    ))

    number = forms.CharField(widget=forms.TextInput(
        attrs={
        'type':'text',
        'placeholder':_lazy('Əlaqə Nömrəniz')
        }
    ))

    text = forms.CharField(widget=forms.Textarea(
        attrs={
        'type':'text',
        'placeholder':_lazy('Mesajınız')
        }
    ))

   
    class Meta:
        model = Contact
        fields = '__all__'




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

