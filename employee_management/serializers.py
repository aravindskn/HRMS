"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/employee_management/serializers.py
    Description: This module contains all serializer definitions that are common across the different
    categories of entities in hrms application.
--------------------------------------------------------------------------------------------------
"""

from rest_framework import serializers
from .models import (
                                        EmployeeAddress,
                                        Address,
                                        Employee,
                                        EmployeeContact,
                                        EmploymentDetails)

from .constants import (
                            ADDRESS,
                            ADDRESS_TYPE,
                            ADDRESSES,
                            CONTACTS,
                            EMPLOYMENT_DETAILS,
                            DEPARTMENT,
                            DESIGNATION,
                            EMPLOYEE,
                            STATE_PROVINCE,
                            COUNTRY,
                            CONTACT_TYPE,
                            MARITAL_STATUS,
                            GENDER
                     )


class AbstractBaseSerializer(serializers.ModelSerializer):
    """
                    This Module contains the serializer for the AbstractBase Model.
                    Fields Serialized:
                            id: The ID for the abstract model.
                            created_by: Name of the user who created the entry.
                            last_updated_by: Name of the user who last updated the the data.
                            deleted_status: Status of the data, whether it is deleted or not.
    """

    class Meta:
        fields = ['created_by',
                  'last_updated_by',
                  'deleted_status',
                  'last_updated_date',
                  'deleted_date',
                  'created_date']


class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(deleted_status=False)
        return super(FilteredListSerializer, self).to_representation(data)


class EmployeeAddressSerializer(AbstractBaseSerializer):
    """
        The serializer for employee address model.
    """
    employee_id = serializers.StringRelatedField(source=EMPLOYEE, read_only=True)
    address_type_name = serializers.StringRelatedField(source=ADDRESS_TYPE, read_only=True)
    addresses = serializers.StringRelatedField(source=ADDRESS, read_only=True)

    class Meta:
        model = EmployeeAddress
        fields = ['id',
                  'address_type',
                  'address',
                  'address_type_name',
                  'addresses',
                  'employee',
                  'employee_id'] + AbstractBaseSerializer.Meta.fields


class AddressSerializer(AbstractBaseSerializer):
    """
        The serializer for address model.
    """
    state_name = serializers.StringRelatedField(source=STATE_PROVINCE, read_only=True)
    country_name = serializers.StringRelatedField(source=COUNTRY, read_only=True)

    class Meta:
        model = Address
        fields = ['id',
                  'addr_line_one',
                  'addr_line_two',
                  'addr_line_three',
                  'locality',
                  'city',
                  'state_province',
                  'state_name',
                  'country',
                  'country_name',
                  'postal_code'] + AbstractBaseSerializer.Meta.fields


class EmploymentDetailsSerializer(AbstractBaseSerializer):
    """
            The serializer for employment details model.
    """
    employee_id = serializers.StringRelatedField(source=EMPLOYEE, read_only=True)
    department_name = serializers.StringRelatedField(source=DEPARTMENT, read_only=True)
    designation_name = serializers.StringRelatedField(source=DESIGNATION, read_only=True)

    class Meta:
        model = EmploymentDetails
        fields = \
        [
            'id',
            'employee',
            'employee_id',
            'employment_start_date',
            'department',
            'department_name',
            'designation',
            'designation_name',
            'employment_end_date'
        ] + AbstractBaseSerializer.Meta.fields


class EmployeeContactSerializer(AbstractBaseSerializer):
    """
            The serializer for employee contact model.
    """
    contact_type_name = serializers.StringRelatedField(source=CONTACT_TYPE, read_only=True)
    employee_id = serializers.StringRelatedField(source=EMPLOYEE, read_only=True)

    class Meta:
        model = EmployeeContact
        fields = \
        [
            'id',
            'employee',
            'employee_id',
            'contact_value',
            'contact_type',
            'contact_type_name'
        ] + AbstractBaseSerializer.Meta.fields


class EmployeeSerializer(AbstractBaseSerializer):
    """
        The serializer for employee model.
    """
    marital_status_name = serializers.StringRelatedField(source=MARITAL_STATUS, read_only=True)
    gender_name = serializers.StringRelatedField(source=GENDER, read_only=True)

    class Meta:
        model = Employee
        fields = ['id',
                  'employee_id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'date_of_birth',
                  'marital_status',
                  'marital_status_name',
                  'gender',
                  'gender_name',
                  ] + AbstractBaseSerializer.Meta.fields


class EmployeeAddressListSerializer(AbstractBaseSerializer):
    """
        Serializer for listing Employee Address only
    """
    address_type_name = serializers.StringRelatedField(source=ADDRESS_TYPE, read_only=True)
    address = AddressSerializer()

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = EmployeeAddress
        fields = [
                    'id',
                    'address_type',
                    'address_type_name',
                    'address',
                    'deleted_status'
                 ]


class EmployeeContactListSerializer(AbstractBaseSerializer):
    """
        Serializer for listing Employee Contact only
    """
    contact_type_name = serializers.StringRelatedField(source=CONTACT_TYPE, read_only=True)

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = EmployeeContact
        fields = [
                    'id',
                    'contact_type',
                    'contact_type_name',
                    'contact_value',
                    'deleted_status'
                 ]


class EmploymentDetailsListSerializer(AbstractBaseSerializer):
    """
        Serializer for listing Employment Details only
    """
    department_name = serializers.StringRelatedField(source=DEPARTMENT, read_only=True)
    designation_name = serializers.StringRelatedField(source=DESIGNATION, read_only=True)

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = EmploymentDetails
        fields = [
                    'id',
                    'department',
                    'department_name',
                    'designation',
                    'designation_name',
                    'employment_start_date',
                    'employment_end_date',
                    'deleted_status'
                 ]


class EmployeeListLevelTenSerializer(AbstractBaseSerializer):
    """
        The serializer for employee model.
    """

    marital_status_name = serializers.StringRelatedField(source=MARITAL_STATUS, read_only=True)
    gender_name = serializers.StringRelatedField(source=GENDER, read_only=True)

    address_list = EmployeeAddressListSerializer(many=True, source=ADDRESSES)
    contact_list = EmployeeContactListSerializer(many=True, source=CONTACTS)
    employment_details_list = EmploymentDetailsListSerializer(many=True, source=EMPLOYMENT_DETAILS)

    class Meta:
        model = Employee
        fields = ['id',
                  'employee_id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'date_of_birth',
                  'marital_status',
                  'marital_status_name',
                  'gender',
                  'gender_name',
                  'address_list',
                  'contact_list',
                  'employment_details_list'
                  ] + AbstractBaseSerializer.Meta.fields


class EmployeeContactCompositeCreateSerializer(AbstractBaseSerializer):
    """
        Serializer for listing Employee Contact only
    """
    contact_type_name = serializers.StringRelatedField(source=CONTACT_TYPE, read_only=True)

    class Meta:
        model = EmployeeContact
        fields = [
                    'contact_type',
                    'contact_type_name',
                    'contact_value'
                 ] + AbstractBaseSerializer.Meta.fields


class EmploymentDetailsCompositeCreateSerializer(AbstractBaseSerializer):
    """
        Serializer for listing Employment Details only
    """
    department_name = serializers.StringRelatedField(source=DEPARTMENT, read_only=True)
    designation_name = serializers.StringRelatedField(source=DESIGNATION, read_only=True)

    class Meta:
        model = EmploymentDetails
        fields = [
                    'department',
                    'department_name',
                    'designation',
                    'designation_name',
                    'employment_start_date',
                    'employment_end_date'
                 ] + AbstractBaseSerializer.Meta.fields


class EmployeeCompositeCreateSerializer(AbstractBaseSerializer):
    """
        serializer for creating an employee with zero or more employee_address, employee_contact and employment_details
    """
    address_list = EmployeeAddressListSerializer(source=ADDRESSES, many=True)
    contact_list = EmployeeContactCompositeCreateSerializer(source=CONTACTS, many=True)
    employment_details_list = EmploymentDetailsCompositeCreateSerializer(source=EMPLOYMENT_DETAILS, many=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'employee_id',
            'first_name',
            'middle_name',
            'date_of_birth',
            'last_name',
            'gender',
            'marital_status',
            'address_list',
            'contact_list',
            'employment_details_list'
        ] + AbstractBaseSerializer.Meta.fields

    def create(self, validated_data):

        address_data = validated_data.pop(ADDRESSES)
        contact_data = validated_data.pop(CONTACTS)
        employment_details_data = validated_data.pop(EMPLOYMENT_DETAILS)

        employee = Employee.objects.create(**validated_data)

        address_data_length = len(address_data)
        contact_data_length = len(contact_data)
        employment_details_data_length = len(employment_details_data)

        if address_data_length != 0:

            for temp in range(len(address_data)):
                address_field = address_data[temp][ADDRESS]
                address_type_id = address_data[temp][ADDRESS_TYPE]

                address_list = []
                address_list.append(address_field)

                for data in address_list:
                    address = Address.objects.create(**data)

                EmployeeAddress.objects.create(address_type=address_type_id, employee_id=employee.id,
                                               address_id=address.id)


        if contact_data_length != 0:

            for data in contact_data:
                EmployeeContact.objects.create(**data, employee_id=employee.id)

        if employment_details_data_length != 0:

            for data in employment_details_data:
                EmploymentDetails.objects.create(**data, employee_id=employee.id)

        return employee

