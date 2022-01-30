from __future__ import unicode_literals
from django.template.defaulttags import register

from django.db import models

# Create your models here.

class MP(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    education = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Constituency(models.Model):
    name = models.CharField(max_length=30)
    mp = models.ForeignKey(MP, on_delete=models.CASCADE)
    area = models.CharField(max_length=20)
    population = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

        
    class Meta:
        verbose_name_plural = "Constituencies"
        
        
class Work(models.Model):
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    brief = models.CharField(max_length=50)
    detail = models.CharField(max_length=250)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.brief
    
    class Meta:
        verbose_name_plural = "Work List"

class Feedback(models.Model):
    against = models.CharField(max_length=50)
    against_id = models.IntegerField()
    detail = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.against
    
    class Meta:
        verbose_name_plural = "Feedback"
    