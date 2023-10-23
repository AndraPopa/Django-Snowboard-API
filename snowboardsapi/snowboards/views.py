from django.views.generic import TemplateView, ListView
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

            gender = request.POST.get('gender')

            attributes_dict = {
                'height': request.POST.get('height'),
                'skills': request.POST.get('skills'),
            }

            return redirect(f'/your-next-snowboard/?gender={gender}')


class YourNextSnowboardView(ListView):
    template_name = 'snowboard_list.html'
    serializer_class = SnowboardSerializer
    queryset = Snowboard.objects.all()

    def get(self, request, *arg, **kwargs):
        gender = request.GET.get('gender')
        queryset = Snowboard.objects.all()
        if gender == 'girl':
            queryset = queryset.filter(gender='Female')
        elif gender == 'boy':
            queryset = queryset.filter(gender='Male')
        return render(request, self.template_name, {'gender': gender, 'snowboards': queryset})
