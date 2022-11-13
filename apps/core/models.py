from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField('name', max_length=90)
    email = models.CharField('email', max_length=90)
    function = models.ManyToManyField('function', related_name="functions")
    projects = models.ManyToManyField('project', related_name="projectsMember", blank=True)

class Function(models.Model):
    namefunction = models.CharField('name', max_length=90)

class Requirement(models.Model):
    name = models.CharField('name', max_length=90)
    description = models.CharField('description', max_length=90)
    priority = models.CharField('priority', max_length=90)
    status = models.CharField('status', max_length=90)
    project = models.ForeignKey('project', on_delete=models.CASCADE) 

class Sprint(models.Model):
    dateBegin = models.DateField('dateBegin')
    dateFinished = models.DateField('dateFinished')
    finished = models.BooleanField(default=False)
    project = models.ForeignKey('project', on_delete=models.CASCADE)

class Task(models.Model):
    name = models.CharField('name', max_length=90)
    description = models.CharField('description', max_length=90)
    dateBegin = models.DateField('dateBegin')
    dateFinished = models.DateField('dateFinished')
    member = models.ForeignKey('member', on_delete=models.CASCADE,)
    status = models.ForeignKey('Status', on_delete=models.CASCADE,)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE,)

class Status(models.Model):
    name = models.CharField('name', max_length=90)

class EventType(models.Model):
    name = models.CharField('name', max_length=90)

class Event(models.Model):
    data = models.DateField('data')
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE, blank=True, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)

class Project(models.Model):
    name = models.CharField('name', max_length=90)
    dateBegin = models.DateField('dateBegin')
    dateFinished = models.DateField('dateFinished')
    client = models.CharField('client', max_length=90)
    contactClient = models.CharField('contactClient', max_length=90)

class ProjectAllInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)