from rest_framework import viewsets
from .models import Room
from .serializers import TinyUserSerialzer, BigRoomSerialzer

class RoomViewset(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer = BigRoomSerialzer