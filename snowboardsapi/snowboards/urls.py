from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/snowboards', views.SnowboardView)

urlpatterns = [
    path('', include(router.urls)),
    path('hello-rider/', views.RiderInfoView.as_view()),
    path('your-next-snowboard/', views.YourNextSnowboardView.as_view()),
]
