from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=10, blank=True)  
    userImage=models.ImageField(upload_to="users/pictures",
    blank=True,
    null=True
    )
    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class regis(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField( blank=True,
    null=True)
    peso=models.DecimalField( max_digits=30,  decimal_places=2,  blank=True,
    null=True)
    altura=models.DecimalField(  max_digits=30,  decimal_places=2, blank=True,
    null=True)
    fecha=models.DateField(   blank=True,
    null=True)
    hora=models.TimeField(   blank=True,
    null=True)

class boletos(models.Model):
    Usuario=models.CharField( max_length=15,blank=True,null=True)
    total=models.DecimalField( max_digits=30,  decimal_places=2,  blank=True,
    null=True)
    subtotal=models.DecimalField( max_digits=30,  decimal_places=2,  blank=True,
    null=True)
    Descuento=models.CharField( max_length=5,blank=True,null=True)
    Valor=models.DecimalField( max_digits=30,  decimal_places=2,  blank=True,
    null=True)
    
   