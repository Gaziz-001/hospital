from rest_framework import serializers

from api.models import Doctor, Service, Visit

class DoctorListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    contact_info = serializers.CharField()

class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'contact_info']
#
# class VisitListSerializer(serializers.Serializer):
#     full_name = serializers.CharField()
#     contact_info = serializers.CharField()
#
# class VisitRetrieveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#
# class VisitCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#
# class VisitUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ['specialization', 'contact_info']
#
# class ServiceListSerializer(serializers.Serializer):
#     full_name = serializers.CharField()
#     contact_info = serializers.CharField()
#
# class ServiceRetrieveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#
# class ServiceCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#
# class ServiceUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ['specialization', 'contact_info']

class PatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField()