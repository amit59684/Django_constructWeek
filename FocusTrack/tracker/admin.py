from django.contrib import admin
from .models import Task, StudySession, UserProfile

admin.site.register(Task)
admin.site.register(StudySession)
admin.site.register(UserProfile)
