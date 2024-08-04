from django.contrib import admin
from django.urls import path, include
from tracker.views import HomeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('', include('tracker.urls')),
]
