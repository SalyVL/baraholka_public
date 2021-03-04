import django_filters
from django_filters import CharFilter, ChoiceFilter
from django.forms.widgets import TextInput

from .models import Ad

class AdFilter(django_filters.FilterSet):
    choice_group = ChoiceFilter(choices=Ad.groups, label='', empty_label='Категория объявления')
    title = CharFilter(field_name='title', lookup_expr='icontains', label='', widget=TextInput(attrs={'placeholder': 'Заголовок', 'id':'search-form'}))
    address = CharFilter(field_name='address', lookup_expr='icontains', label='', widget=TextInput(attrs={'placeholder': 'Город', 'id':'search-form'}))

    class Meta:
        model = Ad
        fields = ('choice_group', 'title', 'address')