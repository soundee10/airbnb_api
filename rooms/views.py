from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer
from .models import Room 

@api_view(["GET"])
def list_rooms(request):
    rooms = Room.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)
