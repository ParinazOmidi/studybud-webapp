from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    #USERNAME_FIELD = 'email'  # What field to use for login
    REQUIRED_FIELDS = []  # Additional required fields (username is already required by AbstractUser)

class Topic(models.Model): 
   name = models.CharField(max_length =200)

   def __str__(self):
       return self.name

class Room(models.Model): 
   host= models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
   topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
   name = models.CharField(max_length =200)
   description = models.TextField(null= True, blank= True)
   participants= models.ManyToManyField(User, related_name ='participants', blank=True)
   updated = models.DateTimeField(auto_now= True)
#  this is going to take a snapshot of anytime this model instance was updated
#  participants = #store all the users that are currently active in a room 
   created = models.DateTimeField(auto_now_add= True)
#  auto_now_add vs auto_now is auto now add only takes a timestamp when we first save or create
#  so if we save it multiple time it will not update the timestamp
   class Meta: 
       ordering = ['-updated', '-created']


   def __str__(self): 
       return self.name
     

class Message(models.Model):     
   user = models.ForeignKey(User, on_delete=models.CASCADE)    
   room = models.ForeignKey(Room, on_delete=models.CASCADE)     
   body = models.TextField()
   updated = models.DateTimeField(auto_now=True)     
   created = models.DateTimeField(auto_now_add=True)      
    
   class Meta: 
       ordering = ['-updated', '-created']
    
   def __str__(self):          
       return self.body[0:50]
   
#first 50 caracters
