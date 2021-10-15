from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sex-counter', views.sex_view, name='sex-counter'),
    path('add_sex',
         views.addSex, name='add_sex'),
    path('delete_sex',
         views.deleteSex, name='delete_sex'),
]
