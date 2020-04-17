"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/user_management/models.py
    Description: This module contains all model definitions for the user_management application.
--------------------------------------------------------------------------------------------------
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from employee_management.models import Employee


class UserManager(BaseUserManager):
    def create_user(self, username, employee, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have username")
        if not password:
            raise ValueError("User must have a password")
        if not employee:
            raise ValueError("User must have a associated Employee ID")

        user = self.model(username=username, employee_id=employee)
        user.set_password(password)
        user.admin = is_admin
        user.active = is_active
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, employee, password):
        user = self.create_user(
            username,
            employee,
            password,
            is_staff=True
            )
        return user

    def create_superuser(self, username, password=None, is_active=True, is_staff=True, is_admin=True):
        if not username:
            raise ValueError("User must have username")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(username=username)
        user.set_password(password)
        user.admin = is_admin
        user.active = is_active
        user.staff = is_staff
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name='Username')
    employee = models.OneToOneField(Employee,
                                    null=True,
                                    blank=True,
                                    verbose_name='Employee ID',
                                    related_name='user',
                                    on_delete=models.PROTECT)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='Email')
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Last name')
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return '{},{}'.format(self.username, self.employee)

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    class Meta:
        db_table = 'hrms_user'
