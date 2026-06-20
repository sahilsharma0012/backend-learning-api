 ##################################################################
 #####################################################################################
 ###########################################################################################################
 ############ FUNCTION BASED VIEWS ############################################################################################  
 ######################################################################################################################################################

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Todo
# from .serializers import TodoSerializer

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes

# from django.contrib.auth.models import User
# from rest_framework import status


# ## GET and POST
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def todo_list(request):
#     ## GET request -> return all todos or row
#     if request.method == 'GET':
#         todo = Todo.objects.filter(user = request.user)
#         serializer = TodoSerializer(todo, many = True)
#         return Response(serializer.data)
    
#     ## POST request -> Create new todo or new row
#     if request.method == 'POST':
#         serializer = TodoSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save(user = request.user)       ## Django automatically runs: Todo.objects.create(...)
#             return Response({"message": "Data saved successfully", "data": serializer.data},status = 201)
        
#         return Response(serializer.errors, status = 400)
    
    
# ## GET(single object or row), PUT, POST
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def todo_detail(request, pk):
#     todo = Todo.objects.get(id = pk, user = request.user)       ## get_object_or_404(Todo, id=pk, user=request.user)
    
#     # GET (get the single row)
#     if request.method == 'GET': 
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
    
#     # PUT (update the row)
#     if request.method == 'PUT':
#         serializer = TodoSerializer(todo, data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Row updated successfully", "data": serializer.data}, status = 201)
        
#         return Response(serializer.errors, status = 400)
    
#     # DELETE (delete the row)
#     if request.method == 'DELETE':
#         deleted_row = todo.delete()
#         return Response({"message": "Row deleted", "data": deleted_row}, status = 200)
        

        
 ##################################################################
 #####################################################################################
 ###########################################################################################################
 ############ CLASS BASED VIEW OR APIView ############################################################################################  
 ###################################################################################################################################################### 
    

# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# from rest_framework.decorators import api_view
# from django.contrib.auth.models import User

# from .models import Todo
# from .serializers import TodoSerializer

# class TodoListCreateView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     # Get all todos or rows
#     def get(self, request):
#         todos = Todo.objects.filter(user = request.user)
#         serializer = TodoSerializer(todos, many = True)
#         return Response(serializer.data)
    
#     # Create Todos (POST)
#     def post(self, request):
#         serializer = TodoSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save(user = request.user)
#             return Response({"message": "Data saved Successfully", "data": serializer.data}, status = 201)
        
#         return Response(serializer.errors, status = 400)
    
    
# class TodoDetailsView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get_object(self, pk, user):
#         return get_object_or_404(Todo, id = pk, user = user)
    
#     # Get Single todo or row
#     def get(self, request, pk):
#         todo = self.get_object(pk, request.user)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)


#     # Update todo or row
#     def put(self, request, pk):
#         todo = self.get_object(pk, request.user)
#         serializer = TodoSerializer(todo, data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()    
#             return Response({"message": "Data is updated successfully", "data": serializer.data}, status = 201)
        
#         return Response(serializer.errors, status = 400)
    
    
#     # Delete todo or row
#     def delete(self, request, pk):
#         todo = self.get_object(pk, request.user)      
#         todo.delete()
#         return Response({"message": "Deleted Successfully"}, status = 201)  
    
    
    


      
 ##################################################################
 #####################################################################################
 ###########################################################################################################
 ############ Generic Views ############################################################################################  
 ###################################################################################################################################################### 
    
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from .models import Todo
# from .serializers import TodoSerializer

# from django.contrib.auth.models import User

# # GET and POST
# class TodoListCreateView(generics.ListCreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Todo.objects.filter(user = self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)
        
# # GET, PUT, DELETE        
# class TodoDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Todo.objects.filter(user = self.request.user)
    
    
    
 ##################################################################
 #####################################################################################
 ###########################################################################################################
 ############ ViewSets + Routers ############################################################################################  
 ###################################################################################################################################################### 
    
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsAdminOrReadOnly

from django.contrib.auth.models import User    

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    
    filterset_fields = ['completed']
    search_fields = ['title']
    ordering_fields = ['title', 'id']
    
    def get_queryset(self):
        return Todo.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    
    
    
    
## Signup API or User Registration API
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if User.objects.filter(username = username).exists():
        return Response({"error": "User already exists"}, status = 400)
    
    user = User.objects.create_user(username = username, password = password)
    
    return Response({"message": "User created Successfully", "username": user.username}, status = 201)