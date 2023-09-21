from django import forms
from .models import User

class StudentRegister(forms.ModelForm):
    class Meta():
        model=User#jis model ka form banana hai
        fields=["name","email","password"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"},render_value=True),
        }