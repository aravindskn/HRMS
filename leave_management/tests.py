from .models import (
                        LeaveEligibility,
                        LeaveRequest,
                        LeaveRevision,
                    )

from ref_data_management.models import (
                                        RefLeaveType,
                                        RefLeaveRequestStatus,
                                        RefLeaveRevisionType
                                  )

from employee_management.models import Employee

from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from rest_framework import status

import json


class LeaveEligibilityTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_leave_eligibility(self):
        return LeaveEligibility.objects.create\
                (
                    number_of_days_id=1,
                    employee_id=1,
                    leave_type_id=1
                )

    def test_create_leave_type(self):
        return RefLeaveType.objects.create\
            (
                leave_type_name='casual',
                description=''
            )

    def test_create_employee(self):
        return Employee.objects.create\
            (
                employee_id='E001',
                first_name='vijay',
                middle_name='k',
                last_name='ssd',
                date_of_birth='2019-01-01',
                gender_id=1,
                marital_status_id=1
            )

    def test_create_leave_revision(self):
        return LeaveRevision.objects.create\
            (
                number_of_days='10',
                leave_type_id=1,
                revision_type_id=1
            )

    def test_check_leave_eligibility(self):
        temp = self.test_create_leave_eligibility()
        self.assertTrue(isinstance(temp, LeaveEligibility))

    def test_list_view_leave_eligibility(self):
        self.test_login()
        response = self.client.get('/api/1.0/leaveeligibilities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_leave_eligibility(self):
        self.test_login()
        self.test_create_leave_eligibility()
        response = self.client.get('/api/1.0/leaveeligibilities/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleted_view_leave_eligibility(self):
        self.test_login()
        self.test_create_leave_eligibility()
        response = self.client.delete('/api/1.0/leaveeligibilities/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_emp_id(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_eligibility()
        response = self.client.get('/api/1.0/leaveeligibilities/', {'emp_id':'E001'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_emp_id_availablility(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_eligibility()
        response = self.client.get('/api/1.0/leaveeligibilities/', {'emp_id': 'E001', 'include_availability': 'y'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_view_leave_eligibility(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_create_leave_revision()

        response = self.client.post('/api/1.0/leaveeligibilities/',  json.dumps({
            "employee": 1,
            "employee_name": "E0002, abcd, hijk",
            "number_of_days": 1,
            "number_of_days_value": "30, sick",
            "leave_type": 1,
            "leave_type_name": "sick",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-17",
            "deleted_date": None,
            "created_date": "2019-01-17"
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_leave_eligibility(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_create_leave_revision()
        self.test_create_leave_eligibility()

        response = self.client.put('/api/1.0/leaveeligibilities/1/',  json.dumps({

            "employee": 1,
            "number_of_days": 1,
            "leave_type": 1,
            "created_by": "systemqqqqq",
            "last_updated_by": "systemqqqqq",
            "deleted_status": False,
            "last_updated_date": "2019-01-17",
            "deleted_date": None,
            "created_date": "2019-01-17"
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # negative test cases
    
    def test_filter_emp_id_availability_wrong_empid(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_eligibility()
        response = self.client.get('/api/1.0/leaveeligibilities/', {'emp_id': 'E01', 'include_availability': 'y'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_emp_id_wrong_empid_wrong_choice(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_eligibility()
        response = self.client.get('/api/1.0/leaveeligibilities/', {'emp_id': 'E01', 'include_availability': 'n'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_wrong_empid_nochoice(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_eligibility()
        response = self.client.get('/api/1.0/leaveeligibilities/', {'emp_id': 'E01'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_wrong_json(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_create_leave_revision()

        response = self.client.post('/api/1.0/leaveeligibilities/', json.dumps({
            "employee": 1,
            "employee_name": "E0002, abcd, hijk",
            "number_of_days_value": "30, sick",
            "leave_type": 1,
            "leave_type_name": "sick",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-17",
            "deleted_date": None,
            "created_date": "2019-01-17"
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_wrong_json(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_create_leave_revision()
        self.test_create_leave_eligibility()

        response = self.client.put('/api/1.0/leaveeligibilities/1/', json.dumps({

            "employee": 1,
            "number_of_days": 1,
            "created_by": "systemqqqqq",
            "last_updated_by": "systemqqqqq",
            "deleted_status": False,
            "last_updated_date": "2019-01-17",
            "deleted_date": None,
            "created_date": "2019-01-17"
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LeaveRevisionTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_leave_revision(self):
        return LeaveRevision.objects.create\
            (
                number_of_days='50',
                leave_type_id=1,
                revision_type_id=1
            )

    def test_create_leave_type(self):
        return RefLeaveType.objects.create\
            (
                leave_type_name='casual',
                description=''
            )

    def test_create_revision_type(self):
        return RefLeaveRevisionType.objects.create\
            (
                leave_revision_type_name='govt',
                description=''
            )

    def test_check_leave_revision(self):
        temp = self.test_create_leave_revision()
        self.assertTrue(isinstance(temp, LeaveRevision))

    def test_list_view_leave_revision(self):
        self.test_login()
        response = self.client.get('/api/1.0/leaverevision/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_leave_revision(self):
        self.test_login()
        self.test_create_leave_revision()
        response = self.client.get('/api/1.0/leaverevision/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_view_leave_revision(self):
        self.test_login()
        self.test_create_leave_revision()
        response = self.client.delete('/api/1.0/leaverevision/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_view_leave_revision(self):
        self.test_login()
        self.test_create_leave_revision()
        self.test_create_leave_type()
        self.test_create_revision_type()
        response = self.client.post('/api/1.0/leaverevision/', json.dumps({
            "leave_type": 1,
            "number_of_days": "50",
            "revision_type": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None,
        }),  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_leave_revision(self):
        self.test_login()
        self.test_create_leave_revision()
        self.test_create_leave_type()
        self.test_create_revision_type()
        response = self.client.put('/api/1.0/leaverevision/1/', json.dumps({
            "leave_type": 1,
            "number_of_days": "50",
            "revision_type": 1,
            "created_by": "systemwww",
            "last_updated_by": "systemwww",
            "deleted_status": False,
            "deleted_date": None,
        }),  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # negative test cases

    def test_post_wrong_json(self):
        self.test_login()
        self.test_create_leave_revision()
        self.test_create_leave_type()
        self.test_create_revision_type()
        response = self.client.post('/api/1.0/leaverevision/', json.dumps({
            "leave_type": 1,
            "number_of_days": "50",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None,
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_wrong_json(self):
        self.test_login()
        self.test_create_leave_revision()
        self.test_create_leave_type()
        self.test_create_revision_type()
        response = self.client.put('/api/1.0/leaverevision/1/', json.dumps({
            "leave_type": 1,
            "number_of_days": "50",
            "last_updated_by": "systemwww",
            "deleted_status": False,
            "deleted_date": None,
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LeaveRequestTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_leave_request(self):
        return LeaveRequest.objects.create\
            (
                leave_start_date='2019-01-01',
                leave_end_date='2019-01-04',
                comments='',
                employee_id=1,
                request_status_id=1,
                leave_type_id=1
            )

    def test_create_leave_type(self):
        return RefLeaveType.objects.create\
            (
                leave_type_name='casual',
                description=''
            )

    def test_create_employee(self):
        return Employee.objects.create\
            (
                employee_id='E001',
                first_name='vijay',
                middle_name='k',
                last_name='ssd',
                date_of_birth='2019-01-01',
                gender_id=1,
                marital_status_id=1
            )

    def test_request_status(self):
        return RefLeaveRequestStatus.objects.create\
            (
                leave_request_status_name='applied',
                description=''
            )

    def test_check_leave_request(self):
        temp = self.test_create_leave_request()
        self.assertTrue(isinstance(temp, LeaveRequest))

    def test_list_view_leave_request(self):
        self.test_login()
        response = self.client.get('/api/1.0/leaverequests/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_leave_request(self):
        self.test_login()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_view_leave_request(self):
        self.test_login()
        self.test_create_leave_request()
        response = self.client.delete('/api/1.0/leaverequests/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_empid_startdate(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'emp_id': 'E001', 'start_date': 20190101})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_empid_startdate_enddate(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {
                                                                'emp_id': 'E001',
                                                                'start_date': 20190101,
                                                                'end_date': 20190130
                                                              })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_start_date(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'start_date': 20190101})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_startdate_enddate(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {
                                                                'start_date': 20190101,
                                                                'end_date': 20190130
                                                              })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_view_leave_request(self):
        self.test_login()
        self.test_create_leave_request()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_request_status()
        response = self.client.post('/api/1.0/leaverequests/', json.dumps({
            "employee": 1,
            "leave_type": 1,
            "leave_start_date": "2019-01-18",
            "leave_end_date": "2019-01-25",
            "comments": "",
            "request_status": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-16",
            "deleted_date": None,
            "created_date": "2019-01-16"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_leave_request(self):
        self.test_login()
        self.test_create_leave_request()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_request_status()
        response = self.client.put('/api/1.0/leaverequests/1/', json.dumps({
            "employee": 1,
            "leave_type": 1,
            "leave_start_date": "2019-01-18",
            "leave_end_date": "2019-01-25",
            "comments": "",
            "request_status": 1,
            "created_by": "systemetet",
            "last_updated_by": "systemeeee",
            "deleted_status": False,
            "last_updated_date": "2019-01-16",
            "deleted_date": None,
            "created_date": "2019-01-16"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # negative test cases

    def test_filter_wrong_empid(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'emp_id': 'E01', 'start_date': 20190101})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_wrong_start_date(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'emp_id': 'E001', 'start_date': 2019})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_empid_correct_dates(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'emp_id': 'E01',
                                                               'start_date': 20190101,
                                                               'end_date': 20190201
                                                               })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_correct_empid_wrong_dates(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'emp_id': 'E01',
                                                               'start_date': 2019,
                                                               'end_date': 'XXSGbsnb'
                                                               })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_start_date(self):
        self.test_login()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {
                                                               'start_date': 2019
                                                               })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_start_date_end_date(self):
        self.test_login()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {
                                                                'start_date': 2019,
                                                                'end_date': 'sssccs'
                                                               })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_empid_correct_start_date(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {'emp_id': 'E01',
                                                               'start_date': 20190120
                                                               })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_missing_start_date(self):
        self.test_login()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {

            'end_date': 20190107
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_emp_id_none_dates(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {
                                                                'emp_id': 'E001'
                                                               })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_emp_id_none_dates(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_leave_request()
        response = self.client.get('/api/1.0/leaverequests/', {
            'emp_id': 'E01'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_wrong_json(self):
        self.test_login()
        self.test_create_leave_request()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_request_status()
        response = self.client.post('/api/1.0/leaverequests/', json.dumps({
            "employee": 1,
            "leave_type": 1,
            "leave_start_date": "2019-01-18",
            "comments": "",
            "request_status": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-16",
            "deleted_date": None,
            "created_date": "2019-01-16"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_wrong_json(self):
        self.test_login()
        self.test_create_leave_request()
        self.test_create_employee()
        self.test_create_leave_type()
        self.test_request_status()
        response = self.client.put('/api/1.0/leaverequests/1/', json.dumps({
            "employee": 1,
            "leave_type": 1,
            "leave_end_date": "2019-01-25",
            "comments": "",
            "request_status": 1,
            "created_by": "systemetet",
            "last_updated_by": "systemeeee",
            "deleted_status": False,
            "last_updated_date": "2019-01-16",
            "deleted_date": None,
            "created_date": "2019-01-16"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

