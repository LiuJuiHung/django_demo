from django.db import models

# Create your models here.
class Group_Emotion(models.Model):
    group = models.TextField(blank=True)
    emotion = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Group_Emotion"

class test(models.Model):
    group = models.TextField(blank=True)
    emotion = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "test"