from django import forms
from .models import Personnel, Address, Order, Material, Warehouse, Project


class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100, required=False)