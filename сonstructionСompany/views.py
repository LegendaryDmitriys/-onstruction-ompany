import csv

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Personnel, Address, Order, Material, Warehouse, Project
from .forms import PersonnelForm, AddressForm, OrderForm, MaterialForm, WarehouseForm, SearchForm, ProjectForm

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('personnel_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('personnel_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def personnel_list(request):
    personnel = Personnel.objects.all()
    return render(request, 'personnel/personnel_list.html', {'personnel': personnel})


@login_required
def personnel_detail(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    return render(request, 'personnel/personnel_detail.html', {'personnel': personnel})

@login_required
def personnel_new(request):
    if request.method == "POST":
        form = PersonnelForm(request.POST)
        if form.is_valid():
            personnel = form.save(commit=False)
            personnel.save()
            return redirect('personnel_detail', pk=personnel.pk)
    else:
        form = PersonnelForm()
    return render(request, 'personnel/personnel_edit.html', {'form': form})

@login_required
def personnel_edit(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            personnel = form.save(commit=False)
            personnel.save()
            return redirect('personnel_detail', pk=personnel.pk)
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'personnel/personnel_edit.html', {'form': form})

@login_required
def personnel_delete(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    personnel.delete()
    return redirect('personnel_list')


@login_required
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address/address_list.html', {'addresses': addresses})

@login_required
def address_detail(request, pk):
    address = get_object_or_404(Address, pk=pk)
    return render(request, 'address/address_detail.html', {'address': address})
@login_required
def address_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm()
    return render(request, 'address/address_edit.html', {'form': form})
@login_required
def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm(instance=address)
    return render(request, 'address/address_edit.html', {'form': form})
@login_required
def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    address.delete()
    return redirect('address_list')

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})
@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order/order_detail.html', {'order': order})
@login_required
def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order/order_edit.html', {'form': form})
@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/order_edit.html', {'form': form})
@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')
@login_required
# Material Views
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material/material_list.html', {'materials': materials})
@login_required
def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'material/material_detail.html', {'material': material})
@login_required
def material_new(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.save()
            return redirect('material_detail', pk=material.pk)
    else:
        form = MaterialForm()
    return render(request, 'material/material_edit.html', {'form': form})
@login_required
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save(commit=False)
            material.save()
            return redirect('material_detail', pk=material.pk)
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material/material_edit.html', {'form': form})
@login_required
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    return redirect('material_list')

@login_required
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse/warehouse_list.html', {'warehouses': warehouses})
@login_required
def warehouse_detail(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    return render(request, 'warehouse/warehouse_detail.html', {'warehouse': warehouse})
@login_required
def warehouse_new(request):
    if request.method == "POST":
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.save()
            return redirect('warehouse_detail', pk=warehouse.pk)
    else:
        form = WarehouseForm()
    return render(request, 'warehouse/warehouse_edit.html', {'form': form})
@login_required
def warehouse_edit(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == "POST":
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.save()
            return redirect('warehouse_detail', pk=warehouse.pk)
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouse/warehouse_edit.html', {'form': form})
@login_required
def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    warehouse.delete()
    return redirect('warehouse_list')

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project_detail.html', {'project': project})

@login_required
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'project/project_edit.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project/project_edit.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')


def search_list_view(request, model, search_fields, template_name):
    form = SearchForm(request.GET or None)
    items = model.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            from django.db.models import Q
            queries = Q()
            for field in search_fields:
                queries |= Q(**{f"{field}__icontains": query})
            items = items.filter(queries)

    return render(request, template_name, {'items': items, 'form': form})
from django.db.models import Q

def export_search_csv(request, model):
    query = request.GET.get('query', '')
    items = model.objects.none()

    if model == Personnel:
        items = model.objects.filter(
            Q(full_name__icontains=query) |
            Q(position__icontains=query) |
            Q(salary__icontains=query) |
            Q(phone__icontains=query) |
            Q(experience__icontains=query)
        )
    elif model == Address:
        items = model.objects.filter(
            Q(address__icontains=query)
        )
    elif model == Order:
        items = model.objects.filter(
            Q(project__name__icontains=query) |
            Q(address__address__icontains=query) |
            Q(completion_date__icontains=query) |
            Q(cost__icontains=query)
        )
    elif model == Material:
        items = model.objects.filter(
            Q(name__icontains=query) |
            Q(weight__icontains=query) |
            Q(quantity__icontains=query) |
            Q(cost__icontains=query) |
            Q(project__name__icontains=query) |
            Q(purchase__icontains=query)
        )
    elif model == Warehouse:
        items = model.objects.filter(
            Q(material__name__icontains=query) |
            Q(material__quantity__icontains=query) |
            Q(material__weight__icontains=query) |
            Q(material__cost__icontains=query) |
            Q(material__purchase__icontains=query)
        )
    elif model == Project:
        items = model.objects.filter(
            Q(name__icontains=query)
        )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model.__name__.lower()}_search_results.csv"'

    writer = csv.writer(response)
    if model == Personnel:
        writer.writerow(['id', 'full_name', 'position', 'salary', 'phone', 'address', 'experience'])
        for item in items:
            writer.writerow([item.id, item.full_name, item.position, item.salary, item.phone, item.address, item.experience])
    elif model == Address:
        writer.writerow(['id', 'address'])
        for item in items:
            writer.writerow([item.id, item.address])
    elif model == Order:
        writer.writerow(['id', 'project', 'completion_date', 'cost', 'address_id'])
        for item in items:
            writer.writerow([item.id, item.project, item.completion_date, item.cost, item.address.address])
    elif model == Material:
        writer.writerow(['id', 'name', 'weight', 'quantity', 'cost', 'project', 'purchase'])
        for item in items:
            writer.writerow([item.id, item.name, item.weight, item.quantity, item.cost, item.project, item.purchase])
    elif model == Warehouse:
        writer.writerow(['id', 'material_name', 'material_weight', 'material_quantity', 'material_cost'])
        for item in items:
            writer.writerow([item.id, item.material.name, item.material.weight, item.material.quantity, item.material.cost])
    elif model == Project:
        writer.writerow(['id', 'name'])
        for item in items:
            writer.writerow([item.id, item.name])

    return response

