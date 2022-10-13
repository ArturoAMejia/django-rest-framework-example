from projects.models import Project
from rest_framework import viewsets, permissions
from projects.serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  # Se permite la consulta de todos los datos de la tabla
  queryset = Project.objects.all()
  # permite cualquier persona que consulte
  permission_classes = [permissions.AllowAny]
  serializer_class = ProjectSerializer

