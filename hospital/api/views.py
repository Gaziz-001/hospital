from .models import Doctor, Visit, Patient
from api.serializers import DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer, \
    DoctorUpdateSerializer, VisitListSerializer, VisitRetrieveSerializer, VisitCreateSerializer, \
    VisitUpdateSerializer, ServiceListSerializer, ServiceRetrieveSerializer, ServiceCreateSerializer, \
    ServiceUpdateSerializer, PatientListSerializer

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import DoctorAccessPermission
from rest_framework.decorators import action

class DoctorView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'
    permission_classes = [IsAuthenticated, DoctorAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.all()

        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits_doctor_id=id).all()
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)

class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'
    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer


    def get_queryset(self):
        return Service.objects.all()

class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'
    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return VisitUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer


    def get_queryset(self):
        return Visit.objects.all()

class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'
    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return VisitUpdateSerializer

    def get_queryset(self):
        return Visit.objects.all()
