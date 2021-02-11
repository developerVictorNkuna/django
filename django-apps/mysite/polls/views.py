from django.shortcuts import render  # used to render the html,a view is a function that mapps url to UI

from rest_framework import  viewsets

# Create your views here.
from . import models #database model
from . import serializers

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializers_class = serializers.QuestionSerializer