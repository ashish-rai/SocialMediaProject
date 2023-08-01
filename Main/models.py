import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank='true')
    profile_pic = models.ImageField(upload_to='profle', default='default.png')
    locations = models.CharField(max_length=100, blank='true')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=0)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    allow_comments = models.BooleanField(default=True) 

    def __str__(self):
        return self.caption
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.created_date}"
    

