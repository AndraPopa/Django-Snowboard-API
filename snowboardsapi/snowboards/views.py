from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer


class SnowboardView(viewsets.ModelViewSet):
    queryset = Snowboard.objects.all()
    serializer_class = SnowboardSerializer


class ChooseSnowboardView(TemplateView):
    template_name = 'snow_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Rider!'
        return context
