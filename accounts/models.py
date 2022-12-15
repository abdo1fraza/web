from django.db import models
from django.contrib.auth.models import User              # import User from django

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=42)              # radio select
    city = models.CharField(max_length=44,unique=True)    # select
    phone_number = models.CharField(max_length=35)      
    block_call = models.CharField(max_length=10, null=True)         # radio select
    block_sms = models.CharField(max_length=10, null=True)           # radio select
    block_email = models.CharField(max_length=10, null=True)         # radio select

    
    def __str__(self):
        return str(self.user)