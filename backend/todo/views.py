from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .serializers import TodoSerializer, ProfileSerializer
from .models import Todo, Profile

from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 
    parser_classes= (MultiPartParser,FormParser)

    def create(self, request, *args, **kwargs):
        name = request.data["name"]
        bio = request.data["bio"]
        picture = request.data["picture"]

        Profile.objects.create(name=name, bio=bio, picture=picture)

        return Response("Profile created successfully", status=status.HTTP_200_OK)