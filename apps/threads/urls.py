from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ThreadListView,
    ThreadDetailView,
    ThreadCreateView,
    ThreadUpdateView,
    ThreadDeleteView,
)

app_name = 'threads'  # <-- правильно, оставляем

urlpatterns = [
    # Главная страница списка тредов
    path('', ThreadListView.as_view(), name='thread_list'),

    # Статические страницы
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('rules/', TemplateView.as_view(template_name='rules.html'), name='rules'),

    # Действия с тредами
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/new/', ThreadCreateView.as_view(), name='thread_create'),
    path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread_update'),
    path('thread/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread_delete'),
]
