from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Ad
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'number', 'email', 'profile_pic', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'number': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почтовый ящик'})
        }
        error_messages = {
            'first_name': {'required':'Введите имя', 'max_length':'Слишком много символов'},
            'last_name': {'required': 'Введите фамилию', 'max_length':'Слишком много символов'},
            'number': {'required': 'Введите номер телефона', 'unique': 'Данный номер телефона уже зарегистрирован', 'max_length':'Слишком много символов'},
            'email': {'required': 'Введите почтовый ящик', 'invalid':'Поле заполнено некорректно', 'unique': 'Данный почтовый ящик уже зарегистрирован'}
        }

class CreateAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('choice_group', 'title', 'description','price', 'address', 'pic')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок'}),
            'description': forms.Textarea(attrs={'placeholder': 'Описание'}),
            'address': forms.TextInput(attrs={'placeholder': 'Адрес (город)'}),
            'price': forms.TextInput(attrs={'placeholder': 'Цена'}),
        }
        error_messages = {
            'choice_group': {'required': 'Выберите категорию', 'invalid': 'Поле заполнено некорректно'},
            'title': {'required': 'Введите заголовок', 'invalid': 'Поле заполнено некорректно'},
            'description': {'required': 'Введите описание товара', 'invalid': 'Поле заполнено некорректно'},
            'address': {'required': 'Введите город, в котором актуально объявление', 'invalid': 'Поле заполнено некорректно'},
            'price': {'required': 'Напишите цену', 'invalid': 'Поле заполнено некорректно'},
        }

class EditProfile(ModelForm):
    profile_pic =  forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'number', 'email', 'profile_pic')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'number': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почтовый ящик'}),
        }
        error_messages = {
            'first_name': {'required': 'Введите имя', 'max_length': 'Слишком много символов'},
            'last_name': {'required': 'Введите фамилию', 'max_length': 'Слишком много символов'},
            'number': {'required': 'Введите номер телефона', 'unique': 'Данный номер телефона уже зарегистрирован',
                       'max_length': 'Слишком много символов'},
            'email': {'required': 'Введите почтовый ящик', 'invalid': 'Поле заполнено некорректно',
                      'unique': 'Данный почтовый ящик уже зарегистрирован'}
        }

class EditAd(ModelForm):
    pic = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Ad
        fields = ('choice_group', 'title', 'description','price', 'address', 'pic')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок'}),
            'description': forms.Textarea(attrs={'placeholder': 'Описание'}),
            'address': forms.TextInput(attrs={'placeholder': 'Адрес (город)'}),
            'price': forms.TextInput(attrs={'placeholder': 'Цена'}),
        }
        error_messages = {
            'choice_group': {'required': 'Выберите категорию', 'invalid': 'Поле заполнено некорректно'},
            'title': {'required': 'Введите заголовок', 'invalid': 'Поле заполнено некорректно'},
            'description': {'required': 'Введите описание товара', 'invalid': 'Поле заполнено некорректно'},
            'address': {'required': 'Введите город, в котором актуально объявление', 'invalid': 'Поле заполнено некорректно'},
            'price': {'required': 'Напишите цену', 'invalid': 'Поле заполнено некорректно'},
        }