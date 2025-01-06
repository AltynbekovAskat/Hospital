from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class Profile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='picture/')
    ROLE_CHOICES = [
        ('администратор', 'администратор'),
        ('врач', 'врач'),
        ('пациент', 'пациент'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='пациент')
    groups = models.ManyToManyField(Group, related_name='profile_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='profile_permissions', blank=True)
    address = models.TextField()
    date_of_birth = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class PatientProfile(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='patientProfile')
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    BLOOD_CHOICES = [
        ('Бомбейский фенотип (hh)', 'Бомбейский фенотип (hh)'),
        ('Золотая кровь (Rh-нулевой)', 'Золотая кровь (Rh-нулевой)'),
        ('Группа крови О−', 'Группа крови О−'),
        ('Группа крови О+', 'Группа крови О+'), ('Группа крови А−', 'Группа крови А−'),
        ('Группа крови А+', 'Группа крови А+'), ('Группа крови Б−', 'Группа крови Б−'),
        ('Группа крови В+', 'Группа крови В+'),
        ('Группа крови АБ−', 'Группа крови АБ−'), ('Группа крови АБ+', 'Группа крови АБ+'),
]
    blood_type = MultiSelectField(max_length=43, max_choices=2, choices=BLOOD_CHOICES, )
    allergies = models.TextField(null=True,  blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.emergency_contact}'


class Doctors(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='doctor_profile')
    shift_start = models.TimeField(null=True, blank=True)
    shift_end = models.TimeField(null=True, blank=True)
    qualifications = models.CharField(max_length=15)
    experience_years = models.CharField(max_length=5)
    WEEKS_DAY = [
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
    ]
    working_days = MultiSelectField(max_length=32, choices=WEEKS_DAY, max_choices=3)

    def __str__(self):
        return f'{self.qualifications}, {self.experience_years}'


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=32, unique=True)
    hospital_image = models.ImageField(upload_to='hospital_image/')
    address = models.CharField(max_length=32)
    description = models.TextField()
    chief_physician = models.OneToOneField(Doctors, on_delete=models.CASCADE, verbose_name='Главный врач')
    operating_mode = models.CharField(max_length=300)

    def __str__(self):
        return f'({self.hospital_image}, {self.address}'


class ContactInfo(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Speciality(models.Model):
    speciality_name = models.CharField(max_length=20)
    speciality = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='speciality')

    def __str__(self):
        return f'{self.speciality}'


class Direction_and_Services(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    doctor = models.ManyToManyField(Doctors)

    def __str__(self):
        return self.name


class Name_and_Services(models.Model):
    name = models.ForeignKey(Direction_and_Services, on_delete=models.CASCADE, related_name='service_name')
    description = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.description}'


class Department(models.Model):
    name = models.CharField(max_length=20)
    dead_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='dead_id')
    location = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.name}'


class Appointments(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_id')
    staff_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='staff_id')
    date_time = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('scheduled', 'scheduled'),
        ('completed', 'completed'),
        ('canceled', 'canceled')
    )
    status = models.CharField(max_length=10, choices=STATUS)
    notes = models.TextField()

    def __str__(self):
        return f'{self.status}'


class MedicalRecord(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='medicalrecord')
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='doctor_id')
    diagnosis = models.CharField(max_length=45)
    treatment = models.CharField(max_length=40)
    prescribed_medication = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.diagnosis}, {self.treatment}'


class Prescriptions(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='prescriptions')
    staff_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='doctor')
    medication = models.CharField(max_length=15)
    dosage = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    medicalRecord = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.medication}, {self.dosage}'


class Billing(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='billing')
    total_amount = models.PositiveIntegerField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient_id}, {self.issued_date}'


class Wards(models.Model):
    name = models.CharField(max_length=20, unique=True)
    WARD_TYPE = (
        ('VIP', 'VIP'),
        ('STANDARD', 'STANDARD')
    )
    ward_type = models.CharField(max_length=10,  choices=WARD_TYPE, default='STANDARD')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    capacity = models.CharField(max_length=6)
    current_occupancy = models.CharField(max_length=3)

    def get_count_patient(self):
        patients = self.patient
        return patients.count()

    def get_total_capacity(self):
        return self.capacity - self.get_count_patient()

    def __str__(self):
        return f'{self.name}, {self.ward_type}'


class Feedbacks(models.Model):
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='feedbacks')
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}, {self.patient_id}'
