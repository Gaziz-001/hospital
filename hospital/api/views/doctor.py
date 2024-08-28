from rest_framework import mixins
from rest_framework.response import Response

from api.models import Doctor, Patient
from api.mixin import HospitalGenericViewSet
from api.serializers.doctor import DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer, \
    DoctorUpdateSerializer
# ServiceListSerializer, ServiceRetrieveSerializer, ServiceCreateSerializer, \
#     ServiceUpdateSerializer, VisitListSerializer, VisitRetrieveSerializer, VisitCreateSerializer, VisitUpdateSerializer, PatientListSerializer)
from api.serializers.patient import PatientListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import DoctorFilterSet


class DoctorView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    lookup_field = '_id'

    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet


    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient', ]
        else:
            self.action_permissions = []

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

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits_doctor_id=id).all()
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)

#
# class ServiceView(
#     HospitalGenericViewSet,
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin
# ):
#
#     lookup_field = 'id'
#     filter_backends = [DjangoFilterBackend,]
#     filterset_fields = ['first_name', 'last_name', 'specialization']
#
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ServiceListSerializer
#         if self.action == 'retrieve':
#             return ServiceRetrieveSerializer
#         if self.action == 'create':
#             return ServiceCreateSerializer
#         if self.action == 'update':
#             return ServiceUpdateSerializer
#
#     def get_queryset(self):
#         return Service.objects.all()
#
# class VisitView(
#     HospitalGenericViewSet,
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin
# ):
#
#     lookup_field = 'id'
#     filter_backends = [DjangoFilterBackend,]
#     filterset_fields = ['first_name', 'last_name', 'specialization']
#
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return VisitListSerializer
#         if self.action == 'retrieve':
#             return VisitRetrieveSerializer
#         if self.action == 'create':
#             return VisitCreateSerializer
#         if self.action == 'update':
#             return VisitUpdateSerializer
#
#     def get_queryset(self):
#         return Visit.objects.all()
#
