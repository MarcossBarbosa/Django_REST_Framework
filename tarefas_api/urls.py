from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tarefas.views import (
    TarefaViewSet,
    MinhasTarefasView,
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    UserCreateView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/tarefas', TarefaViewSet)  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
    path('api/minhas-tarefas/', MinhasTarefasView.as_view(), name='minhas-tarefas'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserCreateView.as_view(), name='user_register'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]