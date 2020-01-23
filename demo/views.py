from demo.models import Room
from demo.serializers import RoomSerializer
from rest_framework import generics


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
