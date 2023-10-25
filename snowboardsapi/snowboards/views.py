from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Snowboard
from .serializers import SnowboardSerializer
from .process_snowboards import process_queryset, process_size_range


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

