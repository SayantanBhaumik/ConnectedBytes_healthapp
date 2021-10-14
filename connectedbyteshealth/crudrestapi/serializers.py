#Serializers allow complex data such as querysets and model instances 
# to be converted to native Python datatypes 
# that can then be easily rendered into JSON, XML or other content types. 
# Serializers also provide deserialization, 
# allowing parsed data to be converted back into complex types, 
# after first validating the incoming data.

from rest_framework import fields, serializers
from connectedbyteshealth.crudrestapi.models import Secondarydata
from crudrestapi.models import Patientcredentials,Secondarydata,Patientsvitals,Patientbloodsugartracking

#The ModelSerializer class provides a shortcut 
# that lets you automatically create a Serializer class 
# with fields that correspond to the Model fields.

class PatientcredentialsSerializer(serializers.ModelSerializer):
# #In the inner class Meta, we declare attributes
    class Meta:
        model=Patientcredentials
        fields=['id',
                'first_name',
                'last_name',
                'email',
                'phonenumber',
                'accountcreationtime',
                'username',
                
        ]
#making the id field optional because when you want to insert new user 
# you might not want to put value for id field in your request object.
        extra_kwargs={'id':{'required':False}}

class SecondarydataSerializer(serializers.ModelSerializer):
        
        class Meta:
                model=Secondarydata
        #all the Secondarydata model fields on the class will be mapped to serializer fields
        
                fields=['id',
                        'profession',
                        'smoking',
                        'drinking',
                        'regularphysicalactivity',
                        'diet',
                        'allergy',
                        'chronicillness',
                        'majorinjury',
                        'majorsurgery',
                        'regularphysicalactivity',
                        'eyepower',
                        ' temperature']
                #exclude=[]
                #read_only_fields=[]
                
        def create(self,validated_data):
                secondarydata=Secondarydata(
                        profession=validated_data['profession'],
                        eyepower=validated_data['eyepower']
                        
                )
                secondarydata.save()
                return secondarydata
                       
                
class PatientsvitalsSerializer(serializers.ModelSerializer):
        
        class Meta:
                model=Patientsvitals
                fields='__all__'

class PatientbloodsugartrackingSerializer(serializers.ModelSerializer):
        
        class Meta:
                model=Patientbloodsugartracking
                fields='__all__'
        









    


    