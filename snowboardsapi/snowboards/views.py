from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer


class SnowboardView(viewsets.ModelViewSet):
    queryset = Snowboard.objects.all()
    serializer_class = SnowboardSerializer


class RiderInfoView(TemplateView):
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
            height = request.POST.get('height')
            return redirect(
                f'/your-next-snowboard/'
                f'?rider_name={rider_name}'
                f'&gender={gender}'
                f'&skills={skills}'
                f'&style={style}'
                f'&height={height}'
            )


class YourNextSnowboardView(ListView):
    template_name = 'snowboard_list.html'
    serializer_class = SnowboardSerializer
    queryset = Snowboard.objects.all()

    def get(self, request, *arg, **kwargs):
        gender = request.GET.get('gender')
        skills = request.GET.get('skills')
        style = request.GET.get('style')
        height = request.GET.get('height')
        rider_name = request.GET.get('rider_name').split("'")[1].split("'")[0]
        filter = process_queryset(gender, skills, style)
        size_range = None
        if height:
            size_range = process_size_range(int(height), style)
        queryset = Snowboard.objects.filter(
            gender__in=[filter['gender'], 'Unisex'],
            style=filter['style'],
            level=filter['level'],
        )
        return render(request,
                      self.template_name,
                      {'gender': gender, 'snowboards': queryset, 'rider_name': rider_name, 'size_range': size_range})


freeride_size_chart = {
    'lt_160': '145-151',
    'gt_160_lt_170': '151-155',
    'gt_170_lt_180': '155-158',
    'gt_180': '158-160'
}

park_size_chart = {
    'lt_160': '140-145',
    'gt_160_lt_170': '145-149',
    'gt_170_lt_180': '149-153',
    'gt_180': '153-156'
}


def process_size_range(height, style):
    size_range = None
    if height < 160:
        size_range = park_size_chart['lt_160'] if style == 'park' else freeride_size_chart['lt_160']
    elif 160 <= height < 170:
        size_range = park_size_chart['gt_160_lt_170'] if style == 'park' else freeride_size_chart['gt_160_lt_170']
    elif 170 <= height < 180:
        size_range = park_size_chart['gt_170_lt_180'] if style == 'park' else freeride_size_chart['gt_170_lt_180']
    elif height > 180:
        size_range = park_size_chart['gt_180'] if style == 'park' else freeride_size_chart['gt_180']
    return size_range


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
