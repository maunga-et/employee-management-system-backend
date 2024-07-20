from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .constants import EMPLOYEE_ROLES, GENDER_OPTIONS


class EmployeeManager(BaseUserManager):
    def create_user(self, employee_number, first_name, last_name, role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not employee_number:
            raise ValueError("Users must have an employee number")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not role:
            raise ValueError("Users must have a role")

        user = self.model(
            employee_number=employee_number,
            first_name=first_name,
            last_name=last_name,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_number, first_name, last_name, role, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            employee_number=employee_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_names = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDER_OPTIONS)
    national_identification_number = models.CharField(max_length=255, unique=True, blank=True, null=True)
    role = models.CharField(max_length=255, blank=False, null=False, choices=EMPLOYEE_ROLES)
    employee_number = models.CharField(max_length=255, unique=True, blank=True, null=True)
    picture = models.ImageField(upload_to='employee_pictures', blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    employment_type = models.CharField(max_length=255, blank=True, null=True, default='FULL_TIME')
    residential_address = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = "employee_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    def __str__(self):
        return self.employee_number

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
