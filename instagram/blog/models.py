from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, upload_to="post_images/")
    caption = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username}\'s Post"

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except :
            url = 'default.jpg'
        return url
    
    class Meta():
        ordering = ['-date_posted']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username}\'s Comment"


class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name='followed')


    def __str__(self):
        return self.user.username
    

    @classmethod
    def follow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user = user)
        obj.followed.add(another_account)
        print("Followed")
    

    @classmethod
    def unfollow(cls, user, another_account):
        obj,create = cls.objects.get_or_create(user = user)
        obj.followed.remove(another_account)
        print("unfollow")


# class Followerer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     follower = models.ManyToManyField(User, related_name='followed')

#     def __str__(self):
#         return f'{self.user.username}'

    
#     @classmethod
#     def follower(cls,user,another_account):
#         obj