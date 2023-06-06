from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email,password=None,**others):
        if not email:
            raise ValueError("Please, provide an email")
        
        email=self.normalize_email(email)
        user=self.model(
            email=email,
            password=password,
            **others
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**others):
        others.setdefault('is_staff',True)
        others.setdefault('is_superuser',True)

        #if not raise error

        if others.get('is_staff') is not True:
            raise ValueError("Superuser must be a staff member")
        if others.get("is_superuser") is not True:
            raise ValueError("superuser must be True")
        
        return self.create_user(email=email,password=password,**others)
        


class User(AbstractUser):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)


    objects=CustomUserManager()
    REQUIRED_FIELDS=['username']
    USERNAME_FIELD='email'

    def __str__(self):
        return f"<User: {self.username}>"
