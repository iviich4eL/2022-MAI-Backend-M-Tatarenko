from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film/<int:film_id>/', views.film_by_id, name='film'),
    path('film', views.read_film, name='film'),
    path('film/update', views.update_film, name='film'),
]
