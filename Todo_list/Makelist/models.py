from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    """Une tâche utilisateur, avec date d'échéance et statut de complétion."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.completed and not self.completed_at:
            self.completed_at = timezone.now()
        elif not self.completed:
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Note(models.Model):
    """Une note rapide, indépendante des tâches, pour noter des idées."""

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserPreference(models.Model):
    """Préférences utilisateur pour le cycle sommeil/repos/réveil et le focus."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sleep_time = models.TimeField(default='22:30:00')
    rest_time = models.TimeField(default='00:30:00')
    wake_time = models.TimeField(default='07:00:00')
    focus_duration = models.PositiveIntegerField(default=25)

    def __str__(self):
        return f"Préférences de {self.user.username}"
