from django.db import models

# Create your models here.
class MemberModel(models.Model):
    name = models.CharField(max_length = 200)
    
    
    
    
  
        
    def __str__(self):
        return self.name