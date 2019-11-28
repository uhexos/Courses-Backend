from django.db import models
from datetime import date
# Create your models here.


class Course (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField(default=date.today)
    owner = models.ForeignKey('auth.User', related_name='courses', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200, null=True)
    thumbnail_url = models.CharField(max_length=200, null=True)
    description = models.TextField()
    position = models.IntegerField()
    course = models.ForeignKey(Course, related_name='lessons',on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
