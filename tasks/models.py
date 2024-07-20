from django.db import models

from employees.models import Employee
from tasks.constants import TASK_STATUS_OPTIONS


class Task(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='owner', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_started = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='the_supervisor')
    status = models.CharField(max_length=255, default='NOT_STARTED', choices=TASK_STATUS_OPTIONS)
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='the_reviewer')

    def __str__(self):
        return self.title

