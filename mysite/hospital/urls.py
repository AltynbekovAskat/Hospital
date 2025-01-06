from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'patientProfile', PatientProfileViewSet, basename='patientProfile')
router.register(r'doctors', DoctorsViewSet, basename='doctors')
router.register(r'speciality', SpecialityViewSet, basename=' specialty')
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'appointment', AppointmentsViewSet, basename='appointment')
router.register(r'medicalrecord', MedicalRecordViewSet, basename='medicalrecord')
router.register(r'prescriptions', PrescriptionsViewSet, basename='prescriptions')
router.register(r'ward', WardsViewSet, basename='ward')
router.register(r'feedbacks', FeedbacksViewSet, basename='feedbacks')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', ProfileListAPIview.as_view(), name='profile'),
    path('contactInfo/',  ContactInfoListAPIview.as_view(), name='ContactInfo'),
    path('Billing/',  BillingListAPIview.as_view(), name='Billing'),
]

