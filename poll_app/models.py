from django.db import models
import math

# Create your models here.
class party(models.Model):
    name = models.CharField(max_length =100)
    def __str__(self):
        return self.name
    
class section(models.Model):
    name = models.CharField(max_length =100)
    def __str__(self):
        return self.name

class Vote(models.Model):
    section = models.ForeignKey(section, on_delete=models.SET_NULL, null=True, blank=True)
    npp_votes = models.IntegerField(blank=False, null=False)
    ndc_votes = models.IntegerField(blank=False, null=False)
    mp_npp = models.IntegerField(blank=False, null=False)
    mp_ndc = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.section)
            
