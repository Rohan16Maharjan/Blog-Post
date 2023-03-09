from django.db import models
import uuid
# Create your models here.
class Home(models.Model):
  image = models.ImageField(default='default.jpg')
  title = models.CharField(max_length=100)
  writer = models.CharField(max_length=100)
  describes =models.TextField(max_length=50000)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
  
  def __str__(self):
    return self.title

class About(models.Model):
  team_image = models.ImageField(default='default.jpg')
  team_name = models.CharField(max_length=200,null=True,blank=True)
  team_position  = models.CharField(max_length=100,null=True,blank=True)
  team_phone = models.CharField(max_length=50,null=True,blank=True)
  team_email = models.CharField(max_length=80,null=True,blank=True)

  def __str__(self):
    return self.team_name
  
  
class Contact(models.Model):
  full_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  message = models.TextField(max_length=1000)
  
  def __str__(self):
    return self.full_name
  
