from django.contrib import admin
from django.urls import path, include
from tarefas.views import MinhasTarefasView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tarefas.urls')),
    path('api/minhas-tarefas/', MinhasTarefasView.as_view(), name='minhas-tarefas'),
    path('api/auth/', include('rest_framework.urls')),
]
