from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('api/snowboards', views.SnowboardView)

urlpatterns = [
    path('', include(router.urls)),
    path('hello-rider/', views.RiderInfoView.as_view()),
    path('your-next-snowboard/', views.YourNextSnowboardView.as_view()),
]
