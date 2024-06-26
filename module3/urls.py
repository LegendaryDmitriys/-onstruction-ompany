from djangoProject.urls import  path
from module3 import views
from module3.models import Test

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register_view, name='register'),

    # path("test/", views.test_list, name="test_list"),
    path("test/<int:pk>/", views.test_detail, name="test_detail"),
    path('test/add/', views.test_add, name="test_add"),
    path('test/<int:pk>/edit/', views.test_edit, name='test_edit'),
    path('test/<int:pk>/delete/', views.test_delete, name='test_delete'),

    path('test/', views.search, {"model" : Test, "search_field" : ["vopros", "otvet", "complexity"], "template_name" : "test/test_list.html"},  name="test_list"),
    path('test/export', views.export_csv, {"model" : Test}, name="test_export"),
]

