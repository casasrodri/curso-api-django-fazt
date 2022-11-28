from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets, permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] # Pero puede ser: permissions.IsAuthenticated u otro.
    serializer_class = ProjectSerializer
