from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status,filters
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .pagination import TaskPagination
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend



def say_view(request):

    msg = request.GET.get('msg','')
    return HttpResponse(f'what u said is :{msg}')

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

#整合版endpoint
class TaskListCreateView(ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = TaskFilter
    search_fields = ['name', 'status']
    ordering_fields = ['deadline', 'priority', 'created_at']
