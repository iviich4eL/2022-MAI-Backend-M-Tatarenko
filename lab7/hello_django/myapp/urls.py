from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creator/<int:creator_id>/', views.read_creator_by_id, name='creator_by_id'),
    path('creator/create', views.create_creator, name='create_creator'),
    path('creator/delete/<str:nickname>', views.delete_creator_by_nikname, name='delete_creator_by_nikname')
]
