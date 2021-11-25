from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register("user", views.UserViewSet)
router.register("todo", views.TodoViewSet)

urlpatterns = [
    path("", views.hello_world, name="hello world"),
]

urlpatterns += router.urls
