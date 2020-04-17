"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/performance_management/serializers.py
    Description: This module contains all serializer definitions that are common across the different
    categories of entities in hrms application.
--------------------------------------------------------------------------------------------------
"""
from rest_framework import serializers
from .models import (PerformanceAssessmentRec,
                     Goals,
                     Milestone)
from .jsonconstants import (EMPLOYEE_ID,
                            ASSESSMENT_STATUS,
                            TARGET_UNIT,
                            SELF_RATING_SCALE,
                            MANAGER_RATING_SCALE,
                            GOAL)


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


class PerformanceAssessmentRecSerializer(AbstractBaseSerializer):
    """
        This module contains the serializer definition for PerformanceAssessmentRec Model.
    """
    employee_name = serializers.StringRelatedField(source=EMPLOYEE_ID, read_only=True)
    assessment_status_name = serializers.StringRelatedField(source=ASSESSMENT_STATUS, read_only=True)

    class Meta:
        model = PerformanceAssessmentRec
        fields = [
                    'id',
                    'employee_id',
                    'employee_name',
                    'assessment_year',
                    'assessment_status',
                    'assessment_status_name',
                    'overall_manager_comment',
                    'overall_hod_comment',
                    'overall_employee_comment'
                 ] + AbstractBaseSerializer.Meta.fields


class GoalsSerializer(AbstractBaseSerializer):
    """
        This module contains the serializer definition for Goals Model.
    """
    target_unit_name = serializers.StringRelatedField(source=TARGET_UNIT, read_only=True)
    self_rating_scale_name = serializers.StringRelatedField(source=SELF_RATING_SCALE, read_only=True)
    manager_rating_scale_name = serializers.StringRelatedField(source=MANAGER_RATING_SCALE, read_only=True)

    class Meta:
        model = Goals
        fields = [
                    'id',
                    'description',
                    'weightage',
                    'target_value',
                    'target_completion_date',
                    'target_achieved_value',
                    'manager_comment',
                    'achievment_comment',
                    'performance_assessment',
                    'target_unit',
                    'target_unit_name',
                    'self_rating_scale',
                    'self_rating_scale_name',
                    'manager_rating_scale',
                    'manager_rating_scale_name'
                ] + AbstractBaseSerializer.Meta.fields


class MilestoneSerializer(AbstractBaseSerializer):
    """
        This module contains the serializer definition for Milestone Model.
    """
    goal_name = serializers.StringRelatedField(source=GOAL, read_only=True)

    class Meta:
        model = Milestone
        fields = [
                    'id',
                    'description',
                    'target_value',
                    'target_completion_date',
                    'achieved_target_value',
                    'goal',
                    'goal_name'
                 ] + AbstractBaseSerializer.Meta.fields

