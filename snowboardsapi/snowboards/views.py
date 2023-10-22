from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer
from django.forms import modelform_factory
from extra_views import ModelFormSetView


class SnowboardView(viewsets.ModelViewSet):
    queryset = Snowboard.objects.all()
    serializer_class = SnowboardSerializer


SnowboardForm = modelform_factory(Snowboard, exclude=[])


class ChooseSnowboardView(ModelFormSetView):
    model = Snowboard
    template_name = 'snow_form.html'
    fields = ['model_name', 'style', 'type', 'price_euro']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Little Corgi Rider'
        return context
