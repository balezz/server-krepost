from rest_framework import serializers
from demo.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['created', 'title', 'detail', 'image']
