"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/performance_management/urls.py
    Description: This module contains all API endpoints for the performance_management application.
--------------------------------------------------------------------------------------------------
"""

from django.urls import path
from . import views

urlpatterns = [
    path('performanceassessmentrec/', views.PerformanceAssessmentRecListCreateView.as_view()),
    # Endpoint LIST, CREATE method for Performance Assessment Record.
    path('performanceassessmentrec/<int:id>/', views.PerformanceAssessmentRecRUDView.as_view()),
    # Endpoint RETRIEVE, UPDATE, DESTROY for Performance Assessment Record.
    path('goals/', views.GoalsListCreateView.as_view()),
    # Endpoint LIST, CREATE method for Goals.
    path('goals/<int:id>/', views.GoalsRUDView.as_view()),
    # Endpoint RETRIEVE, UPDATE, DESTROY for Goals.
    path('performanceassessmentrec/<int:performance_assessment>/goals/', views.GoalsListView.as_view()),
    # Endpoint to list all goals for a specific performance assessment.
    path('milestones/', views.MilestoneListCreateView.as_view()),
    # Endpoint LIST, CREATE method for Milestone.
    path('milestones/<int:id>/', views.MilestoneRUDView.as_view()),
    # Endpoint RETRIEVE, UPDATE, DESTROY for Milestone.
    path('performanceassessmentrec?emp_id=<int:emp_id>&status=<int:status>',
         views.PerformanceAssessmentRecListCreateView.as_view()),
    # Endpoint to list all performance assessment of a particular employee and status
    path('performanceassessmentrec?emp_id=<int:emp_id>', views.PerformanceAssessmentRecListCreateView.as_view()),
    # Endpoint to list all performance assessment of a particular employee.
    path('goals/<int:goal>/milestones/', views.MilestoneListView.as_view()),
    # Endpoint to list all milestones for a specific goal.
]
