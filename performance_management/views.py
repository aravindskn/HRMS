"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/performance_management/views.py
    Description: This module contains all view definitions that are common across the different
    categories of entities in hrms application.
--------------------------------------------------------------------------------------------------
"""

from rest_framework.generics import (
                                        ListAPIView,
                                        ListCreateAPIView,
                                        RetrieveUpdateDestroyAPIView
                                    )
from .models import (PerformanceAssessmentRec,
                     Goals,
                     Milestone)
from .serializers import (PerformanceAssessmentRecSerializer,
                          GoalsSerializer,
                          MilestoneSerializer)
from rest_framework.exceptions import NotFound
from .jsonconstants import (WRONG_EMPLOYEE_ID_ERROR, WRONG_ASSESSMENT_STATUS_ERROR, WRONG_ID_OR_STATUS_ERROR)
from hrms.settings.permissions import PermissionSettings, CustomDjangoModelPermissions


class PerformanceAssessmentRecListCreateView(ListCreateAPIView):
    """
        This view contains the definition for List and Create method of Performance Assessment Records.
    """
    serializer_class = PerformanceAssessmentRecSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        queryset = PerformanceAssessmentRec.objects.all()
        employee_id = self.request.query_params.get('emp_id', None)
        status = self.request.query_params.get('status', None)

        if employee_id is not None and status is not None:
            try:
                status = int(status)
                employee_id = int(employee_id)
                queryset = queryset.filter(deleted_status=False).filter(employee_id=employee_id,
                                                                        assessment_status=status)
                if not queryset:
                    raise NotFound(detail=WRONG_ID_OR_STATUS_ERROR)
            except ValueError:
                raise NotFound(detail=WRONG_ID_OR_STATUS_ERROR)
        elif employee_id is not None:
            try:
                employee_id = int(employee_id)
                queryset = queryset.filter(deleted_status=False).filter(employee_id=employee_id)
                if not queryset:
                    raise NotFound(detail=WRONG_EMPLOYEE_ID_ERROR)
            except ValueError:
                raise NotFound(detail=WRONG_EMPLOYEE_ID_ERROR)
        elif status is not None:
            try:
                status = int(status)
                queryset = queryset.filter(deleted_status=False).filter(assessment_status=status)
                if not queryset:
                    raise NotFound(detail=WRONG_ASSESSMENT_STATUS_ERROR)
            except ValueError:
                raise NotFound(detail=WRONG_ASSESSMENT_STATUS_ERROR)
        else:
            queryset = queryset.filter(deleted_status=False)

        return queryset


class PerformanceAssessmentRecRUDView(RetrieveUpdateDestroyAPIView):
    """
        This view contains the definition for Retrieve, Update and Destroy method of Performance Assessment Records.
    """
    lookup_field = 'id'
    serializer_class = PerformanceAssessmentRecSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return PerformanceAssessmentRec.objects.all()


class GoalsListCreateView(ListCreateAPIView):
    """
        This view contains the definition for List and Create method of Goals.
    """
    lookup_field = 'id'
    serializer_class = GoalsSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Goals.objects.filter(deleted_status=False)


class GoalsRUDView(RetrieveUpdateDestroyAPIView):
    """
        This view contains the definition for Retrieve, Update and Destroy method of Goals.
    """
    lookup_field = 'id'
    serializer_class = GoalsSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Goals.objects.all()


class GoalsListView(ListAPIView):
    """
        This view contains the definition for Listing  all goals related on specific performance assessment.
    """
    lookup_field = 'performance_assessment'
    serializer_class = GoalsSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Goals.objects.filter(deleted_status=False).filter(performance_assessment=self.kwargs.get('performance_assessment'))


class MilestoneListCreateView(ListCreateAPIView):
    """
        This view contains the definition for List and Create method of Milestone.
    """
    lookup_field = 'id'
    serializer_class = MilestoneSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Milestone.objects.filter(deleted_status=False)


class MilestoneRUDView(RetrieveUpdateDestroyAPIView):
    """
        This view contains the definition for Retrieve, Update and Destroy method of Milestone.
    """
    lookup_field = 'id'
    serializer_class = MilestoneSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Milestone.objects.all()


class MilestoneListView(ListAPIView):
    """
        This view contains the definition for Listing  all milestones related on specific goal.
    """
    lookup_field = 'goal'
    serializer_class = MilestoneSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Milestone.objects.filter(deleted_status=False).filter(goal=self.kwargs.get('goal'))

