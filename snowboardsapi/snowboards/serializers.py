from rest_framework import serializers

from .models import Snowboard


class SnowboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snowboard
        fields = '__all__'
