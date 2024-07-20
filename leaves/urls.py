from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateLeaveRequestAPIView.as_view(), name='create_leave_request'),
    path('<int:pk>/', views.RetrieveLeaveRequestAPIView.as_view(), name='retrieve_leave-request'),
    path('<int:pk>/update/', views.UpdateLeaveRequestAPIView.as_view(), name='update_leave_request'),
    path('<int:pk>/delete/', views.DeleteLeaveRequest.as_view(), name='delete_leave_request'),
    path('list/', views.ListLeaveRequestsAPIView.as_view(), name='list_leave_requests'),
    path('count/pending/', views.retrieve_number_of_unreviewed_leave_requests, name='retrieve_pending_leave_request'),
    path(
        'list/<int:employee_id>/',
        views.retrieve_leave_requests_by_user_id,
        name='retrieve_leave_requests_by_employee'
    ),
    path(
        'list-by-supervisor-id/<int:supervisor_id>/',
        views.retrieve_leave_requests_by_supervisor_id,
        name='retrieve_leave_requests_by_employee'
    )
]
