from rest_framework import serializers
from users.serializers import TinyUserSerialzer
from .models import Room

class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerialzer()

    class Meta:
        model = Room
        fields = ("pk", "name", "price", "instant_book", "user")
    

class BigRoomSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Room
        exclude = ()