from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dates', views.date_view, name='dates'),
    path('update_date/<str:pk>/',
         views.updateDate, name='update_date'),
    path('delete_date/<str:pk>/',
         views.deleteDate, name='delete_date'),
]
