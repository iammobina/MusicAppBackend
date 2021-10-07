from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin
# Create your models here.


class Premium(models.Model):
    Premium_Types = (
        ('1 Month', '1 Month'),
        ('3 Month', '3 Month'),
        ('6 Month', '6 Month'),
        ('1 year', '1 year')
    )

    buydate =models.DateField()
    cost = models.CharField(max_length=1000, blank=False)
    leftdays = models.CharField(max_length=100, blank=True)
    type =models.CharField(max_length=100,choices=Premium_Types)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        user =  self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, blank=False,unique=True)
    name=models.CharField(max_length=100,blank=False)
    lastname=models.CharField(max_length=100,blank=False)
    phonenumber=models.CharField(max_length=10,blank=False)
    email=models.CharField(max_length=100,blank=False,unique=True)
    email2=models.CharField(max_length=100,blank=False)
    agreetoterms=models.BooleanField(default=True)
    subscription=models.ManyToManyField(Premium,related_name='Premium_User',blank=True)
    singerfacebooklinks = models.URLField(blank=True)
    singerinstalink = models.URLField(blank=True)
    artworks = models.ImageField(upload_to='Art_image', blank=False)


    objects=UserManager()

    USERNAME_FIELD='email'


