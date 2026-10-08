from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register_view, name='signup'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:id>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/new/', views.note_create, name='note_create'),
    path('notes/<int:id>/edit/', views.note_update, name='note_update'),
    path('notes/<int:id>/delete/', views.note_delete, name='note_delete'),
    path('preferences/', views.preferences, name='preferences'),
]