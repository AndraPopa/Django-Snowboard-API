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

            height = request.POST.get('height'),
            skills = request.POST.get('skills'),

            return redirect(f'/your-next-snowboard/?gender={gender}&skills={skills}')


class YourNextSnowboardView(ListView):
    template_name = 'snowboard_list.html'
    serializer_class = SnowboardSerializer
    queryset = Snowboard.objects.all()

    def get(self, request, *arg, **kwargs):
        gender = request.GET.get('gender')
        skills = request.GET.get('skills')
        queryset = Snowboard.objects.all()
        filter = process_queryset(gender, skills)
        queryset = queryset.filter(gender=filter['gender'], level=filter['level'])
        return render(request, self.template_name, {'gender': gender, 'snowboards': queryset})


def process_queryset(gender, skills):
    filter_dict = {'gender': 'Female' if gender == 'girl' else 'Male',
                   'level': 'Beginner' if 'rookie' in skills else 'Intermediate-Advanced'}
    return filter_dict
