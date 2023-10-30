from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer, ProfileSerializer
from .models import Todo, Profile
from rest_framework.parsers import MultiPartParser, FormParser
from google.cloud import vision
from google.cloud.vision_v1 import types
import os, io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'deep-span-402803-1e142b189014.json'

# Create your views here.

def object_detection(picture):
    client = vision.ImageAnnotatorClient()
    content = picture.read()    
    image = types.Image(content=content)
    response = client.object_localization(image=image)
    labels = response.localized_object_annotations
    set_of_object_detected = {}
    for annotation in labels:
        name = annotation.name
        score = annotation.score
        set_of_object_detected[name] = score
    name_of_max_score = max(zip(set_of_object_detected.values(), set_of_object_detected.keys()))[1]
    return name_of_max_score

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
        result = object_detection(picture)

        Profile.objects.create(name=name, bio=bio, picture=picture)

        return Response(f"Profile created successfully, this is a {result}", status=status.HTTP_200_OK)