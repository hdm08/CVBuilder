from django import forms
from django.contrib.auth.models import User, Group
import django_filters

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    state = django_filters.CharFilter(lookup_expr='icontains')
    skills = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='icontains')
    # middle_name=django_filters.CharFilter(lookup_expr='icontains')
    # last_name=django_filters.CharFilter(lookup_expr='icontains')
    # gender = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['first_name','gender', 'city', 'state','skills']
