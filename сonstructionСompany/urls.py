from django.urls import path
from . import views
from .models import Personnel, Address, Order, Material, Warehouse, Project
from .views import search_list_view, export_search_csv

urlpatterns = [

    # path('personnel/', views.personnel_list, name='personnel_list'),
    path('personnel/<int:pk>/', views.personnel_detail, name='personnel_detail'),
    path('personnel/new/', views.personnel_new, name='personnel_new'),
    path('personnel/<int:pk>/edit/', views.personnel_edit, name='personnel_edit'),
    path('personnel/<int:pk>/delete/', views.personnel_delete, name='personnel_delete'),

    # path('addresses/', views.address_list, name='address_list'),
    path('addresses/<int:pk>/', views.address_detail, name='address_detail'),
    path('addresses/new/', views.address_new, name='address_new'),
    path('addresses/<int:pk>/edit/', views.address_edit, name='address_edit'),
    path('addresses/<int:pk>/delete/', views.address_delete, name='address_delete'),

    # path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/new/', views.order_new, name='order_new'),
    path('orders/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),

    # path('materials/', views.material_list, name='material_list'),
    path('materials/<int:pk>/', views.material_detail, name='material_detail'),
    path('materials/new/', views.material_new, name='material_new'),
    path('materials/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('materials/<int:pk>/delete/', views.material_delete, name='material_delete'),

    # path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/<int:pk>/', views.warehouse_detail, name='warehouse_detail'),
    path('warehouses/new/', views.warehouse_new, name='warehouse_new'),
    path('warehouses/<int:pk>/edit/', views.warehouse_edit, name='warehouse_edit'),
    path('warehouses/<int:pk>/delete/', views.warehouse_delete, name='warehouse_delete'),

    # path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/new/', views.project_new, name='project_new'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),


    path('personnel/', search_list_view,
         {'model': Personnel, 'search_fields': ['full_name', 'position', 'salary', 'phone', 'experience'],
          'template_name': 'personnel/personnel_list.html'}, name='personnel_list'),
    path('address/', search_list_view,
         {'model': Address, 'search_fields': ['address'], 'template_name': 'address/address_list.html'},
         name='address_list'),
    path('order/', search_list_view,
         {'model': Order, 'search_fields': ['project__name', 'completion_date', 'cost'],
          'template_name': 'order/order_list.html'}, name='order_list'),
    path('material/', search_list_view,
         {'model': Material, 'search_fields': ['name', 'quantity'], 'template_name': 'material/material_list.html'},
         name='material_list'),
    path('warehouse/', search_list_view,
         {'model': Warehouse, 'search_fields': ['material__name'], 'template_name': 'warehouse/warehouse_list.html'},
         name='warehouse_list'),
    path('projects/', search_list_view,
         {'model': Project, 'search_fields': ['name'],
          'template_name': 'project/project_list.html'}, name='project_list'),

    path('personnel/export/', export_search_csv, {'model': Personnel}, name='export_personnel_csv'),
    path('projects/export', export_search_csv, {'model': Project}, name='export_projects_csv'),
    path('address/export/', export_search_csv, {'model': Address}, name='export_address_csv'),
    path('order/export/', export_search_csv, {'model': Order}, name='export_order_csv'),
    path('material/export/', export_search_csv, {'model': Material}, name='export_material_csv'),
    path('warehouse/export/', export_search_csv, {'model': Warehouse}, name='export_warehouse_csv'),

]
