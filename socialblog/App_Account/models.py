from django.db import models

# Create your models here.

from django.contrib.auth.models import User 

class Profile(models.Model):
    user=models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    image=models.ImageField( upload_to='profile_picture/',default="avater.png",blank=True,null=True )
    
    def __str__(self) -> str:
        return str(self.user.username)