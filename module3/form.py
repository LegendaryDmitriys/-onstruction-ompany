from django import forms

from module3.models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class SearchForm(forms.Form):
    query = forms.CharField(label="Поиск", max_length=100, required=False)