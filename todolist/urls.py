from django.urls import path, include
from rest_framework import routers
from todolist.views import TodoListView, TodoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)


urlpatterns = [
    path('tasks/', TodoListView.as_view(), name='ListView'),
    path('api/', include(router.urls), name='api'),
]