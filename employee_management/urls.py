"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/employee_management/urls.py
    Description: This module contains all API endpoints for the employee_management application.
--------------------------------------------------------------------------------------------------
"""

from django.urls import path
from . import views

urlpatterns = [
    path('addresses/', views.AddressListCreateView.as_view()),                  # End Point for List and Create method.
    path('addresses/<int:id>/', views.AddressRUDView.as_view()),                # Endpoint for Retrieve, Update and Delete.
    path('employeeaddresses/', views.EmployeeAddressListCreateView.as_view()),    # End Point for List and Create method.
    path('employeeaddresses/<int:id>/', views.EmployeeAddressRUDView.as_view()),  # Endpoint for Retrieve, Update and Delete.
    path('employees/', views.EmployeeListCreateView.as_view()),                 # End Point for List and Create method.
    path('employees/<int:id>/', views.EmployeeRUDView.as_view()),               # Endpoint for Retrieve, Update and Delete.
    path('employees?enq_lvl_id=<int:enq_lvl_id>', views.EmployeeListCreateView.as_view()),  #End point for Create and list.
    path('employees/<int:id>?enq_lvl_id=<int:enq_lvl_id>', views.EmployeeRUDView.as_view()),
    path('employees?first_name=<str:first_name>', views.EmployeeListCreateView.as_view()),
    path('employmentdetails/', views.EmploymentDetailsListCreateView.as_view()),  # End Point for List and Create method.
    path('employmentdetails/<int:id>/', views.EmploymentDetailsRUDView.as_view()),  # Endpoint for Retrieve, Update and Delete.
    path('employmentdetails?department=<str:department>'
         '&designation=<str:designation>',
         views.EmploymentDetailsListCreateView.as_view()),    # End Point for List and Create method.
    path('employeecontacts/', views.EmployeeContactListCreateView.as_view()),       # End Point for List and Create method.
    path('employeecontacts/<int:id>/', views.EmployeeContactRUDView.as_view()),     #Endpoint for Retrieve, Update and Delete.
]
