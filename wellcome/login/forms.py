from .models import Person
from django.forms import ModelForm, TextInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name"]

        widgets = {
            "first_name": TextInput(attrs={
                'placeholder': "Ім'я"
            }),
            "last_name": TextInput(attrs={
                "placeholder": 'Призвіще'
            }
            )
        }
