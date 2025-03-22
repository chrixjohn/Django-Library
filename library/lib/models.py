from django.db import models

# Create your models here.



  

class FormModel(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length=200)
    des=models.TextField()
    img=models.ImageField(upload_to='images/',null=True)
    status=models.BooleanField(default=True)
    
    
  
        
    def __str__(self):
        return self.title