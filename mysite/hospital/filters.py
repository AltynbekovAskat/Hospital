from django_filters import FilterSet
from .models import Doctors


class DoctorsFilter(FilterSet):
    class Meta:
        model = Doctors
        fields = {
            'qualifications': ['exact'],
            'experience_years': ['exact'],
        }
