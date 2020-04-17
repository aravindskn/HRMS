"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/ref_data_managementurls.py
    Description: This module contains all API endpoints for the ref_data_management application.
--------------------------------------------------------------------------------------------------
"""
from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.RefCountryListCreateView.as_view()),  # Endpoint for COUNTRY LIST and CREATE methods.
    path('countries/<int:id>/', views.RefCountryRUDView.as_view()),    # Endpoint for COUNTRY's RETRIVE, UPDATE AND DELETE methods.
    path('countries/<int:country>/states/', views.RefStateListView.as_view()),  # Endpoint for Listing the states of a Country.
    path('states/', views.RefStateProvinceListCreateView.as_view()),   # Endpoint for STATES LIST and CREATE methods.
    path('states/<int:id>/', views.RefStateProvinceRUDView.as_view()),   # Endpoint for STATE's RETRIVE, UPDATE AND DELETE methods.
    path('maritalstatus/', views.RefMaritalStatusListCreateView.as_view()),# Endpoint for Marital Status LIST and CREATE methods.
    path('maritalstatus/<int:id>/', views.RefMaritalStatusRUDView.as_view()),# Endpoint for Marital Status RETRIEVE, UPDATE and DESTROY methods.
    path('contacttype/', views.RefContactTypeListCreateView.as_view()),# Endpoint for CONTACT TYPE's, RETRIEVE, UPDATE and DESTROY methods.
    path('contacttype/<int:id>/',views.RefContactTypeRUDView.as_view()),# Endpoint for CONTACT TYPE's, RETRIEVE, UPDATE and DESTROY methods.
    path('addresstype/',views.RefAddressTypeListCreateView.as_view()),# Endpoint for ADDRESS TYPE's, RETRIEVE, UPDATE and DESTROY methods.
    path('addresstype/<int:id>/',views.RefAddressTypeRUDView.as_view()),# Endpoint for ADDRESS TYPE's, RETRIEVE, UPDATE and DESTROY methods.
    path('gender/', views.RefGenderListCreateView.as_view()),# Endpoint for GENDER's, RETRIEVE, UPDATE and DESTROY methods.
    path('gender/<int:id>/', views.RefGenderRUDView.as_view()),# Endpoint for GENDER's RETRIEVE, UPDATE and DESTROY methods.
    path('departments/', views.RefDepartmentListCreateView.as_view()),# Endpoint for DEPARTMENTS's RETRIEVE, UPDATE and DESTROY methods.
    path('departments/<int:id>/', views.RefDepartmentRUDView.as_view()),# Endpoint for DEPARTMENTS's RETRIEVE, UPDATE and DESTROY methods.
    path('designations/', views.RefDesignationListCreateView.as_view()),# Endpoint for DESIGNATION's RETRIEVE, UPDATE and DESTROY methods.
    path('designations/<int:id>/', views.RefDesignationRUDView.as_view()),# Endpoint for DESIGNATION's RETRIEVE, UPDATE and DESTROY methods.
    path('targetunits/', views.RefTargetUnitListCreateView.as_view()),  # Endpoint for Target Unit LIST and CREATE methods.
    path('targetunits/<int:id>/', views.RefTargetUnitRUDView.as_view()),    # Endpoint for Target Unit RETRIEVE, UPDATE and DESTROY methods.
    path('performancerecstatus/', views.RefPerformanceRecStatusListCreateView.as_view()),   # Endpoint for Performace Record Status LIST and CREATE methods.
    path('performancerecstatus/<int:id>/', views.RefPerformanceRecStatusRUDView.as_view()),  # Endpoint for Performace Record Status RETRIEVE, UPDATE and DESTROY methods.
    path('ratingscale/', views.RefRatingScaleListCreateView.as_view()),   # Endpoint for Rating Scale LIST and CREATE methods.
    path('ratingscale/<int:id>/', views.RefRatingScaleRUDView.as_view()),  # Endpoint for Rating Scale RETRIEVE, UPDATE and DESTROY methods.

    path('leavetypes/', views.RefLeaveTypeListCreateView.as_view()),
    # EndPoint for LeaveType's List Create methods

    path('leavetypes/<int:id>/', views.RefLeaveTypeRUDView.as_view()),
    # EndPoint for LeaveType's Retrieve Update Destroy methods

    path('leaverequeststatus/', views.RefLeaveRequestStatusListCreateView.as_view()),
    # EndPoint for LeaveType's List Create methods

    path('leaverequeststatus/<int:id>/', views.RefLeaveRequestStatusRUDView.as_view()),
    # EndPoint for LeaveType's Retrieve Update Destroy methods

    path('leaverevisiontypes/', views.RefLeaveRevisionTypeListCreateView.as_view()),
    # EndPoint for LeaveType's List Create methods

    path('leaverevisiontypes/<int:id>/', views.RefLeaveRevisionTypeRUDView.as_view())
    # EndPoint for LeaveType's Retrieve Update Destroy methods
]