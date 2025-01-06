from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class PrescriptionsInline(admin.TabularInline):
    model = Prescriptions
    extra = 1


@admin.register(Doctors)
class ProductAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1


class HospitalAdmin(admin.ModelAdmin):
    inlines = [ContactInfoInline]


#admin.site.register(ContactInfo)


@admin.register(Profile, PatientProfile, Hospital, Speciality, Direction_and_Services, Department, Appointments, Wards, Feedbacks)
class ProductAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Billing)


@admin.register(MedicalRecord,)
class ProductAdmin(TranslationAdmin):
    inlines = [PrescriptionsInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# admin.site.register(Profile)
# admin.site.register(PatientProfile)
# admin.site.register(Speciality)
# admin.site.register(Department)
# admin.site.register(Appointments)
# admin.site.register(MedicalRecord)
# admin.site.register(Prescriptions)
# admin.site.register(Billing)
# admin.site.register(Wards)
# admin.site.register(Feedbacks)
