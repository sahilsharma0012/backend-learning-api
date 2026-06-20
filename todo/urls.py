from django.urls import path, include
from rest_framework.routers import DefaultRouter

#from .views import todo_list, todo_detail, register_user
#from .views import TodoListCreateView, TodoDetailsView, register_user
from .views import TodoViewSet, register_user


router = DefaultRouter()
router.register('todos', TodoViewSet, basename = 'todos')

urlpatterns = [
    # path('todos/', TodoListCreateView.as_view()),
    # path('todos/<int:pk>/', TodoDetailsView.as_view()),
    
    path('', include(router.urls)),
    
    path('register/', register_user),
]
