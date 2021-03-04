from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50, null=True, help_text='Введите своё имя. Максимальное кол-во символов 50.')
    last_name = models.CharField(max_length=50, null=True, help_text='Введите свою фамилию. Максимальное кол-во символов 50.')
    number = models.CharField(max_length=11, null=True, unique=True, help_text='Введите номер телефона. Максимальное кол-во символов 11.')
    email = models.EmailField(max_length=254, null=True, unique=True, help_text='Введите почту.')
    profile_pic = models.ImageField(null=True, blank=True, default='img-cat.png')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Ad(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    groups = (
        ('Услуги', 'Услуги'),
        ('Животные', 'Животные'),
        ('Вещи', 'Вещи'),
        ('Техника', 'Техника')
    )
    choice_group = models.CharField(max_length= 10, choices=groups)
    title = models.CharField(max_length=50, help_text='Введите название товара. Максимальное кол-во символов 50.')
    description = models.CharField(max_length=254, help_text='Опишите товар/услугу. Максимальное кол-во символов 254')
    address = models.CharField(max_length=254, help_text='Введите город, в котором актуально объявление. Максимальное кол-во символов 254')
    pic = models.ImageField(null=True, blank=True, default='img-cat.png')
    price = models.CharField(max_length=11, help_text='Цена', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    REQUIRED_FIELDS = ['choice_group', 'title', 'address']

    def __str__(self):
        return self.title