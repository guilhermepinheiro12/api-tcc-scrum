from rest_framework import serializers
from .models import Member, Function, Sprint, Event, EventType, Task, Requirement, Project, Status

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = "__all__"

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"