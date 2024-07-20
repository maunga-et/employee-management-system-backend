from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from leaves.models import LeaveRequest
from leaves.serializers import LeaveRequestSerializer, LeaveRequestDetailSerializer


class CreateLeaveRequestAPIView(generics.CreateAPIView):
    serializer_class = LeaveRequestSerializer


class UpdateLeaveRequestAPIView(generics.UpdateAPIView):
    serializer_class = LeaveRequestSerializer
    queryset = LeaveRequest.objects.all()


class ListLeaveRequestsAPIView(generics.ListAPIView):
    serializer_class = LeaveRequestDetailSerializer
    queryset = LeaveRequest.objects.all()


class DeleteLeaveRequest(generics.DestroyAPIView):
    serializer_class = LeaveRequestSerializer
    queryset = LeaveRequest.objects.all()


class RetrieveLeaveRequestAPIView(generics.RetrieveAPIView):
    serializer_class = LeaveRequestDetailSerializer
    queryset = LeaveRequest.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_number_of_unreviewed_leave_requests(request):
    number_of_unreviewed_leave_requests = LeaveRequest.objects.filter(status='PENDING').count()
    return Response(data={'count': number_of_unreviewed_leave_requests}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_leave_requests_by_user_id(request, employee_id):
    leave_requests = LeaveRequest.objects.filter(employee_id=employee_id)
    serializer = LeaveRequestDetailSerializer(leave_requests, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_leave_requests_by_supervisor_id(request, supervisor_id):
    leave_requests = LeaveRequest.objects.filter(employee__supervisor_id=supervisor_id)
    serializer = LeaveRequestDetailSerializer(leave_requests, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
