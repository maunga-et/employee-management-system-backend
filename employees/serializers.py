from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        employee.set_password(validated_data['password'])
        last_saved = Employee.objects.last().id
        employee.employee_number = f'E000{last_saved + 1}'
        employee.save()
        return employee


class EmployeeSupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'employee_number']


class MiniEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'employee_number', 'gender', 'role']


class EmployeeDetailSerializer(serializers.ModelSerializer):
    supervisor = EmployeeSupervisorSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
