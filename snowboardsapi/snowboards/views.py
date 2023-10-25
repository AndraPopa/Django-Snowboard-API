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
            rider_name = request.POST.get('rider_name'),
            skills = request.POST.get('skills'),

            return redirect(
                f'/your-next-snowboard/?rider_name={rider_name}&gender={gender}&skills={skills}&style={style}'
            )


class YourNextSnowboardView(ListView):
    template_name = 'snowboard_list.html'
    serializer_class = SnowboardSerializer
    queryset = Snowboard.objects.all()

    def get(self, request, *arg, **kwargs):
        gender = request.GET.get('gender')
        skills = request.GET.get('skills')
        style = request.GET.get('style')
        rider_name = request.GET.get('rider_name').split("'")[1].split("'")[0]
        filter = process_queryset(gender, skills, style)
        queryset = Snowboard.objects.filter(
            gender__in=[filter['gender'], 'Unisex'],
            style=filter['style'],
            level=filter['level'],
        )
        return render(request, self.template_name,
                      {'gender': gender, 'snowboards': queryset, 'rider_name': rider_name})


def process_queryset(gender, skills, style):
    filter_dict = {'gender': 'Female' if gender == 'girl' else 'Male',
                   'level': 'Beginner' if 'rookie' in skills else 'Intermediate-Advanced'}
    if style == 'freestyle':
        filter_dict['style'] = 'Park'
    elif style == 'freeride':
        filter_dict['style'] = 'Freeride'
    else:
        filter_dict['style'] = 'All mountain'
    return filter_dict
