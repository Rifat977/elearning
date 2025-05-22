from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_true_false_game, name='index_true_false_game'),

]
