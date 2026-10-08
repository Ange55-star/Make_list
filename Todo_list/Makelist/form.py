from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Note, Task, UserPreference


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Titre de la tâche'}),
            'description': forms.Textarea(attrs={'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500', 'rows': 4, 'placeholder': 'Description'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500'}),
            'completed': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-indigo-600 rounded'}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Titre de la note'}),
            'content': forms.Textarea(attrs={'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500', 'rows': 5, 'placeholder': 'Écris ton idée ici...'}),
        }


class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['sleep_time', 'rest_time', 'wake_time', 'focus_duration']
        widgets = {
            'sleep_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500'}),
            'rest_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500'}),
            'wake_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500'}),
            'focus_duration': forms.NumberInput(attrs={'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 focus:ring-2 focus:ring-indigo-500'}),
        }
