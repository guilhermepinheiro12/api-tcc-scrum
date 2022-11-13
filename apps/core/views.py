from django.http import JsonResponse
from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.decorators import action, api_view
from .serializers import MemberSerializer, FunctionSerializer, SprintSerializer, EventSerializer, EventTypeSerializer, TaskSerializer, RequirementSerializer, ProjectSerializer, StatusSerializer
from .models import Member, Function, Sprint, Event, EventType, Task, Requirement, Project, Status

# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    @action(detail=False, methods=['get']) 
    def getMembers(self, request):
        member = Member.objects.all()
        response = MemberSerializer(member, many=True)
        return Response({
                        'success' : True,
                        'member' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getMember(self, request, pk):
        member = Member.objects.filter(id=pk)
        response = MemberSerializer(member, many=True)
        return Response({
                        'success' : True,
                        'member' : response.data})

    @action(detail=False, methods=['get']) 
    def onlyDevs(self, request):
        devs = Member.objects.filter(function=1)
        response = MemberSerializer(devs, many=True)
        return Response({
            'success' : True,
            'devs': response.data})

class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    
    @action(detail=False, methods=['get']) 
    def getFunctions(self, request):
        function = Function.objects.all()
        response = FunctionSerializer(function, many=True)
        return Response({
                        'success' : True,
                        'function' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getFunction(self, request, pk):
        function = Function.objects.filter(id=pk)
        response = FunctionSerializer(function, many=True)
        return Response({
                        'success' : True,
                        'function' : response.data})

class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    
    @action(detail=False, methods=['get']) 
    def getSprints(self, request):
        sprint = Sprint.objects.all()
        response = SprintSerializer(sprint, many=True)
        return Response({
                        'success' : True,
                        'sprint' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getSprint(self, request, pk):
        sprint = Sprint.objects.filter(id=pk)
        response = SprintSerializer(sprint, many=True)
        return Response({
                        'success' : True,
                        'sprint' : response.data})

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    @action(detail=False, methods=['get']) 
    def getEvents(self, request):
        event = Event.objects.all()
        response = EventSerializer(event, many=True)
        return Response({
                        'success' : True,
                        'event' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getEvent(self, request, pk):
        event = Event.objects.filter(id=pk)
        response = EventSerializer(event, many=True)
        return Response({
                        'success' : True,
                        'event' : response.data})

class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    
    @action(detail=False, methods=['get']) 
    def getEventTypes(self, request):
        eventtype = EventType.objects.all()
        response = EventTypeSerializer(eventtype, many=True)
        return Response({
                        'success' : True,
                        'eventType' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getEventType(self, request, pk):
        eventtype = EventType.objects.filter(id=pk)
        response = EventTypeSerializer(eventtype, many=True)
        return Response({
                        'success' : True,
                        'eventType' : response.data})

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    @action(detail=False, methods=['get']) 
    def getAllStatus(self, request):
        status = Status.objects.all()
        response = StatusSerializer(status, many=True)
        return Response({
                        'success' : True,
                        'status' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getStatus(self, request, pk):
        status = Status.objects.filter(id=pk)
        response = StatusSerializer(status, many=True)
        return Response({
                        'success' : True,
                        'status' : response.data})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=False, methods=['get']) 
    def getTasks(self, request):
        task = Task.objects.all()
        response = TaskSerializer(task, many=True)
        return Response({
                        'success' : True,
                        'task' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getTask(self, request, pk):
        task = Task.objects.filter(id=pk)
        response = TaskSerializer(task, many=True)
        return Response({
                        'success' : True,
                        'task' : response.data})

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    
    @action(detail=False, methods=['get']) 
    def getRequirements(self, request):
        requirement = Requirement.objects.all()
        response = RequirementSerializer(requirement, many=True)
        return Response({
                        'success' : True,
                        'requirement' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getRequirement(self, request, pk):
        requirement = Requirement.objects.filter(id=pk)
        response = RequirementSerializer(requirement, many=True)
        return Response({
                        'success' : True,
                        'requirement' : response.data})

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @action(detail=False, methods=['get']) 
    def getProjects(self, request):
        projects = Project.objects.all()
        response = ProjectSerializer(projects, many=True)
        return Response({
                        'success' : True,
                        'project' : response.data})
    
    @action(detail=True, methods=['get']) 
    def getProject(self, request, pk):
        project = Project.objects.filter(id=pk)
        response = ProjectSerializer(project, many=True)
        return Response({
                        'success' : True,
                        'project' : response.data})


    @action(detail=True, methods=['get']) 
    def allInfo(self, request, pk):

        project = Project.objects.get(id=pk)
        projectInfo = ProjectSerializer(project)
        sprints = Sprint.objects.filter(project=pk)
        sprintsInfo = SprintSerializer(sprints, many=True)
        AllsprintsInfo = []
        for sprint in sprints:
            tasks = Task.objects.filter(sprint = sprint.id)
            tasksInfo = TaskSerializer(tasks, many=True)
            sprintJson = {'id' : sprint.id,
                            'from' : sprint.dateBegin,
                            'to' : sprint.dateFinished,
                            'finished' : sprint.finished,
                            'project' : sprint.project,
                            'tasks': tasksInfo.data}
            AllsprintsInfo.append(sprintJson)

        projectJson = {
                            'id' : project.id,
                            'name' : project.name,
                            'from' : project.dateBegin,
                            'to' : project.dateFinished,
                            'sprints': str(AllsprintsInfo),
                            'clientName' : project.client,
                            'clientContact' : project.contactClient,
                        }
        
        return Response({
                        'success' : True,
                        'project' : projectJson})
