from django.db import models

from employees.models import Employee
from leaves.constants import LEAVE_REQUEST_STATUS_OPTIONS


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='requestor')
    start_date = models.DateField(blank=False, null=False)
    return_date = models.DateField(blank=False, null=False)
    status = models.CharField(
        max_length=255,
        default='PENDING',
        blank=True,
        null=True,
        choices=LEAVE_REQUEST_STATUS_OPTIONS
    )
    reason = models.TextField(blank=True, null=True)
    reviewed_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviewer', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
