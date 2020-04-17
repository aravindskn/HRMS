"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/employee_management/admin.py
    Description: This module contains all the models that are added in the django admin page.
--------------------------------------------------------------------------------------------------
"""
from django.contrib import admin
from .models import Address, EmployeeAddress, Employee, EmployeeContact, EmploymentDetails

admin.site.register(Address)
admin.site.register(EmployeeAddress)
admin.site.register(Employee)
admin.site.register(EmployeeContact)
admin.site.register(EmploymentDetails)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address_type')


class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'addr_type', 'addr_line_one', 'addr_line_two', 'addr_line_three', 'locality', 'city', 'postal_code')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'marital_status', 'employee_address')

