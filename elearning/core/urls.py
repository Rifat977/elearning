from django.urls import path
from . import views

urlpatterns = [
    path('visualize', views.index, name='index'),
    path('', views.home, name='Home'),
    path('generate_simulation/', views.generate_simulation, name='generate_simulation'),

    path('myth-check/', views.myth_check, name='myth_check'),
    path('fact_check_api/', views.fact_check_api, name='fact_check_api'),
    path('role_play/', views.role_play, name='role_play'),
]
