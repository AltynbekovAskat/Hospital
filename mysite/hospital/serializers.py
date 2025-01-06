from rest_framework import serializers
from rest_framework.authtoken.admin import User
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_picture', 'role', 'groups', 'user_permissions', 'user_permissions',
                  'address', 'date_of_birth']


class UserProSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_date):
        user = User.objects.create_user(**validated_date)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Не верный пароль или логин ")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['user', 'emergency_contact', 'blood_type', 'allergies', 'medical_history']


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['user', 'shift_start', 'shift_end', 'qualifications', 'experience_years', 'working_days']


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['speciality_name', 'speciality']


class Direction_and_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction_and_Services
        fields = '__all__'


class Name_and_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name_and_Services
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'dead_id', 'location']


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['patient_id', 'staff_id', 'date_time', 'status', 'notes']


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['patient_id', 'doctor_id', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']


class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = ['patient_id', 'staff_id', 'medication', 'dosage', 'created_at', 'medicalRecord']


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'


class WardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = ['name', 'ward_type', 'capacity', 'current_occupancy']


class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = ['doctor_id', 'patient_id', 'content', 'created_at']
