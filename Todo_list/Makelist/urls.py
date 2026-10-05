from zipfile import Path

from django.urls import path
from .import views

urlpatterns = [
    path("tasks/", views.task_list, name="task_list"),
    path("Ajouter/", views.add_task, name="add_task"),
    path("modifier/<int:id>/", views.update_task, name="update_task"),
    path("supprimer/<int:id>/", views.delete_task, name="delete_task"),
]