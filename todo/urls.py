from django.urls import path
from .views import todo_list, todo_detail, register_user

urlpatterns = [
    path('todos/', todo_list),
    path('todos/<int:pk>/', todo_detail),
    path('register/', register_user),
]
