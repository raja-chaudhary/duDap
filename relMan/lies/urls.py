from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lies', views.lie_view, name='lies'),
    path('update_lie/<str:pk>/',
         views.updateLie, name='update_lie'),
    path('delete_lie/<str:pk>/',
         views.deleteLie, name='delete_lie'),
]
