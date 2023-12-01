from rest_framework import serializers
from .models import Todo, Profile, CarModel, Car_Listing

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "picture"]

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        field =['id','make','model_name']
        """field =['id','make','model_name','year','fuel_type','transmission']"""

class Car_ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Listing
        field =['id','model_name','price','mileage','year','location','listing_date','link_to_buyer']

