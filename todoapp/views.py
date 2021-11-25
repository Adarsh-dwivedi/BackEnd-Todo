from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import User, Todo
from .serializer import UserSerializer, TodoSerializer

# Create your views here.
def hello_world(request):
    return JsonResponse({
        "message": "Hello World! Successfull Hit"
    }, status=200)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer