"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/performance_management/admin.py
    Description: This module contains all the models that are added in the django admin page.
--------------------------------------------------------------------------------------------------
"""
from django.contrib import admin

from .models import (PerformanceAssessmentRec,
                     Goals,
                     Milestone)

admin.site.register(PerformanceAssessmentRec)   # Adding Performance Assessment Record to Admin Page.
admin.site.register(Goals)                      # Adding Goals to Admin Page.
admin.site.register(Milestone)                  # Adding Milestone to Admin Page.

