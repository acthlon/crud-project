from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser

# class User(AbstractUser):
#     email = models.EmailField(unique=True)


class Person(models.Model):

    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True, related_name='asuser' )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    city= models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'{self.first_name}_{self.last_name}_Data'
    
    # you can use the above or below format to write formatted string
        return '{}_{}_Data'.format(self.first_name,self.last_name)
    