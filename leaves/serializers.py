from rest_framework import serializers

from employees.serializers import MiniEmployeeSerializer
from leaves.models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'


class LeaveRequestDetailSerializer(serializers.ModelSerializer):
    employee = MiniEmployeeSerializer()
    reviewed_by = MiniEmployeeSerializer()

    class Meta:
        model = LeaveRequest
        fields = '__all__'

