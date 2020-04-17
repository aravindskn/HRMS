from rest_framework import serializers
from .models import (
                        LeaveEligibility,
                        LeaveRevision,
                        LeaveRequest
                    )

from .json_constants import (
                                LEAVE_TYPE,
                                EMPLOYEE,
                                NUMBER_OF_DAYS,
                                REQUEST_STATUS,
                                REVISION_TYPE
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
        fields = \
            [
                'created_by',
                'last_updated_by',
                'deleted_status',
                'last_updated_date',
                'deleted_date',
                'created_date'
            ]


class LeaveRevisionSerializer(AbstractBaseSerializer):
    """
        Serializer for Leave Revision
        Fields Serialized : id, number_of_days, leave_type, revision_type
    """
    leave_type_name = serializers.StringRelatedField(source=LEAVE_TYPE, read_only=True)
    revision_type_name = serializers.StringRelatedField(source=REVISION_TYPE, read_only=True)

    class Meta:
        model = LeaveRevision
        fields = \
            [
                'id',
                'leave_type',
                'leave_type_name',
                'number_of_days',
                'revision_type',
                'revision_type_name'
            ] + AbstractBaseSerializer.Meta.fields


class LeaveEligibilitySerializer(AbstractBaseSerializer):
    """
        Serializer for Leave Eligibility
        Fields Serialized : id, employee_name, leave_type_id and leave_type_name
    """
    leave_type_name = serializers.StringRelatedField(source=LEAVE_TYPE, read_only=True)
    employee_name = serializers.StringRelatedField(source=EMPLOYEE, read_only=True)
    number_of_days_value = serializers.StringRelatedField(source=NUMBER_OF_DAYS, read_only=True)

    class Meta:
        model = LeaveEligibility
        fields = \
            [
                'id',
                'employee',
                'employee_name',
                'number_of_days',
                'number_of_days_value',
                'leave_type',
                'leave_type_name',
            ] + AbstractBaseSerializer.Meta.fields


class LeaveRequestSerializer(AbstractBaseSerializer):
    """
        serializer for leave request
        Fields serialized : id, employee, employee_name, leave_type, leave_start_date, leave_end_date, comments
                            leave_request_status
    """
    leave_type_name = serializers.StringRelatedField(source=LEAVE_TYPE, read_only=True)
    employee_name = serializers.StringRelatedField(source=EMPLOYEE, read_only=True)
    request_status_name = serializers.StringRelatedField(source=REQUEST_STATUS, read_only=True)

    class Meta:
        model = LeaveRequest
        fields = \
            [
                'id',
                'employee',
                'employee_name',
                'leave_type',
                'leave_type_name',
                'leave_start_date',
                'leave_end_date',
                'comments',
                'request_status',
                'request_status_name',
            ] + AbstractBaseSerializer.Meta.fields
