from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerLogin(models.Model):
    #create relationship (dont inherit from User)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #add any additional attributes you want
    address = models.CharField(max_length=15, default='')


    def __str__(self):
        return self.user.username
