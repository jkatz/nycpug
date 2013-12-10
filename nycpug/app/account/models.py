from django.db import models

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save, pre_save

__all__ = [
    'Profile', 'User',
]

class Profile(models.Model):
    """information used in "speaker" profile that can be assigned to the user"""
    user = models.OneToOneField('User')
    title = models.TextField()
    company = models.TextField()
    description = models.TextField()
    url = models.URLField(null=True, blank=True, help_text="URL to the website of a User")
    twitter = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True, help_text="URL to Facebook page")
    linkedin = models.URLField(null=True, blank=True, help_text="URL to LinkedIn page")
    irc = models.TextField(null=True, blank=True)

## need a custom manager for the custom User class
class UserManager(BaseUserManager):
    """
    borrowed from the Django default, this enables us to have the key user management functions
    in order to properly create users, superusers, etc. from all parts of the app
    """

    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a User with the given email and password"""
        if not email:
            raise ValueError('The email must be set')
        email = email.lower().strip()
        now = datetime.now()
        user = self.model(
            email=email,
            is_active=True,
            is_staff=False,
            is_superuser=False,
            last_login=now,
            **extra_fields)
        user.set_password(password) if password else user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    manage the user information pertaining to auth
    right now only supports email authentication
    """
    USERNAME_FIELD = 'email'

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField(default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(auto_now_add=True)

    # custom manager
    objects = UserManager()

    def get_full_name(self):
        return self.name.strip()

    def get_short_name(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.name

def clean_email(sender, instance, *args, **kwargs):
    """
    clean email data and make sure things are accurate,
    i.e. email is all lowercase
    """
    if isinstance(instance.email, (str, unicode)):
        instance.email = instance.email.lower().strip()

def create_profile(sender, instance, created, *args, **kwargs):
    """create an account.Profile for the created account.User"""
    if created:
        Profile(user=instance).save()

pre_save.connect(clean_email, sender=User)
post_save.connect(create_profile, sender=User)
