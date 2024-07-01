from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectNestedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='project_name')

    class Meta:
        model = Project
        fields = ['id', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name', read_only=True)
    users = serializers.SerializerMethodField()
    created_by = serializers.ReadOnlyField(source='created_by.username')
    created_at = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = [
            'id',
            'project_name',
            'client',
            'users',
            'created_at',
            'created_by'
        ]

    def get_users(self, obj):
        return [{'id': user.id, 'name': user.username} for user in obj.users.all()]
class ClientSerializer(serializers.ModelSerializer):
    #projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = [
            'id',
            'client_name',
            'created_at',
            'created_by',
            'updated_at'
        ]

class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'client_name',
            'projects',
            'created_at',
            'created_by',
            'updated_at'
        ]

class ClientListSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = [
            'id',
            'client_name',
            'created_by',
            'created_at'
        ]