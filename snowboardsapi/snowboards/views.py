from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer
from django.forms import modelform_factory
from django.shortcuts import render


class SnowboardView(viewsets.ModelViewSet):
    queryset = Snowboard.objects.all()
    serializer_class = SnowboardSerializer


SnowboardForm = modelform_factory(Snowboard, exclude=[])


def choose_snowboard(request):
    return render(request, 'choose_snowboard.html', {'name': 'Rider'})
