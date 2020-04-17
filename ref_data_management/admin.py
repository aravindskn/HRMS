"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/ref_data_management/admin.py
    Description: This module contains all admin page definitions for the ref_data_management application.
--------------------------------------------------------------------------------------------------
"""
from django.contrib import admin
from .models import RefCountry
from .models import RefStateProvince
from .models import RefMaritalStatus
from .models import RefContactType
from .models import RefAddressType
from .models import RefGender
from .models import RefDepartment
from .models import RefDesignation
from .models import RefTargetUnit
from .models import RefPerformanceRecStatus
from .models import RefRatingScale
from .models import RefLeaveRevisionType
from .models import RefLeaveType
from .models import RefLeaveRequestStatus

admin.site.register(RefCountry)         # Adds Country to admins page
admin.site.register(RefStateProvince)   # Adds StateProvince to admins page
admin.site.register(RefMaritalStatus)   # Adding the Marital Status to Admin Page
admin.site.register(RefContactType)     # Adds Contact Type to admins page
admin.site.register(RefAddressType)     # Adds Address Type to admins page
admin.site.register(RefGender)          # Adding the Gender to Admin Page
admin.site.register(RefDepartment)      # Adding the Department to Admin Page
admin.site.register(RefDesignation)     # Adding the Designation to Admin Page
admin.site.register(RefTargetUnit)      # Adding the Target Unit to Admin Page
admin.site.register(RefPerformanceRecStatus)    # Adding the Performance Record Status to Admin Page
admin.site.register(RefRatingScale)     # Adding the Rating Scale to Admin Page
admin.site.register(RefLeaveRequestStatus) #Adding leave request status to admin page
admin.site.register(RefLeaveType)          #Adding Leave type to admin page
admin.site.register(RefLeaveRevisionType)   #Adding leave revision type to admin page


class DepartmentAdmin(admin.ModelAdmin):
    """
        The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'department_name', 'department_code', 'department_description')


class DesignationAdmin(admin.ModelAdmin):
    """
        The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'designation_name', 'designation_code', 'designation_description')


class GenderAdmin(admin.ModelAdmin):
    """
            The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'gender_type', 'gender_description')


class MaritalStatusAdmin(admin.ModelAdmin):
    """
            The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'marital_status_type', 'marital_status_description')


class CountryAdmin(admin.ModelAdmin):
    """
        The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'country_name', 'country_iso_code', 'country_code')


class StateProvince(admin.ModelAdmin):
    """
        The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'state_name', 'state_code')


class AddressType(admin.ModelAdmin):
    """
        The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'address_type')


class ContactType(admin.ModelAdmin):
    """
        The class for defining the attributes to be displayed in the admin page.
    """
    list_display = ('id', 'contact_type')
