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
            style = request.POST.get('style')
            height = request.POST.get('height'),
            skills = request.POST.get('skills'),

            return redirect(
                f'/your-next-snowboard/?gender={gender}&skills={skills}&style={style}'
            )


class YourNextSnowboardView(ListView):
    template_name = 'snowboard_list.html'
    serializer_class = SnowboardSerializer
    queryset = Snowboard.objects.all()

    def get(self, request, *arg, **kwargs):
        gender = request.GET.get('gender')
        skills = request.GET.get('skills')
        style = request.GET.get('style')
        filter = process_queryset(gender, skills, style)
        queryset = Snowboard.objects.filter(
            gender=filter['gender'],
            level=filter['level'],
            style=filter['style'],
        ) & Snowboard.objects.filter(
            gender='Unisex',
            level=filter['level'],
            style=filter['style'],
        )
        return render(request, self.template_name, {'gender': gender, 'snowboards': queryset})


def process_queryset(gender, skills, style):
    filter_dict = {'gender': 'Female' if gender == 'girl' else 'Male',
                   'level': 'Beginner' if 'rookie' in skills else 'Intermediate-Advanced'}
    if style == 'freestyle':
        filter_dict['style'] = 'Park'
    elif style == 'freeride':
        filter_dict['style'] = 'Free Ride'
    else:
        filter_dict['style'] = 'All Mountain'
    return filter_dict
