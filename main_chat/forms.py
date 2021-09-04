from .models import User_message
from django.forms import ModelForm, TextInput, Textarea, Select

ROOM_CHOISE=[
('0','главная'),
('1','кино'),
('2','музыка'),
]

class UsersForm(ModelForm):
    class Meta:
        model = User_message
        fields = ['name','message','room']

        widgets = {
            "name": TextInput(attrs={
                'placeholder':'Имя',
                'class':'form-name'
            }),
            "message": Textarea(attrs={
                'placeholder':'Сообщение',
                'class':'form-message'
            }),
            "room": Select(
            choices=ROOM_CHOISE

            )
            # "room": Select(choices=ROOM_CHOISE)
        }
