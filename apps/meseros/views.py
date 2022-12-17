from django.shortcuts import render

# Serializador

from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.meseros.forms import MeserosForm
from apps.meseros.models import Meseros
from apps.meseros.serializers import MeserosSerializer


def meseros_list(request):


    meseross = Meseros.objects.all()
    # meseross = Meseros.objects.filter( edad__lt=30,nacionalidad="Peru")
    # Meseros.objects.filter(edad__gt=0).update(edad=F('edad') + 10)

    return render(request, 'meseros/meseross_list.html', context={'data': meseross})

"""Vistas basadas en clases"""
"""ListView, CreateView, UpdateView, DeleteView"""

class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros/meseros_vc.html'


class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/meseros-create.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/meseros-update-vc.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeserosDelete(DeleteView):
    model = Meseros
    success_url = reverse_lazy('meseros_list')
    template_name = 'meseros/meseros-confirm-delete.html'

# """Serializers"""
# def ListMeserosSerializer(request):
#     lista = ssr.serialize('json', Meseros.objects.all(), fields=['nombre', 'edad'])
#     return HttpResponse(lista, content_type="application/json")


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def meseros_api_view(request):

    if request.method == 'GET':
        queryset = Meseros.objects.all()  # Se obtiene todos los datos de la tabla owner
        serializers_class = MeserosSerializer(queryset, many=True)
        # return Response(serializers_class.data)
        return Response(serializers_class.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MeserosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # return Response(serializer.data)
        # return Response(serializer.errors)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def meseros_detail_view(request, pk):
    meseros = Meseros.objects.filter(id=pk).first()

    if meseros:
        if request.method == 'GET':
            serializers_class = MeserosSerializer(meseros)
            return Response(serializers_class.data)

        elif request.method == 'PUT':
            # pass
            serializers_class = MeserosSerializer(meseros, data=request.data)

            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            # pass
            meseros.delete()
            return Response('Owner se ha eliminado correctamente', status=status.HTTP_201_CREATED)
            return Response({'message': 'No se ha encontrado ningún owner con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
