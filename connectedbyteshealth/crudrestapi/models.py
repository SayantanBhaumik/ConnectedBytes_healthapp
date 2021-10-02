from django.db import models
import datetime


# Create your models here.
class Patientcredentials(models.Model):
    #used AutoField for out primary key instead of IntergerField 
    # otherwise when you will make a POST request to create new user record 
    # and if you are returning the newly created record from server 
    # then you will get null value for id field. 
    # Making it AutoField will give you the exact value for id filed 
    # for the new user record inserted into table
    
    id = models.AutoField(primary_key=True,default=0)
    patient_first_name=models.CharField(max_length=30,blank=False,default='')
    patient_last_name=models.CharField(max_length=30,blank=False,default='')
    patient_email=models.EmailField(max_length=100,blank=False,default='')
    patient_phonenumber=models.CharField(max_length=15,blank=False)
    patient_accountcreationtime=models.DateTimeField(default=datetime.datetime.now)
    patient_username=models.CharField(max_length=20,blank=False)
    MALE='M'
    FEMALE='F'
    OTHERS='O'
    Patient_Sex_Choices=[(MALE,'Male'),(FEMALE,'Female'),(OTHERS,'Others')]
    patient_sex=models.CharField(max_length=2,choices=Patient_Sex_Choices,default='Male')
    patient_dob=models.DateField(auto_now=False, auto_now_add=False,default=datetime.date.today)
    patient_height=models.FloatField(null=False, blank=False, default=None)
    patient_weight=models.FloatField(null=False, blank=False, default=None)
    patient_bloodgroup=models.CharField(max_length=10,default='A+')
    patient_maritalstatus=models.CharField(max_length=10,default='Married')
    patient_emergencycontact=models.CharField(max_length=15,default='')
    patient_city=models.CharField(max_length=15,default='Kolkata')
    patient_state=models.CharField(max_length=15,default='WestBengal')
    patient_pincode=models.CharField(max_length=15,default='700000')
    patient_country=models.CharField(max_length=15,default='India')
    
    #specified the table name under class Meta.
    class Meta:
        db_table='patients'
    #because object representations are used throughout Django application
    # convert Python objects into strings
    def __str__(self):
        return self
    
    
class Patienthealthdata(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    patient_profession=models.CharField(max_length=30,blank=False,default='')
    patient_smoking=models.CharField(max_length=30,blank=False,default='')
    patient_drinking=models.CharField(max_length=30,blank=False,default='')
    patient_regularphysicalactivity=models.CharField(max_length=30,blank=False,default='')
    patient_diet=models.CharField(max_length=30,blank=False,default='')
    patient_allergy=models.CharField(max_length=30,blank=False,default='')
    patient_chronicillness=models.CharField(max_length=30,blank=False,default='')
    patient_majorinjury=models.CharField(max_length=30,blank=False,default='')
    patient_majorsurgery=models.CharField(max_length=30,blank=False,default='')
    patient_regularphysicalactivity=models.CharField(max_length=30,blank=False,default='')
    patient_eyepower=models.CharField(max_length=30,blank=False,default='')
    patient_temperature=models.FloatField(null=False, blank=False, default=None)
        
        
    class Meta:
         db_table='patientshealthdata'
        
    def __str__(self):
        return self
    
class Patientsvitals(models.Model):
    patient_vitalsdatetime=models.DateTimeField(default=datetime.datetime.now)
    patient_systolic=models.IntegerField(null=False,blank=False,default=0)
    patient_diastolic=models.IntegerField(null=False,blank=False,default=0)
    patient_temperature=models.FloatField(null=False, blank=False, default=None)
    patient_pulse=models.IntegerField(null=False,blank=False,default=0)
        
    class Meta:
        db_table='patientvitals'
    
    def __str__(self):
        return self

class Patientbloodsugartracking(models.Model):
    patient_bloodsugarreadingdatetime=models.DateTimeField(default=datetime.datetime.now)
    patient_bloodsugarreading=models.IntegerField(null=False,blank=False,default=0)
   
    class Meta:
       db_table='patientBloodSugarreading'
    
    def __str__(self):
        return self
    