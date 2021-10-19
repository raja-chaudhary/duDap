from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('discussions', views.discussion_view, name='discussions'),
    path('update_discussion/<str:pk>/',
         views.updateDiscussion, name='update_discussion'),
    path('delete_discussion/<str:pk>/',
         views.deleteDiscussion, name='delete_discussion'),
]
