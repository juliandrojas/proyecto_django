from django.urls import path
from .views import index, tasks
urlpatterns = [
    path('', index),
    path('tasks/', tasks),
]
