from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Task
from api.v1.tasks.serializers import TaskSerializer

@api_view(["GET"])
def tasks(request):
    instances = Task.objects.filter(is_deleted=False)
    serializer = TaskSerializer(instances, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_task(request):
    pass
