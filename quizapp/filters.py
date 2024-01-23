import django_filters
from .models import Result
from django import forms


class ResultFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains', label='first_name',
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    total_ball = django_filters.NumberFilter(lookup_expr='icontains', label='Title',
                                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    balls = django_filters.NumericRangeFilter(lookup_expr='icontains', label='range',
                                              widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Result
        fields = ['total_ball', 'username', 'balls']
