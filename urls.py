from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.threads.urls', 'threads'), namespace='threads')),  # главная страница
    path('users/', include(('apps.users.urls', 'users'), namespace='users')),   # страница пользователей
]
