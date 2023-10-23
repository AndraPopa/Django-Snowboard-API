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
        global gender
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
                gender = boy
            elif girl:
                gender = girl

            return redirect(f'/your-next-snowboard/?gender={gender}')


class YourNextSnowboardView(TemplateView):
    template_name = 'snowboard_list.html'

    def get(self, request, *arg, **kwargs):
        gender = request.GET.get('gender')
        return render(request, self.template_name, {'gender': gender})
