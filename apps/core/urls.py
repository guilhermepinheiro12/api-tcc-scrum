from django.urls import path, include
from core import views
from rest_framework import routers

app_name = 'core'

router = routers.DefaultRouter()
router.register('member', views.MemberViewSet)
router.register('function', views.FunctionViewSet)
router.register('sprint', views.SprintViewSet)
router.register('event', views.EventViewSet)
router.register('eventtype', views.EventTypeViewSet)
router.register('task', views.TaskViewSet)
router.register('requirement', views.RequirementViewSet)
router.register('project', views.ProjectViewSet, basename='project')
router.register('status', views.StatusViewSet)

urlpatterns = [
        path('', include(router.urls)),
]
