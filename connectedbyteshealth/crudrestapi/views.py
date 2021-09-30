#Here going to use ViewSets which will allow  to write multiple views together

from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets,status
from django.http import Http404
from rest_framework.utils import serializer_helpers
from crudrestapi.serializers import PatientcredentialsSerializer
from crudrestapi.models import Patientcredentials
from rest_framework import response


class PatientcredentialsViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed/created/edited/deleted.
    """
    queryset=Patientcredentials.objects.all().order_by('id')
    serializer_class=PatientcredentialsSerializer
    update_data_pk_field='id'
    
#defined create() function to either create or update record. 
# have also defined destroy() function to delete the existing record.
    
    def create(self,request,*args,**kwargs):
        kwarg_field:str=self.lookup_url_kwarg or self.lookup_field
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
        return response(status=status.HTTP_204_NO_CONTENT)
        