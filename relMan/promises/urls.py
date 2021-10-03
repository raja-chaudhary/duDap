from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('promises', views.promise_view, name='promises'),
    path('update_promise/<str:pk>/',
         views.updatePromise, name='update_promise'),
    path('delete_promise/<str:pk>/',
         views.deletePromise, name='delete_promise'),
]
