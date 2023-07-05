from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    #many to one, 1 user can have many items
    #on delete specifies what happen if the user is deleted, so with cascade the items
    #are deletd too and with set to null the items stay
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )
    title = models.CharField(max_length=200)
    #we can use charfield but text field is more apporpriate for a form, more options
    description = models.TextField(null=True, blank= True)
    complete = models.BooleanField(default=False)
    create =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']