from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User
from rest_framework import status


## GET and POST
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    ## GET request -> return all todos or row
    if request.method == 'GET':
        todo = Todo.objects.filter(user = request.user)
        serializer = TodoSerializer(todo, many = True)
        return Response(serializer.data)
    
    ## POST request -> Create new todo or new row
    if request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save(user = request.user)       ## Django automatically runs: Todo.objects.create(...)
            return Response({"message": "Data saved successfully", "data": serializer.data},status = 201)
        
        return Response(serializer.errors, status = 400)
    
    
## GET(single object or row), PUT, POST
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo_detail(request, pk):
    todo = Todo.objects.get(id = pk, user = request.user)       ## get_object_or_404(Todo, id=pk, user=request.user)
    
    # GET (get the single row)
    if request.method == 'GET': 
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    # PUT (update the row)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Row updated successfully", "data": serializer.data}, status = 201)
        
        return Response(serializer.errors, status = 400)
    
    # DELETE (delete the row)
    if request.method == 'DELETE':
        deleted_row = todo.delete()
        return Response({"message": "Row deleted", "data": deleted_row}, status = 200)
        
        
        

## Signup API or User Registration API
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if User.objects.filter(username = username).exists():
        return Response({"error": "User already exists"}, status = 400)
    
    user = User.objects.create_user(username = username, password = password)
    
    return Response({"message": "User created Successfully", "username": user.username}, status = 201)
    


    
