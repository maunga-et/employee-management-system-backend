from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from employees.models import Employee


class EmployeeTests(APITestCase):
    def setUp(self):
        employee = Employee.objects.create(
            first_name='Sam',
            last_name='Altman',
            role='ADMINISTRATOR',
            password='password',
            employee_number='abc123'
        )
        self.client.force_authenticate(user=employee)

    def test_create_employee(self):
        data = {
            "first_name": "Tanyaradzwa",
            "last_name": "Maunga",
            "role": "EMPLOYEE",
            "password": "password",
            "employee_number": "xyz123"
        }
        url = reverse('create_employee')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(Employee.objects.all().last().first_name, 'Tanyaradzwa')
        self.assertEqual(Employee.objects.all().last().last_name, 'Maunga')
        self.assertEqual(Employee.objects.all().last().role, 'EMPLOYEE')
        self.assertEqual(Employee.objects.all().last().employee_number, 'xyz123')

    def test_update_employee(self):
        data = {
            "first_name": "Emmanuel"
        }

        url = reverse('update_employee', kwargs={'pk': 1})

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.get(pk=1).first_name, 'Emmanuel')

    def test_delete_employee(self):
        url = reverse('delete_employee', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_employee(self):
        data = {
            "first_name": "Trill",
            "last_name": "Percy",
            "role": "EMPLOYEE",
            "password": "password",
            "employee_number": "qwe123"
        }
        create_employee_url = reverse('create_employee')

        create_employee_response = self.client.post(create_employee_url, data, format='json')

        url = reverse('retrieve_employee', kwargs={'pk': create_employee_response.data['id']})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(response.data['first_name'], 'Trill')
        self.assertEqual(response.data['last_name'], 'Percy')
        self.assertEqual(response.data['role'], 'EMPLOYEE')
        self.assertEqual(response.data['employee_number'], 'qwe123')

