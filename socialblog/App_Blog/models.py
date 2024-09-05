from django.db import models
from django.contrib.auth.models import User 
from App_Account.models import Profile
# Create your models here.

from django.db.models import CharField, DateField, ForeignKey, Model
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Blog(models.Model):
    Blog_Category=(
        ("Lifestyle & Personal Development","Lifestyle & Personal Development"),
        ("Tech & Innovation","Tech & Innovation"),
        ("Career & Professional Growth","Career & Professional Growth"),
        ("Finance & Business","Finance & Business"),
        ("Travel & Adventure","Travel & Adventure"),
        ("Health & Fitness","Health & Fitness"),
        ("Food & Cooking","Food & Cooking"),
        ("Arts & Creativity","Arts & Creativity"),
       
        ("Education & Learning","Education & Learning"),
        ("Parenting & Family","Parenting & Family"),
       
        
    )
    author=models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title=models.TextField(max_length=150)
    category=models.CharField(max_length=100, choices=Blog_Category)
    slug = AutoSlugField(populate_from='title')
    content=models.TextField(blank=True,null=True)
    image=models.ImageField( upload_to='post_picture/',blank=True,null=True )
    date=models.DateTimeField( auto_now_add=True)
    update=models.DateTimeField( auto_now=True)
    
    def __str__(self) -> str:
        return str(self.author) + self.title + str(self.date)
    
    
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self) :
        return  str(self.comment) 
    
class Like(models.Model):
    blog=models.ForeignKey(Blog, related_name='liked_blog', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='liker_user', on_delete=models.CASCADE)
    
    
    
    
    
