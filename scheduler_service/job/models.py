from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=200,null=False)
    job_description = models.CharField(max_length=200, null=True,blank=True)
    schedule = models.CharField(max_length=200)
    last_run = models.DateTimeField(null=True,blank=True)
    next_run = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.job_name
    