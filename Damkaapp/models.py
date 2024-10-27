from django.db import models

# Create your models here.
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
import uuid




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    

    def save_profile(self):
        self.save()
        
        

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
            
class Activity(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    Image = CloudinaryField('image', null= True) 
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # admin_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    
    
    def save_activities(self):
        self.save()
    
    def delete_activities(self):
        self.delete()
        
    @classmethod
    def get_allactivities(cls):
        activities = cls.objects.all()
        return activities
    
   
    
    @classmethod
    def get_activities(request, id):
        try:
            account = Activity.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return account
    
    def update_activities(self):
        self.update_activities()
    
    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Activities'
        verbose_name_plural = 'Activities'

            
class Event(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    Image = CloudinaryField('image', null= True)
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    admin_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    
    
    def save_events(self):
        self.save()
    
    def delete_events(self):
        self.delete()
        
    @classmethod
    def get_allevents(cls):
        accounts = cls.objects.all()
        return accounts
    
   
    
    @classmethod
    def get_events(request, id):
        try:
            account = Activity.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return account
    
    def update_events(self):
        self.update_events()
    
    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Events'
        verbose_name_plural = 'Events'