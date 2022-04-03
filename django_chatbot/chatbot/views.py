from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import json

import time

from chatbot.models import Estudiante

class chatbot:
    chatbot = 'Chatbot no existe'

@api_view(['GET'])
def create(request):
    try: 
        pk = request.GET.get('codigo', None)
        estudiante = Estudiante.objects.get(pk=pk) 
    except Estudiante.DoesNotExist: 
        return JsonResponse({'respuesta': 'Estudiante no registrado'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        chatbot.chatbot = ChatBot("profesor")
        nombre = request.GET.get('nombre', None)
        notaPP = estudiante.primerParcial
        notaSP = estudiante.segundoParcial
        notaTP = estudiante.TercerParcial
        faltas = estudiante.faltas
        conversation = [
            "Hola", f"Hola {nombre}!, ¿Qué tal?",
            "Quiero saber mis notas", f"Claro {nombre}, ¿De qué parcial deseas saber tus notas?",
            "Primer parcial", f"Esta es tu nota del primer parcial: {notaPP}",
            "Segundo parcial", f"Esta es tu nota del segundo parcial: {notaSP}",
            "Tercer parcial", f"Esta es tu nota del tercer parcial: {notaTP}",
            "Nota primer parcial", f"Claro {nombre}, tu nota para el primer parcial es de: {notaPP}",
            "Nota segundo parcial", f"Claro {nombre}, tu nota para el segundo parcial es de: {notaSP}",
            "Nota tercer parcial", f"Claro {nombre}, tu nota para el tercer parcial es de: {notaTP}",
            "Cuanto tengo en mi primer parcial?", f"Hola {nombre}, tu nota para el primer parcial es de: {notaPP}",
            "Cuanto tengo en mi segundo parcial?", f"Hola {nombre}, tu nota para el segundo parcial es de: {notaSP}",
            "Cuanto tengo en mi tercer parcial?", f"Hola {nombre}, tu nota para el tercer parcial es de: {notaTP}",
            "Cuantas faltas tengo?", f"Hola {nombre}, tienes {faltas} faltas. Ten cuidado!",
            "faltas", f"Hola {nombre}, tienes {faltas} faltas. Ten cuidado!",
            "nro de faltas", f"Hola {nombre}, tienes {faltas} faltas. Ten cuidado!",
            "Tareas", f"Hola {nombre}, A continuación te enviaré la información de las tareas:",
            "tareas no entregadas", f"Hola {nombre}, estas son las tareas que no entregaste:"
        ]
        trainer = ListTrainer(chatbot.chatbot)
        trainer.train(conversation)
        data = {
            "respuesta":"Creado correctamente"
        }
        return JsonResponse(data)



@api_view(['GET'])
def chat(request):
    if request.method == 'GET':
        frase = request.GET.get('frase', None)
        if frase is not None:
            response = chatbot.chatbot.get_response(frase)
            print(response.text)
            data = {
                "respuesta": response.text
            }
            return JsonResponse(data)


@api_view(['GET'])
def prueba(request):
    data = {
        "respuesta": "hola"
    }
    return JsonResponse(data)