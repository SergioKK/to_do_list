from django.views.generic import ListView

from .models import Todo
from rest_framework import viewsets
from .serializers import TodoSerializer


class TodoListView(ListView):
    model = Todo
    template_name = 'todo.html'
    context_object_name = 'tasks'


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer