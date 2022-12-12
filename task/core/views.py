from rest_framework import viewsets, mixins
from core.models import Task
from core.serializers import TaskSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
#git remote set-url origin https://DanLivassan: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@github.com/DanLivassan/devlane_test.git
