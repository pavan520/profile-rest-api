from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager


# Create your models here.

class UserProfileManager(UserManager):
    """Helps Django to work with user model"""

    def create_user(self, name, email=None, password=None, **extra_fields):
        """ Creates a new user Object"""
        if not email:
            raise ValueError('Users must have an email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(
            password)  # set_password converts password string to hex fr security, so that text password can never be seen
        user.save(using=self.db)
        return user

    def create_super_user(self, name, email, password):
        """Creates and saves new super users with given details."""
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents user profile inside our System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Is required and must when u use custom user model

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def getFullName(self):
        """ USed to get user full name """
        return self.name

    def getShortName(self):
        """ USed to get user short name """
        return self.name

    def __str__(self):
        """Django uses this when need to convert object to string"""
        return self.email
