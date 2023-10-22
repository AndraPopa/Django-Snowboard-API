from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer
from django.forms import modelform_factory
from django.shortcuts import render
from django.views.generic import TemplateView


class SnowboardView(viewsets.ModelViewSet):
    queryset = Snowboard.objects.all()
    serializer_class = SnowboardSerializer


SnowboardForm = modelform_factory(Snowboard, exclude=[])


class ChooseSnowboardView(TemplateView):
    template_name = 'choose_snowboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Little Corgi Rider'
        return context

