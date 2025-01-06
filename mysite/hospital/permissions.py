from rest_framework.permissions import BasePermission
from rest_framework import permissions
#from mysite.hospital.models import Doctors, PatientProfile
from .models import Doctors, PatientProfile


class CheckDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, Doctors) and user.role == 'doctor':
            return True
        return False


class CheckPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, PatientProfile) and user.role == 'patient':
            return True
        return False


class CheсkReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.patient == request.user


