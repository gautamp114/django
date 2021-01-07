from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null= True)
    profile_pics = models.ImageField(upload_to = 'profile_pics/')


    def __str__(self):
        return f"{self.user.username} Profile"


    @property
    def imageurl(self):
        try:
            url = self.profile_pics.url
        except :
            url = '/media/profile_pics/default.jpg'
        return url