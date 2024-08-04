from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class StudySession(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()  # Duration in minutes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Ensure this field is added

    def __str__(self):
        return f"{self.task.name} - {self.started_at}"
    from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StudySession(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()  # Duration in minutes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)  # Ensure this field is included
    ended_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Ensure this field is included

    def __str__(self):
        return f"{self.task.name} - {self.started_at}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_study_time = models.DurationField(default=timedelta())

    def __str__(self):
        return self.user.username