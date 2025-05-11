from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Все урлы форума
    path('',    include(('apps.threads.urls', 'threads'), namespace='threads')),

    # Все урлы пользователей (логин/рег/профиль)
    path('users/', include(('apps.users.urls',   'users'),   namespace='users')),
]
