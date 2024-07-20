from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateEmployeeAPIView.as_view(), name='create_employee'),
    path('<int:pk>/', views.RetrieveEmployeeAPIView.as_view(), name='retrieve_employee'),
    path('<int:pk>/update/', views.UpdateEmployeeAPIView.as_view(), name='update_employee'),
    path('<int:pk>/delete/', views.DeleteEmployeeAPIView.as_view(), name='delete_employee'),
    path('list/', views.ListEmployeesAPIView.as_view(), name='list_employees'),
    path('count/', views.retrieve_number_of_employees, name='number_of_employees'),
    path(
        'count-by-supervisor/<int:supervisor_id>/',
        views.retrieve_number_of_employees_under_a_supervisor,
        name='number_of_employees_under_a_supervisor'
    ),
    path(
        'employees-under-a-supervisor/<int:supervisor_id>/',
        views.retrieve_employees_under_a_supervisor,
        name='employees_under_a_supervisor')
]
