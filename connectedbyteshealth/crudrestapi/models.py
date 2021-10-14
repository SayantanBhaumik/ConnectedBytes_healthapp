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
    first_name=models.CharField(max_length=30,blank=False,default='')
    last_name=models.CharField(max_length=30,blank=False,default='')
    email=models.EmailField(max_length=100,blank=False,default='')
    phonenumber=models.CharField(max_length=15,blank=False)
    accountcreationtimestamp=models.DateTimeField(default=datetime.datetime.now)
    username=models.CharField(max_length=20,blank=False)
    MALE='M'
    FEMALE='F'
    OTHERS='O'
    gender=[(MALE,'Male'),(FEMALE,'Female'),(OTHERS,'Others')]
    sex=models.CharField(max_length=2,choices=gender,default='Male')
    dob=models.DateField(auto_now=False, auto_now_add=False,default=datetime.date.today)
    height=models.FloatField(null=False, blank=False, default=None)
    weight=models.FloatField(null=False, blank=False, default=None)
    bloodgroup=models.CharField(max_length=10,default='A+')
    maritalstatus=models.CharField(max_length=10,default='Married')
    emergencycontact=models.CharField(max_length=15,default='')
    city=models.CharField(max_length=15,default='Kolkata')
    state=models.CharField(max_length=15,default='WestBengal')
    pincode=models.CharField(max_length=15,default='700000')
    country=models.CharField(max_length=15,default='India')
    
    #specified the table name under class Meta.
    class Meta:
        db_table='patients'
    #because object representations are used throughout Django application
    # convert Python objects into strings
    def __str__(self):
        return self
    
    
class Secondarydata(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    profession=models.CharField(max_length=30,blank=False,default='')
    smoking=models.CharField(max_length=30,blank=False,default='')
    drinking=models.CharField(max_length=30,blank=False,default='')
    regularphysicalactivity=models.CharField(max_length=30,blank=False,default='')
    diet=models.CharField(max_length=30,blank=False,default='')
    allergy=models.CharField(max_length=30,blank=False,default='')
    chronicillness=models.CharField(max_length=30,blank=False,default='')
    majorinjury=models.CharField(max_length=30,blank=False,default='')
    majorsurgery=models.CharField(max_length=30,blank=False,default='')
    regularphysicalactivity=models.CharField(max_length=30,blank=False,default='')
    eyepower=models.CharField(max_length=30,blank=False,default='')
    temperature=models.FloatField(null=False, blank=False, default=None)
        
        
    class Meta:
         db_table='patientshealthdata'
        
    def __str__(self):
        return self
    
class Patientsvitals(models.Model):
    vitalsdatetime=models.DateTimeField(default=datetime.datetime.now)
    systolic=models.IntegerField(null=False,blank=False,default=0)
    diastolic=models.IntegerField(null=False,blank=False,default=0)
    temperature=models.FloatField(null=False, blank=False, default=None)
    pulse=models.IntegerField(null=False,blank=False,default=0)
        
    class Meta:
        db_table='patientvitals'
    
    def __str__(self):
        return self

class Patientbloodsugartracking(models.Model):
    bloodsugarreadingdatetime=models.DateTimeField(default=datetime.datetime.now)
    bloodsugarreading=models.IntegerField(null=False,blank=False,default=0)
   
    class Meta:
       db_table='patientBloodSugarreading'
    
    def __str__(self):
        return self
    