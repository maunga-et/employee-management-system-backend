from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeDetailSerializer, MiniEmployeeSerializer


class CreateEmployeeAPIView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer


class RetrieveEmployeeAPIView(generics.RetrieveAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()


class DeleteEmployeeAPIView(generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class UpdateEmployeeAPIView(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class ListEmployeesAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(is_active=True)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_number_of_employees(request):
    number_of_employees = Employee.objects.all().count()
    return Response(data={'count': number_of_employees}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_number_of_employees_under_a_supervisor(request, supervisor_id):
    number_of_employees = Employee.objects.filter(supervisor_id=supervisor_id, is_active=True).count()
    return Response(data={'count': number_of_employees}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_employees_under_a_supervisor(request, supervisor_id):
    employees = Employee.objects.filter(supervisor_id=supervisor_id, is_active=True)
    serializer = MiniEmployeeSerializer(employees, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
