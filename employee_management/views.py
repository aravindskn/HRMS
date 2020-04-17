"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/employee_management/views.py
    Description: This module contains all view definitions that are common across the different
    categories of entities in hrms application.
--------------------------------------------------------------------------------------------------
"""
from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateDestroyAPIView)

from ref_data_management.models import RefContactType

from .models import (
                        EmployeeAddress,
                        Address,
                        Employee,
                        EmployeeContact,
                        EmploymentDetails
                    )

from .serializers import (
                            EmployeeCompositeCreateSerializer,
                            EmployeeAddressSerializer,
                            AddressSerializer,
                            EmployeeSerializer,
                            EmployeeContactSerializer,
                            EmploymentDetailsSerializer,
                            EmployeeListLevelTenSerializer,
                        )
from hrms.settings.permissions import PermissionSettings, CustomDjangoModelPermissions
from rest_framework.exceptions import NotFound
from .errors import EMPLOYEE_LIST_CREATE_QUERY_STRING_ERROR, EMPLOYEE_RETRIEVE_QUERY_STRING_ERROR, NOT_A_VALID_EMAIL
from django.core.validators import validate_email
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from ref_data_management.serializers import RefDesignation,RefDepartment


class AddressListCreateView(ListCreateAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = AddressSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Address.objects.filter(deleted_status=False)


class AddressRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = AddressSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return Address.objects.all()


class EmployeeAddressListCreateView(ListCreateAPIView):
    """
            This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = EmployeeAddressSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return EmployeeAddress.objects.filter(deleted_status=False)


class EmployeeAddressRUDView(RetrieveUpdateDestroyAPIView):
    """
            This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = EmployeeAddressSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        return EmployeeAddress.objects.all()


class EmployeeContactListCreateView(ListCreateAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = EmployeeContactSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json_data = self.request.data
        contact = RefContactType.objects.filter(id=json_data['contact_type'])
        contact_type = str(contact[0]).upper()
        value = json_data['contact_value']
        contact_value = str(value)
        if contact_type == 'EMAIL':
            try:
                validate_email(contact_value)
            except:
                raise ValidationError(detail=NOT_A_VALID_EMAIL)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return EmployeeContact.objects.filter(deleted_status=False)


class EmployeeContactRUDView(RetrieveUpdateDestroyAPIView):
    """
       This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = EmployeeContactSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def update(self, request, *args, **kwargs):

        json_data = self.request.data
        contact = RefContactType.objects.filter(id=json_data['contact_type'])
        contact_type = str(contact[0]).upper()
        value = json_data['contact_value']
        contact_value = str(value)
        if contact_type == 'EMAIL':
            try:
                validate_email(contact_value)
            except:
                raise ValidationError(detail=NOT_A_VALID_EMAIL)

        return super(EmployeeContactRUDView, self).update(request, *args, **kwargs)

    def get_queryset(self):
        return EmployeeContact.objects.all()

class EmploymentDetailsListCreateView(ListCreateAPIView):
    """
        This module contains the definitions for LIST and CREATE method.
    """
    lookup_field = 'id'
    serializer_class = EmploymentDetailsSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):
        department = self.request.query_params.get('department', None)
        designation = self.request.query_params.get('designation', None)

        if department is not None and designation is None:
            try:
                valid_department = RefDepartment.objects.get(department_name=department)
                department_id = valid_department.id
                queryset = EmploymentDetails.objects.filter(deleted_status=False).filter(department_id=department_id)
            except:
                raise NotFound(detail='Data Not Found')

        elif department is None and designation is not None:
            try:
                valid_designation = RefDesignation.objects.get(designation_name=designation)
                designation_id = valid_designation.id
                queryset = EmploymentDetails.objects.filter(deleted_status=False).filter(department_id=designation_id)
            except:
                raise NotFound(detail='Data Not Found')

        elif department is not None and designation is not None:
            try:
                valid_department = RefDepartment.objects.get(department_name=department)
                valid_designation = RefDesignation.objects.get(designation_name=designation)
                department_id = valid_department.id
                designation_id = valid_designation.id
                queryset = EmploymentDetails.objects.filter(deleted_status=False).filter(
                    department_id=department_id).filter(designation_id=designation_id)
            except:
                raise NotFound(detail='Data Not Found')

        else:
            queryset = EmploymentDetails.objects.filter(deleted_status=False)

        return queryset


class EmploymentDetailsRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = EmploymentDetailsSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_queryset(self):

        return EmploymentDetails.objects.all()


class EmployeeListCreateView(ListCreateAPIView):
    """
            This module contains the definitions for LIST and CREATE method.
            This module lists and creates zero or more EmployeeAddress, EmployeeContacts and EmploymentDetails
    """
    serializer_class = EmployeeSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_serializer_class(self):

        if self.request.method == 'GET':

            enq_level = self.request.query_params.get('enq_lvl_id', '1')

            if enq_level[-1] == '/':
                enq_level = enq_level[:-1]

            try:

                enq_level = int(enq_level)

                if enq_level == 10:
                    serializer_class = EmployeeListLevelTenSerializer
                elif enq_level == 1:
                    serializer_class = EmployeeSerializer
                else:
                    raise NotFound(detail=EMPLOYEE_LIST_CREATE_QUERY_STRING_ERROR)
            except:
                raise NotFound(detail=EMPLOYEE_LIST_CREATE_QUERY_STRING_ERROR)

            return serializer_class

        elif self.request.method == 'POST':

            json_data = self.request.data   # holds the json structure of POST request

            if 'address_list' in json_data or 'employment_details_list' in json_data or 'contact_list' in json_data:
                    serializer_class = EmployeeCompositeCreateSerializer
            else:
                serializer_class = EmployeeSerializer

            return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json_data = self.request.data
        contact_list = json_data['contact_list']

        contact_list_length = len(contact_list)
        for i in range(contact_list_length):

            contact = RefContactType.objects.filter(id=contact_list[i]['contact_type'])

            contact_type = str(contact[0]).upper()

            value = contact_list[i]['contact_value']
            contact_value = str(value).upper()

            if contact_type == 'EMAIL':
                try:
                    validate_email(contact_value)
                except:
                    raise ValidationError(detail=NOT_A_VALID_EMAIL)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name', None)
        if first_name is not None:
            try:
                queryset = Employee.objects.filter(first_name=first_name)
            except:
                raise NotFound(detail='Data Not Found')
        else:
            queryset = Employee.objects.filter(deleted_status=False)
        return queryset


class EmployeeRUDView(RetrieveUpdateDestroyAPIView):
    """
            This module contains the definitions for RETRIEVE, UPDATE and DESTROY methods.
    """
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    permission_classes = (PermissionSettings.IS_AUTHENTICATED, CustomDjangoModelPermissions)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            enq_lvl_id = self.request.query_params.get('enq_lvl_id', '1')

            if enq_lvl_id[-1] == '/':
                enq_lvl_id = enq_lvl_id[:-1]

            try:
                enq_lvl_id = int(enq_lvl_id)

                if enq_lvl_id == 10:
                    serializer_class = EmployeeListLevelTenSerializer
                elif enq_lvl_id == 1:
                    serializer_class = EmployeeSerializer
                else:
                    raise NotFound(detail=EMPLOYEE_RETRIEVE_QUERY_STRING_ERROR)

            except:
                raise NotFound(detail=EMPLOYEE_RETRIEVE_QUERY_STRING_ERROR)

            return serializer_class
        else:
            return EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

