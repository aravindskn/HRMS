"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/employee_management/models.py
    Description: This module contains all model definitions that are common across the different
    categories of entities in hrms application.
--------------------------------------------------------------------------------------------------
"""
from django.db import models
from ref_data_management.models import (AbstractBaseModel, RefCountry,
                                         RefStateProvince, RefDepartment,
                                         RefDesignation, RefGender,
                                         RefMaritalStatus, RefAddressType,
                                         RefContactType
                                       )


class Address(AbstractBaseModel):
    """
      Model provides representation of Address record.

      Attributes:
          addr_line_one (CharField, mandatory): First line of address.
          addr_line_two (CharField, optional): Second line of address.
          addr_line_three (CharField, optional): Third line of address.
          locality (CharField, mandatory): Locality.
          city (CharField, mandatory): City.
          state_province (ForeignKey(StateProvince)): State.
          country (ForeignKey(Country)): Country.
          postal_code (CharField, mandatory): Postal code.
          latitude (DecimalField, optional): Latitude value of the address.
          longitude (DecimalField, optional): Longitude value of the address.
    """
    addr_line_one = models.CharField(max_length=255, blank=False, null=False, verbose_name='Address line one')
    addr_line_two = models.CharField(max_length=255, blank=True, null=True, verbose_name='Address line two')
    addr_line_three = models.CharField(max_length=255, blank=True, null=True, verbose_name='Address line three')
    locality = models.CharField(max_length=255, blank=True, null=True, verbose_name='Locality')
    city = models.CharField(max_length=255, blank=False, null=False, verbose_name='City')
    state_province = models.ForeignKey(RefStateProvince,
                                       null=False,
                                       blank=False,
                                       verbose_name='State/Province',
                                       on_delete=models.PROTECT,
                                       related_name='addresses')
    country = models.ForeignKey(RefCountry,
                                null=False,
                                blank=False,
                                verbose_name='Country',
                                on_delete=models.PROTECT,
                                related_name='addresses')
    postal_code = models.CharField(max_length=255, blank=False, null=False, verbose_name='Postal code')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Latitude', null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='Longitude', null=True, blank=True)

    def __str__(self):
        """
          Method that returns address types.
        """
        return '{}, {}, {}, {}, {}, {}'.format(self.addr_line_one,
                                               self.addr_line_two,
                                               self.addr_line_three,
                                               self.city,
                                               self.state_province,
                                               self.country)

    class Meta:
        db_table = 'hrms_address'  # Name of the database table


class Employee(AbstractBaseModel):
    """
      Model provides representation of Employee record.

      Attributes:
        employee_id (CharField, mandatory): Employee ID.
        first_name (CharField, mandatory): First name of an employee.
        middle_name (CharField, optional): Middle name of an employee.
        last_name (CharField, mandatory): Last name of an employee.
        date_of_birth (CharField, mandatory): Date of birth of an employee.
        gender (ForeignKey(Gender)): Gender.
        marital_status (ForeignKey(MaritalStatus)): Marital Status.
    """
    employee_id = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='Employee ID')
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='First name')
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Middle name')
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Last name')
    date_of_birth = models.DateField(null=False, blank=False, verbose_name='Date of birth')
    gender = models.ForeignKey(RefGender,
                               blank=False,
                               null=False,
                               verbose_name='Gender',
                               on_delete=models.PROTECT,
                               related_name='employees')
    marital_status = models.ForeignKey(RefMaritalStatus,
                                       blank=True,
                                       null=True,
                                       verbose_name='Marital Status',
                                       on_delete=models.PROTECT,
                                       related_name='employees')

    def __str__(self):
        """
          Method that returns the id of each employee
        """
        return '{}, {}, {}'.format(self.employee_id, self.first_name, self.last_name)

    class Meta:
        db_table = 'hrms_employee'  # Name of the database table


class EmployeeAddress(AbstractBaseModel):
    """
      Model provides representation of different address types.

      Attributes:
          address_type (CharField, mandatory): Types of address.
          address (ForeignKey(Address), mandatory): Address.
          employee (ForeignKey(Employee), mandatory): Employee ID.
    """
    address_type = models.ForeignKey(RefAddressType,
                                     blank=False,
                                     null=False,
                                     verbose_name='Type of address',
                                     on_delete=models.PROTECT,
                                     related_name='addresses')
    address = models.ForeignKey(Address,
                                blank=False,
                                null=False,
                                verbose_name='Address',
                                on_delete=models.PROTECT,
                                related_name='addresses')
    employee = models.ForeignKey(Employee,
                                 blank=False,
                                 null=False,
                                 verbose_name='Employee id',
                                 on_delete=models.PROTECT,
                                 related_name='addresses')

    def __str__(self):
        """
          Method that returns address types.
        """
        return '{}, {}'.format(self.address_type, self.address)

    class Meta:
        db_table = 'hrms_employee_address'  # Name of the database table


class EmployeeContact(AbstractBaseModel):
    """
        Model provides representation of different contacts.

      Attributes:
          contact_value (CharField, mandatory): Value of selected contact type.
          contact_type (ForeignKey(RefContactType), mandatory): Type of contact.
          employee (ForeignKey(Employee), mandatory): Employee ID.
    """
    contact_value = models.CharField(max_length=255,
                                     blank=False,
                                     null=False,
                                     verbose_name='Contact value')
    contact_type = models.ForeignKey(RefContactType,
                                     blank=False,
                                     null=False,
                                     on_delete=models.PROTECT,
                                     verbose_name='Contact type',
                                     related_name='contacts')
    employee = models.ForeignKey(Employee,
                                 blank=False,
                                 null=False,
                                 on_delete=models.PROTECT,
                                 related_name='contacts',
                                 verbose_name='Employee id')

    def __str__(self):
        return '{}, {}'.format(self.contact_value, self.contact_type)

    class Meta:
        db_table = 'hrms_employee_contact'


class EmploymentDetails(AbstractBaseModel):
    """
        Model provides representation of different employement details.

      Attributes:
          employment_start_date (DateField, mandatory): Date of joining.
          employment_end_date (DateField, optional): Date of leaving employment.
          employee (ForeignKey(Employee), mandatory): Employee ID.
          department (ForeignKey(RefDepartment), mandatory): Department.
          designation (ForeignKey(RefDesignation), mandatory): Designation.
    """
    employment_start_date = models.DateField(null=False, blank=False, verbose_name='Employment start date')
    employment_end_date = models.DateField(null=True, blank=True, verbose_name='Employment end date')

    employee = models.ForeignKey(Employee,
                                 blank=False,
                                 null=False,
                                 on_delete=models.PROTECT,
                                 verbose_name='employee id',
                                 related_name='employment_details')
    department = models.ForeignKey(RefDepartment,
                                   blank=False,
                                   null=False,
                                   on_delete=models.PROTECT,
                                   verbose_name='Department',
                                   related_name='employment_details')
    designation = models.ForeignKey(RefDesignation,
                                    blank=False,
                                    null=False,
                                    on_delete=models.PROTECT,
                                    related_name='employment_details',
                                    verbose_name='Designation')

    def __str__(self):
        return '{}'.format(self.department)

    class Meta:
        db_table = 'hrms_employment_details'



