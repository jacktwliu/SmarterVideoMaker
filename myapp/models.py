from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

class News(models.Model):
    newsdate = models.DateField(null=False)
    newsname = models.CharField(max_length=20 ,default='')
    newssubject = models.CharField(max_length=250, default='')
    newsperson = models.CharField(max_length=10, default='')
    newsurl = models.CharField(max_length=200, default='')
        
class SendFeedback(models.Model):
    feedbacktype = models.CharField(max_length=10 ,default='')
    detail = models.CharField(max_length=100, default='')
    feedbackemail = models.CharField(max_length=32, default='')
    datetime = models.DateTimeField(auto_now_add=True)

class Messageboard(models.Model):
    msboardname = models.CharField(max_length=50, default='')
    msboardcontent = models.CharField(max_length=100, default='')
    datetime = models.DateTimeField(auto_now_add=True)
    
    

    
'''
class Userinfo(models.Model):
    userid = models.CharField(max_length= 32 ,default='', primary_key=True)
    password = models.CharField(max_length= 32 ,default='')
    username = models.CharField(max_length= 32 ,default='')'''