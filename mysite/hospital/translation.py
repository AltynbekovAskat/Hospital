from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Doctors)
class ProductTranslationOptions(TranslationOptions):
    fields = ('qualifications',)


@register(Profile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


@register(PatientProfile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('allergies',)


@register(Hospital)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hospital_name', 'address')


@register(Speciality)
class ProductTranslationOptions(TranslationOptions):
    fields = ('speciality_name',)


@register(Direction_and_Services)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Department)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'location')


@register(Appointments)
class ProductTranslationOptions(TranslationOptions):
    fields = ('status', 'notes')


@register(MedicalRecord)
class ProductTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'prescribed_medication')


@register(Prescriptions)
class ProductTranslationOptions(TranslationOptions):
    fields = ('medication', 'dosage')


@register(Wards)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'ward_type', 'capacity', 'current_occupancy')


@register(Feedbacks)
class ProductTranslationOptions(TranslationOptions):
    fields = ('content',)
