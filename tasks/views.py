from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializer import TaskSerializer


class CreateTaskAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer


class ListTasksAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class UpdateTaskAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_tasks_by_owner_id(request, owner_id):
    tasks = Task.objects.filter(owner_id=owner_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_tasks_by_creator_id(request, creator_id):
    tasks = Task.objects.filter(owner_id=creator_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
