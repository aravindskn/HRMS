"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/hrms/urls.py
    Description: This module contains all API endpoints for the hrms application.
--------------------------------------------------------------------------------------------------
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),    # Endpoint for Django admin page
    path('api/1.0/ref/', include('ref_data_management.urls')),  # Endpoint for Reference Data Management
    path('api/1.0/', include('employee_management.urls')),    # Endpoint for Employment Management
    path('', include('rest_auth.urls')),     # Endpoint for Authentication provided by django-rest-auth
    path('docs/', include_docs_urls(title='HRMS API Endpoints', public=False)),     # Endpoint for API Documentation
    path('api/1.0/', include('performance_management.urls')),   # Endpoint for Performance Management
    path('api/1.0/', include('leave_management.urls')),
]
