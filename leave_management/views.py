from .models import (
                        LeaveEligibility,
                        LeaveRevision,
                        LeaveRequest
                    )

from employee_management.models import Employee

from .serializers import (
                            LeaveEligibilitySerializer,
                            LeaveRevisionSerializer,
                            LeaveRequestSerializer
                         )

from hrms.settings.permissions import PermissionSettings, CustomDjangoModelPermissions

from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateDestroyAPIView
                                    )

from rest_framework.exceptions import NotFound

from .errors import (
                        INVALID_DATE_FORMAT,
                        MISSING_START_DATE,
                        INVALID_EMP_ID_OR_DATE,
                        INVALID_EMP_ID
                    )

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist


class LeaveEligibilityListCreateView(ListCreateAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = LeaveEligibilitySerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):

        emp_id = self.request.query_params.get('emp_id', None)
        choice = self.request.query_params.get('include_availability', None)
        if emp_id is not None and choice == 'y':

            try:
                validate_employee = Employee.objects.get(employee_id=emp_id)

                query_set = LeaveEligibility.objects.filter(deleted_status=False, employee_id=validate_employee)
            except ObjectDoesNotExist:
                raise NotFound(detail=INVALID_EMP_ID)

        elif emp_id is not None and (choice != 'y' or choice is None):

            try:
                validate_employee = Employee.objects.get(employee_id=emp_id)

                query_set = LeaveEligibility.objects.filter(deleted_status=False, employee_id=validate_employee)
            except ObjectDoesNotExist:
                raise NotFound(detail=INVALID_EMP_ID)

        else:
            query_set = LeaveEligibility.objects.filter(deleted_status=False)

        return query_set


class LeaveEligibilityRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = LeaveEligibilitySerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return LeaveEligibility.objects.all()


class LeaveRevisionListCreateView(ListCreateAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = LeaveRevisionSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return LeaveRevision.objects.filter(deleted_status=False)


class LeaveRevisionRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = LeaveRevisionSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return LeaveRevision.objects.all()


class LeaveRequestListCreateView(ListCreateAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = LeaveRequestSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        emp_id = self.request.query_params.get('emp_id', None)

        if emp_id is None and start_date is None and end_date is None:
            query_set = LeaveRequest.objects.filter(deleted_status=False)

        elif emp_id is not None:

            if start_date is None and end_date is None:
                try:
                    validate_employee = Employee.objects.get(employee_id=emp_id)

                    query_set = LeaveRequest.objects.filter \
                        (
                            deleted_status=False,
                            employee_id=validate_employee
                        )
                except ObjectDoesNotExist:
                    raise NotFound(detail=INVALID_EMP_ID)

            elif start_date is not None and end_date is not None:
                try:
                    validate_start_date = datetime.strptime(start_date, '%Y%m%d')
                    validate_start_date = datetime.date(validate_start_date)

                    validate_end_date = datetime.strptime(end_date, '%Y%m%d')
                    validate_end_date = datetime.date(validate_end_date)

                    try:
                        validate_employee = Employee.objects.get(employee_id=emp_id)

                        query_set = LeaveRequest.objects.filter\
                            (
                                deleted_status=False,
                                employee_id=validate_employee,
                                leave_start_date__gte=validate_start_date,
                                leave_end_date__lte=validate_end_date
                            )
                    except ObjectDoesNotExist:
                        raise NotFound(detail=INVALID_EMP_ID_OR_DATE)
                except:
                    raise NotFound(detail=INVALID_EMP_ID_OR_DATE)

            elif start_date is not None:

                if start_date is not None:
                    try:
                        validate_start_date = datetime.strptime(start_date, '%Y%m%d')
                        validate_start_date = datetime.date(validate_start_date)

                        try:
                            validate_employee = Employee.objects.get(employee_id=emp_id)

                            query_set = LeaveRequest.objects.filter\
                                (
                                    deleted_status=False,
                                    employee_id=validate_employee,
                                    leave_start_date__gte=validate_start_date
                                )
                        except ObjectDoesNotExist:
                            raise NotFound(detail=INVALID_EMP_ID_OR_DATE)
                    except:
                        raise NotFound(detail=INVALID_EMP_ID_OR_DATE)

        elif emp_id is None:

            if start_date is None and end_date is not None:
                raise NotFound(detail=MISSING_START_DATE)

            elif start_date is not None and end_date is not None:

                try:
                    validate_start_date = datetime.strptime(start_date, '%Y%m%d')
                    validate_start_date = datetime.date(validate_start_date)

                    validate_end_date = datetime.strptime(end_date, '%Y%m%d')
                    validate_end_date = datetime.date(validate_end_date)

                    query_set = LeaveRequest.objects.filter\
                        (
                            deleted_status=False,
                            leave_start_date__gte=validate_start_date,
                            leave_end_date__lte=validate_end_date
                        )

                except ValueError:
                    raise NotFound(detail=INVALID_DATE_FORMAT)

            elif start_date is not None:
                try:
                    validate_start_date = datetime.strptime(start_date, '%Y%m%d')
                    validate_start_date = datetime.date(validate_start_date)

                    query_set = LeaveRequest.objects.filter\
                            (
                                deleted_status=False,
                                leave_start_date__gte=validate_start_date
                            )
                except ValueError:
                    raise NotFound(detail=INVALID_EMP_ID_OR_DATE)

        return query_set


class LeaveRequestRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = LeaveRequestSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return LeaveRequest.objects.all()

