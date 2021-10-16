from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('traits', views.traits_view, name='traits'),
    #     path('update_trait/<str:pk>/',
    #          views.updateTrait, name='update_trait'),
    #     path('delete_trait/<str:pk>/',
    #          views.deleteTrait, name='delete_trait'),
]
