#write API endpoint URL
#As I am using viewsets instead of views, 
# I can automatically generate the URL conf for REST API,
# by simply registering the viewsets with a router class.
#if you are using individual view then
# you can configure API URL explicitly.

from django.urls import include,path
from rest_framework import routers, urlpatterns
from crudrestapi import views

router=routers.DefaultRouter()
router.register(r'patients',views.PatientcredentialsViewSet)
router.register(r'patientshealthdata',views.PatienthealthdataViewSet)
router.register(r'patientvitals',views.PatientvitalsViewSet)
router.register(r'patientBloodSugarreading',views.PatientbloodsugartrackingViewSet)

urlpatterns=[
    path('',include(router.urls)),
]
