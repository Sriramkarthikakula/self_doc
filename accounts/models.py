from django.db import models

# Create your models here.

class PatDoc(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode=models.IntegerField()
    phno=models.BigIntegerField()
    def str(self):
        return self.username
    
class Patreg(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode=models.IntegerField()
    phno=models.BigIntegerField()
    dof = models.DateField()
    age = models.IntegerField()
    def str(self):
        return self.username

class patien_dise(models.Model):
    patient_id=models.IntegerField()
    disease=models.CharField(max_length=100)
    specilaist=models.CharField(max_length=100)
    def str(self):
        return self.disease
    
class Notifydatabase(models.Model):
    padid = models.IntegerField()
    
    docid = models.IntegerField()
    pred = models.CharField(max_length=50)
    patname=models.CharField(max_length=30)


class Appoint(models.Model):
    padid = models.IntegerField()
    patname = models.CharField(max_length=50)
    pred = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    unique_id = models.IntegerField()
    booked = models.BooleanField(default=False)
    docid = models.IntegerField()
    doc_name = models.CharField(max_length=50)
    city1=models.CharField(max_length=50)
    hospital_name=models.CharField(max_length=30)
    phno=models.BigIntegerField()
    patphno = models.BigIntegerField()
    hospin = models.IntegerField()


class Treating(models.Model):
    patid = models.IntegerField()
    docid=models.IntegerField()
    treat = models.CharField(max_length=20)
