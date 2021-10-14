#Here going to use ViewSets which will allow  to write multiple views together

#rom django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets
from rest_framework import status
from django.http import Http404
from rest_framework.utils import serializer_helpers
from crudrestapi.serializers import PatientcredentialsSerializer,PatientbloodsugartrackingSerializer,SecondarydataSerializer,PatientsvitalsSerializer
from crudrestapi.models import Patientcredentials,Patientbloodsugartracking,Secondarydata,Patientsvitals
from rest_framework.response import Response


class PatientcredentialsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed/created/edited/deleted.
    """
    queryset=Patientcredentials.objects.all().order_by('id')
    serializer_class=PatientcredentialsSerializer
    update_data_pk_field='id'
    
#defined create() function to either create or update record. 
# have also defined destroy() function to delete the existing record.
    
    def create(self,request,*args,**kwargs):
        kwarg_field: str=self.lookup_url_kwarg or self.lookup_field
        self.kwargs[kwarg_field] = request.data[self.update_data_pk_field]
        
        try:
            return self.update(request, *args, **kwargs)
        except Http404:
            return super().create(request, *args, **kwargs)
    
    def destroy(self,request,*args,**kwargs):
        try:
            instance=self.get_object()
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SecondarydataViewSet(viewsets.ModelViewSet):
    """
    patient's secondarydata ViewSet for listing or retrieving patient secondarydata.
    """
    #permission_classes = [IsAccountAdminOrReadOnly]
    #patient_secondarydata_list
    
    def list(self,req):
        queryset=Secondarydata.objects.all()
        serializer=SecondarydataSerializer(queryset,many=True)
        return Response(serializer.data)
       
    #individual_secondarydata_detail
    
    def retrieve(self,req,pk=None):
        queryset=Secondarydata.objects.all()
        patientsecondarydata=get_object_or_404(queryset,pk=pk)
        serializer=SecondarydataSerializer(patientsecondarydata)
        return Response(serializer.data)
    
    def create(self,req,*args,**kwargs):
        serializer=self.get_serializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)
    
    
    """
     main reason behind this is to allow customizeability when calling the save function. 
     You might want to supply extra data before calling save (like serializer.save(owner=self.request.user) 
     and if we didn't have perform_create(self, serializer), 
     you would have to override the create(self, request, *args, **kwargs)
     and that just defeats the purpose of having mixins doing the heavy and boring work.
    """
    
    # will save our object into the database
    
    def perform_create(self,serializer):
        serializer.save()
        
        
    
    
    
    
class PatientsvitalsViewSet(viewsets.ViewSet):
    

class PatientbloodsugartrackingViewSet(viewsets.ViewSet):
        