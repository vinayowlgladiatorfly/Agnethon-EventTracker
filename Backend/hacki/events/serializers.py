from rest_framework import serializers 
from . models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model:Event
        fields="__all__"                