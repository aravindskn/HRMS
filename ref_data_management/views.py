"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/ref_data_management/views.py
    Description: This module contains all view definition for the ref_data_management application.
--------------------------------------------------------------------------------------------------
"""
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

from rest_framework.generics import \
    (
        ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
    )
from .serializers import (
                            RefCountrySerializer,
                            RefStateProvinceSerializer,
                            RefMaritalStatusSerializer,
                            RefContactTypeSerializer,
                            RefAddressTypeSerializer,
                            RefGenderSerializer,
                            RefDepartmentSerializer,
                            RefDesignationSerializer,
                            RefPerformanceRecStatusSerializer,
                            RefRatingScaleSerializer,
                            RefTargetUnitSerializer,
                            RefLeaveTypeSerializer,
                            RefLeaveRequestStatusSerializer,
                            RefLeaveRevisionTypeSerializer
                         )

from hrms.settings.permissions import PermissionSettings, CustomDjangoModelPermissions


class RefCountryListCreateView(ListCreateAPIView):
    """
        This module creates the POST method for Country Model
    """

    lookup_field = 'id'
    serializer_class = RefCountrySerializer
    pagination_class = None
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefCountry.objects.filter(deleted_status=False)


class RefStateListView(ListAPIView):
    """
                This module creates the LIST method for Country Model with its respective states.
    """
    lookup_field = 'country'
    serializer_class = RefStateProvinceSerializer
    pagination_class = None
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefStateProvince.objects.filter(deleted_status=False).filter(country=self.kwargs.get('country'))


class RefCountryRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module creates the RETRIEVE, UPDATE, DESTROY method for Country Model
    """

    lookup_field = 'id'
    serializer_class = RefCountrySerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefCountry.objects.all()


class RefStateProvinceListCreateView(ListCreateAPIView):
    """
        This module creates the POST method for State Model
    """

    lookup_field = 'id'
    serializer_class = RefStateProvinceSerializer
    pagination_class = None
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefStateProvince.objects.filter(deleted_status=False)


class RefStateProvinceRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module creates the RETRIEVE, UPDATE, DESTROY method for Country Model
    """

    lookup_field = 'id'
    serializer_class = RefStateProvinceSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefStateProvince.objects.all()


class RefMaritalStatusListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST,CREATE operation for the Designation Model.
    """
    lookup_field = 'id'
    serializer_class = RefMaritalStatusSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefMaritalStatus.objects.filter(deleted_status=False)


class RefMaritalStatusRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE,PUT,DELETE operation for the Designation Model.
    """
    lookup_field = 'id'
    serializer_class = RefMaritalStatusSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefMaritalStatus.objects.all()


class RefContactTypeListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the CONTACT TYPE Model.
    """
    lookup_field = 'id'
    serializer_class = RefContactTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefContactType.objects.filter(deleted_status=False)


class RefContactTypeRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the CONTACT TYPE Model.
    """
    lookup_field = 'id'
    serializer_class = RefContactTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefContactType.objects.all()


class RefAddressTypeListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the ADDRESS TYPE Model.
    """
    lookup_field = 'id'
    serializer_class = RefAddressTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefAddressType.objects.filter(deleted_status=False)


class RefAddressTypeRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the ADDRESS TYPE Model.
    """
    lookup_field = 'id'
    serializer_class = RefAddressTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefAddressType.objects.all()


class RefGenderListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the GENDER Model.
    """
    lookup_field = 'id'
    serializer_class = RefGenderSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefGender.objects.filter(deleted_status=False)


class RefGenderRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the GENDER Model.
    """
    lookup_field = 'id'
    serializer_class = RefGenderSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefGender.objects.all()


class RefDepartmentListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the DEPARTMENT Model.
    """
    lookup_field = 'id'
    serializer_class = RefDepartmentSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefDepartment.objects.filter(deleted_status=False)


class RefDepartmentRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the DEPARTMENT Model.

    """
    lookup_field = 'id'
    serializer_class = RefDepartmentSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefDepartment.objects.all()


class RefDesignationListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the DESIGNATION Model.
    """
    lookup_field = 'id'
    serializer_class = RefDesignationSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefDesignation.objects.filter(deleted_status=False)


class RefDesignationRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the DESIGNATION Model.
    """
    lookup_field = 'id'
    serializer_class = RefDesignationSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefDesignation.objects.all()


class RefTargetUnitListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the Target Unit Model.
    """
    lookup_field = 'id'
    serializer_class = RefTargetUnitSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefTargetUnit.objects.filter(deleted_status=False)


class RefTargetUnitRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the Target Unit Model.
    """
    lookup_field = 'id'
    serializer_class = RefTargetUnitSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefTargetUnit.objects.all()


class RefPerformanceRecStatusListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the PERFORMANCE RECORD STATUS Model.
    """
    lookup_field = 'id'
    serializer_class = RefPerformanceRecStatusSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefPerformanceRecStatus.objects.filter(deleted_status=False)


class RefPerformanceRecStatusRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the PERFORMANCE RECORD STATUS Model.
    """
    lookup_field = 'id'
    serializer_class = RefPerformanceRecStatusSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefPerformanceRecStatus.objects.all()


class RefRatingScaleListCreateView(ListCreateAPIView):
    """
        This module contains the definition for LIST, CREATE operation for the Rating Scale Model.
    """
    lookup_field = 'id'
    serializer_class = RefRatingScaleSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefRatingScale.objects.filter(deleted_status=False)


class RefRatingScaleRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for the Rating Scale Model.
    """
    lookup_field = 'id'
    serializer_class = RefRatingScaleSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefRatingScale.objects.all()


class RefLeaveTypeListCreateView(ListCreateAPIView):
    """
        This module contains the definition for CREATE and LIST operation for LEAVE TYPE MODEL
    """
    lookup_field = 'id'
    serializer_class = RefLeaveTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefLeaveType.objects.filter(deleted_status=False)


class RefLeaveTypeRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for LEAVE TYPE MODEL
    """
    lookup_field = 'id'
    serializer_class = RefLeaveTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefLeaveType.objects.all()


class RefLeaveRequestStatusListCreateView(ListCreateAPIView):
    """
        This module contains the definition for CREATE and LIST operation for LEAVE REQUEST STATUS MODEL
    """
    lookup_field = 'id'
    serializer_class = RefLeaveRequestStatusSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefLeaveRequestStatus.objects.filter(deleted_status=False)


class RefLeaveRequestStatusRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for LEAVE REQUEST STATUS MODEL
    """
    lookup_field = 'id'
    serializer_class = RefLeaveRequestStatusSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefLeaveRequestStatus.objects.all()


class RefLeaveRevisionTypeListCreateView(ListCreateAPIView):
    """
        This module contains the definition for CREATE and LIST operation for LEAVE REVISION TYPE MODEL
    """
    lookup_field = 'id'
    serializer_class = RefLeaveRevisionTypeSerializer
    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefLeaveRevisionType.objects.filter(deleted_status=False)


class RefLeaveRevisionTypeRUDView(RetrieveUpdateDestroyAPIView):
    """
        This module contains the definition for RETRIEVE, UPDATE AND DELETE operation for LEAVE REVISION TYPE MODEL
    """
    lookup_field = 'id'
    serializer_class = RefLeaveRevisionTypeSerializer

    permission_classes = (PermissionSettings.IS_ADMIN_OR_READ_ONLY, CustomDjangoModelPermissions)

    def get_queryset(self):
        return RefLeaveRevisionType.objects.all()
