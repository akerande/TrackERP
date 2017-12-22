# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser,BaseUserManager ,Group
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    dob = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    previous_designation = models.CharField(max_length=100, null=True, blank=True)
    shift = models.CharField(max_length=100, null=True, blank=True)
    emp_id = models.IntegerField(blank=True, unique=True, null=True)
    project = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

