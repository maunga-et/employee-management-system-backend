from django.db import models

from employees.models import Employee


class Department(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    department_code = models.CharField(max_length=255, unique=True)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
