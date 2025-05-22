from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    STATUS = (
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)  
    due_date = models.DateField(null=True, blank=True)  
    created_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title