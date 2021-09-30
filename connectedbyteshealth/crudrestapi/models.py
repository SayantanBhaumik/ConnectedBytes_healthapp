from django.db import models

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
    patient_accountcreationtime=models.DateTimeField()
    patient_username=models.CharField(max_length=20,blank=False)
    
    #specified the table name under class Meta.
    class Meta:
        db_table='patients'
    #because object representations are used throughout Django application
    # convert Python objects into strings
    def __str__(self):
        return self
    
