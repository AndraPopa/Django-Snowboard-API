from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/snowboards', views.SnowboardView)

urlpatterns = [
    path('', include(router.urls)),
    path('hello-rider/', views.ChooseSnowboardView.as_view()),
    path('girls-who-ride/', views.GirlsBoardsView.as_view()),
    path('boys-who-ride/', views.BoysBoardsView.as_view())
]
