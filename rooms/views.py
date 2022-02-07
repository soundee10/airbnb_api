from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import RoomSerializer, BigRoomSerialzer
from .models import Room 

class ListRoomsView(ListAPIView):
    
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(ListAPIView):
    
    queryset = Room.objects.all()
    serializer_class = BigRoomSerialzer

