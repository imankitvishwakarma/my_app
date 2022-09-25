from django.db import models
class skills(models.Model):
    skill_logo=models.ImageField(upload_to='img/',blank=True, height_field=None, width_field=None, max_length=100)
    skill_heading=models.CharField(max_length=30)
    skill_detail=models.TextField()
    skill_perce=models.CharField(max_length=30)

class projects(models.Model):
    project_img=models.ImageField(upload_to='img/',blank=True, height_field=None, width_field=None, max_length=100)
    project_p=models.TextField()
    project_btn=models.CharField(max_length=30)

class aboutme(models.Model):
    about_img=models.ImageField(upload_to='img/',blank=True)
    about_resume=models.FileField(upload_to='resume/', max_length = 100)
    
    
# Create your models here.
