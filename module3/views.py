import csv

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from module3.form import TestForm, SearchForm
from module3.models import Test


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('test_list')
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
            return redirect('test_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})




@login_required
def test_list(request):
    test = Test.objects.all()
    return render(request, 'test/test_list.html', {"test": test})

@login_required
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test/test_detail.html', {"test": test})

@login_required
def test_add(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.save()
            return redirect('test_detail', test.pk)
    else:
        form = TestForm()
    return render(request, 'test/test_edit.html', {'form': form})

@login_required
def test_edit(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save(commit=False)
            test.save()
            return redirect('test_detail', test.pk)
    else:
        form = TestForm(instance=test)
    return render(request, 'test/test_edit.html', {'form': form})

def test_delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('test_list')


def search(request, model, search_field, template_name):
    form = SearchForm(request.GET or None)
    items = model.objects.all()

    if form.is_valid():
       query = form.cleaned_data['query']
       if query:
           q = Q()
       for field in search_field:\
           q |= Q(**{f"{field}__icontains": query})

       items = items.filter(q)

    return render(request, template_name, {'form': form, 'items': items})





def export_csv(request, model):
    query = request.GET.get('query', '')
    items = model.objects.none()

    if model == Test:
        items = model.objects.filter(
            Q(vopros__icontains=query)
        )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model.__name__.lower()}.csv"'

    writer = csv.writer(response)
    if model == Test:
        writer.writerow(['vopros', 'otvet', 'complexity'])
        for item in items:
            writer.writerow([item.vopros, item.otvet, item.complexity])

    return response
