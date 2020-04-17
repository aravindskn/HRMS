"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/ref_data_management/serializers.py
    Description: This module contains all API endpoints for the ref_data_management application.
--------------------------------------------------------------------------------------------------
"""
from rest_framework import serializers
from .models import (
                        RefCountry,
                        RefStateProvince,
                        RefMaritalStatus,
                        RefContactType,
                        RefAddressType,
                        RefGender,
                        RefDepartment,
                        RefDesignation,
                        RefPerformanceRecStatus,
                        RefRatingScale,
                        RefTargetUnit,
                        RefLeaveType,
                        RefLeaveRequestStatus,
                        RefLeaveRevisionType
                    )


class AbstractBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = \
          [
            'created_by',
            'last_updated_by',
            'deleted_status',
            'created_date',
            'deleted_date',
            'created_date',
            'last_updated_date'
           ]


class RefCountrySerializer(AbstractBaseSerializer):
    """
        This module has the attributes of 'Country' model
    """
    class Meta:
        model = RefCountry
        fields = \
            [
                'id',
                'country_name',
                'country_iso_code',
                'country_code',
            ] + AbstractBaseSerializer.Meta.fields


class RefStateProvinceSerializer(AbstractBaseSerializer):
    """
        This module has the attributes of 'state' model
    """
    country_name = serializers.StringRelatedField(source='country', read_only=True)

    class Meta:
        model = RefStateProvince
        fields = \
            [
                'id',
                'state_name',
                'state_code',
                'country',
                'country_name'
            ] + AbstractBaseSerializer.Meta.fields


class RefMaritalStatusSerializer(AbstractBaseSerializer):
    """
        This module contains the serializer for the Marital Status Model.
    """

    class Meta:
            model = RefMaritalStatus
            fields = \
                [
                    'id',
                    'marital_status',
                    'description'
                ] + AbstractBaseSerializer.Meta.fields


class RefContactTypeSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Employee Contact type model
    """
    class Meta:
        model = RefContactType
        fields = \
            [
                'id',
                'contact_type',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefAddressTypeSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Employee Address type model
    """
    class Meta:
        model = RefAddressType
        fields =\
            [
                'id',
                'address_type',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefGenderSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Gender model
    """
    class Meta:
        model = RefGender
        fields = \
            [
                'id',
                'gender_type',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefDepartmentSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Department model
    """
    class Meta:
        model = RefDepartment
        fields = \
            [
                'id',
                'department_name',
                'department_code',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefDesignationSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Designation model
    """
    class Meta:
        model = RefDesignation
        fields = \
            [
                'id',
                'designation_name',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefTargetUnitSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Target Unit model.
    """
    class Meta:
        model = RefTargetUnit
        fields = [
                    'id',
                    'target_unit',
                 ] + AbstractBaseSerializer.Meta.fields


class RefPerformanceRecStatusSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Performance Record Status model.
    """
    class Meta:
        model = RefPerformanceRecStatus
        fields = [
                    'id',
                    'status_name',
                    'description'
                 ] + AbstractBaseSerializer.Meta.fields


class RefRatingScaleSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for Rating Scale model.
    """

    class Meta:
        model = RefRatingScale
        fields = [
                     'id',
                     'rating_value',
                     'description'
                 ] + AbstractBaseSerializer.Meta.fields


class RefLeaveTypeSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for LEAVE TYPE model
    """
    class Meta:
        model = RefLeaveType
        fields = \
            [
                'id',
                'leave_type_name',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefLeaveRequestStatusSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for lEAVE REQUEST STATUS model
    """

    class Meta:
        model = RefLeaveRequestStatus
        fields = \
            [
                'id',
                'leave_request_status_name',
                'description'
            ] + AbstractBaseSerializer.Meta.fields


class RefLeaveRevisionTypeSerializer(AbstractBaseSerializer):
    """
        This model contains the serializer for lEAVE REVISION TYPE model
    """

    class Meta:
        model = RefLeaveRevisionType
        fields = \
            [
                'id',
                'leave_revision_type_name',
                'description'
            ] + AbstractBaseSerializer.Meta.fields

