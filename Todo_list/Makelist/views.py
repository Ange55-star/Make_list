from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .form import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html/', {'tasks' :tasks})

def add_task(request):
    #Utilisateur a cliquer sur le bouton ajouter
    if request.method == 'POST':
        form = TaskForm(request.POST)  ##permet de gerer un formulaire automatiquement
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm() #Formulaire tout euf et vide
    return render(request, 'Makelist/task.html', {'form' :form})
def update_task(request, id):
    task = get_object_or_404(Task, id=id) ##On recupère les taches existante ou on envoie une erreur si elle n'existe
    if request.method == 'POST':
        # On passe les données du POST MAIS on précise bien quelle "instance" (tâche) modifier
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'Makelist/task.html', {'form' :form})
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'Makelist/task.html', {'task' :task})


