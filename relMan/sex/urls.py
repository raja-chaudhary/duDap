from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sex-counter', views.sex_view, name='sex-counter'),
    #     path('update_sex/<str:pk>/',
    #          views.updateSex, name='update_sex'),
    #     path('delete_sex/<str:pk>/',
    #          views.deleteSex, name='delete_sex'),
]
