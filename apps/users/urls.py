from django.urls import path
from django.views.generic import TemplateView
from .views import register_view
from django.contrib.auth import views as auth_views

app_name = 'users'  # Очень важно для {% url 'users:...' %} в шаблонах

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Новые страницы форума
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('rules/', TemplateView.as_view(template_name='rules.html'), name='rules'),
]
