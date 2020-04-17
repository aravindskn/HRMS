"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/ref_data_management/models.py
    Description: This module contains all model definitions for the ref_data_management application.
--------------------------------------------------------------------------------------------------
"""
from django.db import models


class AbstractBaseModel(models.Model):
    """
           This abstract model provides the details related to creation , update and deletion of attributes

            Attributes :
            created_by (CharField , mandatory) : It holds the value by whom created the attribute
            created_date (DateField , mandatory) : It holds the value of when it was created
            last_updated_by (CharField , mandatory) : It holds the value of who updated or modified the data
            last_updated_date (DateField , mandatory) : It holds the value of when it was last updated
            deleted_status (Boolean , mandatory) : It holds the value of whether it was deleted or not
            deleted_date (DateField , mandatory) : It holds the value of when that data was deleted

    """

    created_by = models.CharField(max_length=255, blank=False, null=False, verbose_name='Created by')
    last_updated_by = models.CharField(max_length=255, blank=False, null=False, verbose_name='Last updated by')
    last_updated_date = models.DateField(auto_now_add=True, blank=False, null=False, verbose_name='Last updated date')
    deleted_status = models.BooleanField(default=False, blank=False, null=False, verbose_name='Deleted status')
    deleted_date = models.DateField(blank=True, null=True, verbose_name='Deleted date')
    created_date = models.DateField(auto_now_add=True, blank=False, null=False, verbose_name='Created date')

    def __str__(self):
        return self.last_updated_date

    class Meta:
        abstract = True


class RefCountry(AbstractBaseModel):
    """
            This model provides representation of countries , country_iso_code and country_code

            Attributes:
            country_name (CharField , mandatory) : It holds the value of country name
            country_iso_code (CharField , mandatory) : It holds the value of country's ISO code
            country_code (CharField , mandatory) : It holds the value of county's code
    """

    country_name = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Country name')
    country_iso_code = models.CharField(max_length=255,
                                        blank=False,
                                        null=False,
                                        unique=True,
                                        verbose_name='Country iso code')
    country_code = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Country code')

    def __str__(self):
        return '{}'.format(self.country_name)

    class Meta:
        db_table = 'ref_country'


class RefStateProvince(AbstractBaseModel):
    """
           This model provides representation of countries , country_iso_code and country_code

           Attributes:
           state_name (CharField , mandatory) : It holds the value of state name
           state_code (CharField , mandatory) : It holds the value of state code
           country_id (ForeignKey(Country)): country
    """
    state_name = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='State name')
    state_code = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='State code')
    country = models.ForeignKey(RefCountry,
                                blank=False,
                                null=False,
                                on_delete=models.PROTECT,
                                verbose_name='Country ID',
                                related_name='state')

    def __str__(self):
        return '{}'.format(self.state_name)

    class Meta:
        db_table = 'ref_state_province'


class RefMaritalStatus(AbstractBaseModel):
    """
            This model provides representation of marital status model

            Attributes:
            marital_status(CharField , mandatory) : holds which type of marital_status
    """

    marital_status = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name='Marital status')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.marital_status

    class Meta:
        db_table = 'ref_marital_status'


class RefContactType(AbstractBaseModel):
    """
            This model provides representation of contact_type

            Attributes:
            contact_type(CharField , mandatory) : holds which type of contact
            description(TextField , optional) : holds description of which type of contact
    """
    contact_type = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Contact type')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.contact_type

    class Meta:
        db_table = 'ref_contact_type'


class RefAddressType(AbstractBaseModel):
    """
            This model provides representation of address_type

            Attributes:
            address_type(CharField , mandatory) : holds which type of address
            description(TextField , optional) : holds description of which type of address
    """
    address_type = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Address type')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.address_type

    class Meta:
        db_table = 'ref_address_type'


class RefGender(AbstractBaseModel):
    """
            This model provides representation of gender

            Attributes:
            gender_type(CharField , mandatory) : holds which type of gender
            description(TextField , optional) : holds description of which type of gender
    """
    gender_type = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='Gender type')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.gender_type

    class Meta:
        db_table = 'ref_gender'


class RefDepartment(AbstractBaseModel):
    """
            This model provides representation of department

            Attributes:
            department_name(CharField , mandatory) : holds department name
            department_code(CharField , mandatory) : holds department code
            description(TextField , optional) : holds description of department
    """
    department_name = models.CharField(max_length=255,
                                       blank=False,
                                       null=False,
                                       unique=True,
                                       verbose_name='Department name')
    department_code = models.CharField(max_length=255,
                                       blank=False,
                                       null=False,
                                       unique=True,
                                       verbose_name='Department code')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return '{}'.format(self.department_name)

    class Meta:
        db_table = 'ref_department'


class RefDesignation(AbstractBaseModel):
    """
            This model provides representation of designation

            Attributes:
            designation_name(CharField , mandatory) : holds designation name
            description(TextField , optional) : holds description of designation
    """
    designation_name = models.CharField(max_length=255,
                                        blank=False,
                                        null=False,
                                        unique=True,
                                        verbose_name='Designation name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.designation_name

    class Meta:
        db_table = 'ref_designation'


class RefTargetUnit(AbstractBaseModel):
    """
       This model provides representation of Target Unit.
       Attributes:
            target_unit (CharField, mandatory): Target Unit.
            description (TextField, optional) : Description.
    """
    target_unit = models.CharField(max_length=255,
                                   blank=False,
                                   null=False,
                                   unique=True,
                                   verbose_name='Target Unit')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.target_unit

    class Meta:
        db_table = 'ref_target_unit'


class RefPerformanceRecStatus(AbstractBaseModel):
    """
        This model provides representation of Performance Record Status.

        Attributes:
            status_name (CharField, mandatory): Status.
            description (TextField, optional) : Description.
    """
    status_name = models.CharField(max_length=255,
                                   blank=False,
                                   null=False,
                                   unique=True,
                                   verbose_name='Status')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = 'ref_performance_rec_status'


class RefRatingScale(AbstractBaseModel):
    """
        This model provides representation of Rating Scale.

        Attributes:
            rating_scale (CharField, mandatory): Rating Scale.
            description (TextField, optional) : Description.
    """
    rating_value = models.CharField(max_length=255,
                                    blank=False,
                                    null=False,
                                    unique=True,
                                    verbose_name='Status')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.rating_value

    class Meta:
        db_table = 'ref_rating_scale'


class RefLeaveType(AbstractBaseModel):
    """
        This model provides representation of Performance Record Status.

        Attributes:
            leave_type_name (CharField, mandatory): leave_type.
            description (TextField, optional) : Description.
    """
    leave_type_name = models.CharField(
                                        max_length=255,
                                        blank=False,
                                        null=False,
                                        verbose_name='Leave type name'
                                      )
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.leave_type_name

    class Meta:
        db_table = 'ref_leave_type'


class RefLeaveRequestStatus(AbstractBaseModel):
    """
        This model provides representation of Performance Record Status.

        Attributes:
            leave_request_status (CharField, mandatory): leave_request_status.
            description (TextField, optional) : Description.
    """
    leave_request_status_name = models.CharField(
                                                    max_length=255,
                                                    blank=False,
                                                    null=False,
                                                    verbose_name='Leave request status'
                                                )
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.leave_request_status_name

    class Meta:
        db_table = 'ref_leave_request_status'


class RefLeaveRevisionType(AbstractBaseModel):
    """
        This model provides representation of Performance Record Status.

        Attributes:
            leave_revision_type (CharField, mandatory): leave_revision_type.
            description (TextField, optional) : Description.
    """
    leave_revision_type_name = models.CharField(
                                                    max_length=255,
                                                    blank=False,
                                                    null=False,
                                                    verbose_name='Leave revision type name'
                                               )
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.leave_revision_type_name

    class Meta:
        db_table = 'ref_leave_revision_type'
