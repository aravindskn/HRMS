from django.urls import path
from . import views

urlpatterns = [

    path('leaveeligibilities/', views.LeaveEligibilityListCreateView.as_view()),
        # Endpoints for CREATE AND LIST operations for leave eligibility

    path('leaveeligibilities/<int:id>/', views.LeaveEligibilityRUDView.as_view()),
        # Endpoints for RUD operations for leave eligibility

    path('leaverevision/', views.LeaveRevisionListCreateView.as_view()),
        # Endpoints for CREATE AND LIST operations for leave eligibility

    path('leaverevision/<int:id>/', views.LeaveRevisionRUDView.as_view()),
        # Endpoints for RUD operations for leave request

    path('leaverequests/', views.LeaveRequestListCreateView.as_view()),
        # Endpoints for CREATE AND LIST operations for leave requests

    path('leaverequests/<int:id>/', views.LeaveRequestRUDView.as_view()),
        # Endpoints for RUD operations for leave requests

    path('leaverequests?start_date=<yyyymmdd>', views.LeaveRequestListCreateView.as_view()),
        # End point for Listing leave reqeusts for a particular employee

    path('leaverequests?start_date=<yyyymmdd>&end_date=<yearmmdd>', views.LeaveRequestListCreateView.as_view()),
        # End point for Listing leave requests of all employees based on leave start and end date

    path('leaverequests?emp_id=<employee_id>&start_date=<yyyymmdd>', views.LeaveRequestListCreateView.as_view()),
        # End point for Listing leave requests for an employee_id and filtering based on start date

    path('leaverequests?emp_id=<employee_id>&start_date=<yyyymmdd>&end_date=<yearmmdd>',
            views.LeaveRequestListCreateView.as_view()),
        # Endpoint for filtering leave requests for an employee based on leave_start and end_dat

    path('leaveeligibilities?emp_id=<employee_id>', views.LeaveEligibilityListCreateView.as_view()),
        # Endpoint for filtering leave eligibility for an employee using employee_id

    path('leaveeligibilities?emp_id=<employee_id>&include_availability=<y>',
         views.LeaveEligibilityListCreateView.as_view())
    # Endpoint for filtering employee based on include_availability code

]