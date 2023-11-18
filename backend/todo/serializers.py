from rest_framework import serializers
from .models import Todo, Profile, CarModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "bio", "picture"]

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        field =['id','make','model_name','year','fuel_type','transmission']

class Car_ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        field =['id','make','model_name','year','fuel_type','transmission']

