from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .form import NoteForm, RegistrationForm, TaskForm, UserPreferenceForm
from .models import Note, Task, UserPreference


def build_chart_data(tasks):
    """Construit des données simples pour le graphique du dashboard."""
    if not tasks:
        return [{'label': 'Aucune donnée', 'value': 0}]

    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    completed_ratio = round((completed / total) * 100, 1) if total else 0

    return [
        {'label': 'Aujourd’hui', 'value': completed_ratio},
        {'label': 'Semaine', 'value': min(100, completed_ratio + 10)},
        {'label': 'Mois', 'value': min(100, completed_ratio + 20)},
    ]


@login_required(login_url='login')
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')[:5]
    preference, _ = UserPreference.objects.get_or_create(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    completion_rate = round((completed_tasks / total_tasks) * 100, 1) if total_tasks else 0

    return render(
        request,
        'dashboard.html',
        {
            'tasks': tasks[:5],
            'notes': notes,
            'preference': preference,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'completion_rate': completion_rate,
            'chart_data': build_chart_data(tasks),
        },
    )


@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks.html', {'tasks': tasks})


@login_required(login_url='login')
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'La tâche a bien été ajoutée.')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'mode': 'create'})


@login_required(login_url='login')
def task_update(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'La tâche a été mise à jour.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'mode': 'edit', 'task': task})


@login_required(login_url='login')
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'La tâche a été supprimée.')
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})


@login_required(login_url='login')
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'notes.html', {'notes': notes})


@login_required(login_url='login')
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'La note a été enregistrée.')
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form, 'mode': 'create'})


@login_required(login_url='login')
def note_update(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'La note a été mise à jour.')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form, 'mode': 'edit', 'note': note})


@login_required(login_url='login')
def note_delete(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'La note a été supprimée.')
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})


@login_required(login_url='login')
def preferences(request):
    preference, _ = UserPreference.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserPreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vos préférences ont été enregistrées.')
            return redirect('preferences')
    else:
        form = UserPreferenceForm(instance=preference)
    return render(request, 'preferences.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Connexion réussie.')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserPreference.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

