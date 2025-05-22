from rest_framework import viewsets, generics, permissions, filters
from .models import Tarefa
from .serializers import TarefaSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

# ViewSet para operações completas (opcional)
class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View personalizada para listar tarefas do usuário
class MinhasTarefasView(generics.ListAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

# View para CRUD de tarefas (usando TarefaSerializer)
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_in']
    filterset_fields = ['completed']

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]