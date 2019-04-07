from django.conf import settings
from django.db import models
from django.utils import timezone

class TodoList(models.Model): 
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field 
    created_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    
    class meta:
    	ordering = ["-created_date"]
        #return self.created_date #ordering by the created field

    def __str__(self):
        return self.title #name to be shown when called