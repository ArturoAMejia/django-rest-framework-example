from dataclasses import field, fields
from pyexpat import model
from tokenize import Pointfloat
from rest_framework import serializers
from .models import Project
# decimos que esta basado en un modelo que hemos creado


# Se crea el serializer y se le pasa el modelo que tendrá
class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'title', 'description', 'technology', 'created_at',)
    # Se le pasa que campos del modelo unicamente se pueden leer
    read_only_fields = ('created_at',)