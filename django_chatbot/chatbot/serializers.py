from rest_framework import serializers 
from chatbot.models import Estudiante, Tarea

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'apellido', 'codigo', 'primerParcial', 'segundoParcial', 'TercerParcial', 'faltas')

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('nombre', 'descripcion', 'nota', 'estudiante', 'entregado', 'fecha')