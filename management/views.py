from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Client, Project
from .serializers import ClientSerializer, ClientListSerializer, ProjectSerializer, ClientDetailSerializer
from django.contrib.auth.models import User
from django.utils import timezone


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    #serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        if self.action in [
            'create',
            'update',
            'partial_update'
        ]:
            return ClientSerializer
        return ClientDetailSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
        instance = serializer.save(updated_at=timezone.now())
        return instance

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated],
        authentication_classes=[TokenAuthentication]
    )
    def projects(self, request, pk=None):
        client = self.get_object()
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(
                client=client,
                created_by=request.user
            )
            users = request.data.get('users', [])
            for user_data in users:
                user = User.objects.get(id=user_data['id'])
                project.users.add(user)
            project.save()
            response_serializer = ProjectSerializer(project)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]





 