from django.db import models

# Create your models here.
class Events(models.Model):
    # event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=50,default='Event Name')
    event_description=models.TextField(null=True)
