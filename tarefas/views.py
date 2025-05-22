from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class MinhasTarefasView(ListAPIView):
    serializer_class = TarefaSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

    def list(self,request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({
                'messege': 'Você ainda não tem tarefas',
                'Criar tarefa': 'Crie uma tarefa'
            })
        return super().list(request, *args, **kwargs)