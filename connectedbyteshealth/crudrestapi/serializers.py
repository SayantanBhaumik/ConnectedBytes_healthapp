#Serializers allow complex data such as querysets and model instances 
# to be converted to native Python datatypes 
# that can then be easily rendered into JSON, XML or other content types. 
# Serializers also provide deserialization, 
# allowing parsed data to be converted back into complex types, 
# after first validating the incoming data.

from rest_framework import fields, serializers
from connectedbyteshealth.crudrestapi.models import Patienthealthdata
from crudrestapi.models import Patientcredentials,Patienthealthdata,Patientsvitals,Patientbloodsugartracking

#The ModelSerializer class provides a shortcut 
# that lets you automatically create a Serializer class 
# with fields that correspond to the Model fields.

class PatientcredentialsSerializer(serializers.ModelSerializer):
# #In the inner class Meta, we declare attributes
    class Meta:
        model=Patientcredentials
        fields=['id',
                'patient_first_name',
                'patient_last_name',
                'patient_email',
                'patient_phonenumber',
                'patient_accountcreationtime',
                'patient_username',
                
        ]
#making the id field optional because when you want to insert new user 
# you might not want to put value for id field in your request object.
        extra_kwargs={'id':{'required':False}}

class PatienthealthdataSerializer(serializers.ModelSerializer):
        
        class Meta:
                model=Patienthealthdata
                fields=[]
                
class PatientsvitalsSerializer(serializers.ModelSerializer):
        
        class Meta:
                model=Patientsvitals
                fields=[]

class PatientbloodsugartrackingSerializer(serializers.ModelSerializer):
        
        class Meta:
                model=Patientbloodsugartracking
                fields=[]
        









    


    