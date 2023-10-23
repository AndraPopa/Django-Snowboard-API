from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer


class SnowboardView(viewsets.ModelViewSet):
    queryset = Snowboard.objects.all()
    serializer_class = SnowboardSerializer


class ChooseSnowboardView(TemplateView):
    template_name = 'snow_form.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {'name': 'Rider!'})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":

            boy = request.POST.get('boy', False)
            girl = request.POST.get('girl', False)

            attributes_dict = {
                'freestyle': request.POST.get('freestyle', False),
                'freeride': request.POST.get('freeride', False),
                'both': request.POST.get('both', False),
                'height': request.POST['height'],
                'skills': request.POST['skills'],
            }

            if boy:
                return redirect('/boys-who-ride/')
            elif girl:
                return redirect('/girls-who-ride/')


class GirlsBoardsView(TemplateView):
    template_name = 'girls_who_ride.html'


class BoysBoardsView(TemplateView):
    template_name = 'boys_who_ride.html'
