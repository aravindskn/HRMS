from .models import (
                        Employee,
                        EmploymentDetails,
                        EmployeeContact,
                        EmployeeAddress,
                        Address
                    )

from ref_data_management.models import (
                                            RefDesignation,
                                            RefDepartment,
                                            RefMaritalStatus,
                                            RefGender,
                                            RefContactType,
                                            RefAddressType,
                                            RefCountry,
                                            RefStateProvince,
                                       )

from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from rest_framework import status

import json

from .constants import (
                            ZERO_ADDRESS_CONTACT_EMPLOYMENT_DETAILS,
                            ZERO_ADDRESS_EMPLOYMENT_DETAILS,
                            ZERO_ADDRESS,
                            EMPLOYEE_COMPOSITE_CREATE
                       )


class AddressTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_address_model(self):
        return Address.objects.create\
            (
                addr_line_one='16 A main',
                addr_line_two='HAL 2nd stage',
                addr_line_three='indiranagara',
                locality='bengaluru east',
                state_province_id=1,
                country_id=1,
                postal_code='560060',
                latitude=5,
                longitude=10
            )

    def test_create_ref_country_model(self):
        return RefCountry.objects.create\
            (
                country_name='India',
                country_iso_code='IN',
                country_code='91'
            )

    def test_create_ref_state_province_model(self):
        return RefStateProvince.objects.create\
            (
                state_name='Karnataka',
                state_code='KA',
                country_id=1
            )

    def test_check_address(self):
        temp = self.test_create_address_model()
        self.assertTrue(isinstance(temp, Address))

    def test_list_view_address(self):
        self.test_login()
        response = self.client.get('/api/1.0/addresses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_address(self):
        self.test_login()
        self.test_create_address_model()
        response = self.client.get('/api/1.0/addresses/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        self.test_login()
        self.test_create_address_model()
        response = self.client.delete('/api/1.0/addresses/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_view_address(self):
        self.test_login()
        self.test_create_ref_country_model()
        self.test_create_ref_state_province_model()

        response = self.client.post('/api/1.0/addresses/', json.dumps({
            "addr_line_one": "16 A MAIN",
            "addr_line_two": "HAL",
            "addr_line_three": "2nd stage",
            "locality": "Indiranagara",
            "city": "Bengaluru",
            "state_province": 1,
            "country": 1,
            "postal_code": "5600606",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_address(self):
        self.test_login()
        self.test_create_address_model()
        self.test_create_ref_country_model()
        self.test_create_ref_state_province_model()

        response = self.client.put('/api/1.0/addresses/1/', json.dumps({
            "addr_line_one": "16 A MAIN, 1st cross",
            "addr_line_two": "HALLL",
            "addr_line_three": "2nd stageeee",
            "locality": "Indiranagara",
            "city": "Bengaluru",
            "state_province": 1,
            "country": 1,
            "postal_code": "5600606",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmployeeTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    # create employee models

    def test_create_employee_model(self):
        return Employee.objects.create\
            (
                employee_id='E001',
                first_name='abcd',
                middle_name='efgh',
                last_name='rrrr',
                date_of_birth='1996-01-01',
                gender_id=1,
                marital_status_id=1
            )

    def test_create_ref_gender_model(self):
        return RefGender.objects.create\
            (
                gender_type='MALE',
                description=''
            )

    def test_create_ref_marital_status_model(self):
        return RefMaritalStatus.objects.create\
            (
                marital_status='SINGLE',
                description=''
            )

    # create employee contact

    def test_create_employee_contact_model(self):
        return EmployeeContact.objects.create\
            (
                contact_value='8660766574',
                contact_type_id=1,
                employee_id=1
            )

    def test_create_ref_contact_type_model(self):
        return RefContactType.objects.create\
            (
                contact_type='personal phone',
                description=''
            )

    # create employee address

    def test_create_employee_address_model(self):
        return EmployeeAddress.objects.create\
            (
                address_type_id=1,
                address_id=1,
                employee_id=1
            )

    def test_create_ref_address_type_model(self):
        return RefAddressType.objects.create\
            (
                address_type='HOME',
                description=''
            )

    # create employment details

    def test_create_employment_details_model(self):
        return EmploymentDetails.objects.create\
            (
                employment_start_date='2019-01-01',
                employment_end_date='2020-01-01',
                employee_id=1,
                department_id=1,
                designation_id=1
            )

    def test_create_ref_department_model(self):
        return RefDepartment.objects.create\
            (
                department_name='IT',
                department_code='D001',
                description=''
            )

    def test_create_ref_designation_model(self):
        return RefDesignation.objects.create\
            (
                designation_name='engineer',
                description=''
            )

    # create address model

    def test_create_address_model(self):
        return Address.objects.create\
            (
                addr_line_one='16 A main',
                addr_line_two='HAL 2nd stage',
                addr_line_three='indiranagara',
                locality='bengaluru east',
                state_province_id=1,
                country_id=1,
                postal_code='560060',
                latitude=5,
                longitude=10
            )

    def test_create_ref_country_model(self):
        return RefCountry.objects.create\
            (
                country_name='India',
                country_iso_code='IN',
                country_code='91'
            )

    def test_create_ref_state_province_model(self):
        return RefStateProvince.objects.create\
            (
                state_name='Karnataka',
                state_code='KA',
                country_id=1
            )
    #end

    def test_check_employee(self):
        temp = self.test_create_employee_model()
        self.assertTrue(isinstance(temp, Employee))

    def test_list_view_employee(self):
        self.test_login()
        response = self.client.get('/api/1.0/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_employee(self):
        self.test_login()
        self.test_create_employee_model()
        response = self.client.get('/api/1.0/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        self.test_login()
        self.test_create_employee_model()
        response = self.client.delete('/api/1.0/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_view_employee(self):
        self.test_login()
        self.test_create_ref_gender_model()
        self.test_create_ref_marital_status_model()

        response = self.client.post('/api/1.0/employees/', json.dumps({
            "employee_id": "E001",
            "first_name": "vijay",
            "middle_name": "kashyap",
            "last_name": "s",
            "date_of_birth": '1996-01-01',
            "marital_status": 1,
            "gender": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_employee(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_ref_gender_model()
        self.test_create_ref_marital_status_model()

        response = self.client.put('/api/1.0/employees/1/', json.dumps({
            "employee_id": "E001",
            "first_name": "vijay",
            "middle_name": "kashyap",
            "last_name": "s",
            "date_of_birth": '1996-01-01',
            "marital_status": 1,
            "gender": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_zero_contact_address_employment_details(self):
        self.test_login()
        self.test_create_ref_gender_model()
        self.test_create_ref_marital_status_model()

        response = self.client.post('/api/1.0/employees/', json.dumps(
            ZERO_ADDRESS_CONTACT_EMPLOYMENT_DETAILS
        ), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_zero_address_employment_details(self):
        self.test_login()
        self.test_create_ref_gender_model()
        self.test_create_ref_marital_status_model()

        self.test_create_ref_contact_type_model()

        response = self.client.post('/api/1.0/employees/', json.dumps(
            ZERO_ADDRESS_EMPLOYMENT_DETAILS
        ), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_zero_address(self):
        self.test_login()
        self.test_create_ref_gender_model()
        self.test_create_ref_marital_status_model()

        self.test_create_ref_contact_type_model()
        self.test_create_ref_department_model()
        self.test_create_ref_designation_model()

        response = self.client.post('/api/1.0/employees/', json.dumps(
            ZERO_ADDRESS
        ), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_composite_create(self):
        self.test_login()
        self.test_create_ref_gender_model()
        self.test_create_ref_marital_status_model()

        self.test_create_ref_contact_type_model()
        self.test_create_ref_department_model()
        self.test_create_ref_designation_model()
        self.test_create_ref_address_type_model()
        self.test_create_ref_country_model()
        self.test_create_ref_state_province_model()

        response = self.client.post('/api/1.0/employees/', json.dumps(
            EMPLOYEE_COMPOSITE_CREATE
        ), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filter_enq_lvl_id(self):
        self.test_login()
        response = self.client.get('/api/1.0/employees/', {'enq_lvl_id': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_wrong_enq_lvl_id(self):
        self.test_login()
        response = self.client.get('/api/1.0/employees/', {'enq_lvl_id': 11})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_noninteger_enq_lvl_id(self):
        self.test_login()
        response = self.client.get('/api/1.0/employees/', {'enq_lvl_id': 'w'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_filter_enq_lvl_id(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_employee_address_model()
        self.test_create_employee_contact_model()
        self.test_create_employment_details_model()
        self.test_create_address_model()
        
        response = self.client.get('/api/1.0/employees/1/', {'enq_lvl_id': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_filter_wrong_enq_lvl_id(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_employee_address_model()
        self.test_create_employee_contact_model()
        self.test_create_employment_details_model()
        self.test_create_address_model()

        response = self.client.get('/api/1.0/employees/1/', {'enq_lvl_id': 11})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_filter_noninteger_enq_lvl_id(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_employee_address_model()
        self.test_create_employee_contact_model()
        self.test_create_employment_details_model()
        self.test_create_address_model()

        response = self.client.get('/api/1.0/employees/1/', {'enq_lvl_id': 'w'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EmployeeContactTest(APITestCase):

    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_employee_contact_model(self):
        return EmployeeContact.objects.create\
            (
                contact_value='8660766574',
                contact_type_id=1,
                employee_id=1
            )

    def test_create_ref_contact_type_model(self):
        return RefContactType.objects.create\
            (
                contact_type='personal phone',
                description=''
            )

    def test_create_employee_model(self):
        return Employee.objects.create\
            (
                employee_id='E001',
                first_name='abcd',
                middle_name='efgh',
                last_name='rrrr',
                date_of_birth='1996-01-01',
                gender_id=1,
                marital_status_id=1
            )

    def test_check_employee_contact(self):
        temp = self.test_create_employee_contact_model()
        self.assertTrue(isinstance(temp, EmployeeContact))

    def test_list_view_employee_contact(self):
        self.test_login()
        response = self.client.get('/api/1.0/employeecontacts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_employee_contact(self):
        self.test_login()
        self.test_create_employee_contact_model()
        response = self.client.get('/api/1.0/employeecontacts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee_contact(self):
        self.test_login()
        self.test_create_employee_contact_model()
        response = self.client.delete('/api/1.0/employeecontacts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_view_employee_contact(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_ref_contact_type_model()

        response = self.client.post('/api/1.0/employeecontacts/', json.dumps({
            "employee": 1,
            "contact_value": "1234567890",
            "contact_type": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_employee_contact(self):
        self.test_login()
        self.test_create_employee_contact_model()
        self.test_create_employee_model()
        self.test_create_ref_contact_type_model()

        response = self.client.put('/api/1.0/employeecontacts/1/', json.dumps({
            "employee": 1,
            "contact_value": "1234567891",
            "contact_type": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmploymentDetailsTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_employment_details_model(self):
        return EmploymentDetails.objects.create\
            (
                employment_start_date='2019-01-01',
                employment_end_date='2020-01-01',
                employee_id=1,
                department_id=1,
                designation_id=1
            )

    def test_create_ref_department_model(self):
        return RefDepartment.objects.create\
            (
                department_name='IT',
                department_code='D001',
                description=''
            )

    def test_create_ref_designation_model(self):
        return RefDesignation.objects.create\
            (
                designation_name='engineer',
                description=''
            )

    def test_create_employee_model(self):
        return Employee.objects.create\
            (
                employee_id='E001',
                first_name='abcd',
                middle_name='efgh',
                last_name='rrrr',
                date_of_birth='1996-01-01',
                gender_id=1,
                marital_status_id=1
            )

    def test_check_employment_details(self):
        temp = self.test_create_employment_details_model()
        self.assertTrue(isinstance(temp, EmploymentDetails))

    def test_list_view_employment_details(self):
        self.test_login()
        response = self.client.get('/api/1.0/employmentdetails/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_employment_details(self):
        self.test_login()
        self.test_create_employment_details_model()
        response = self.client.get('/api/1.0/employmentdetails/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employment_details(self):
        self.test_login()
        self.test_create_employment_details_model()
        response = self.client.delete('/api/1.0/employmentdetails/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_view_employment_details(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_ref_department_model()
        self.test_create_ref_designation_model()

        response = self.client.post('/api/1.0/employmentdetails/', json.dumps({
            "employee": 1,
            "employment_start_date": "2019-01-01",
            "department": 1,
            "designation": 1,
            "employment_end_date": "2019-02-01",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_employment_details(self):
        self.test_login()
        self.test_create_employment_details_model()
        self.test_create_employee_model()
        self.test_create_ref_department_model()
        self.test_create_ref_designation_model()

        response = self.client.put('/api/1.0/employmentdetails/1/', json.dumps({
            "employee": 1,
            "employment_start_date": "2019-01-01",
            "department": 1,
            "designation": 1,
            "employment_end_date": "2020-02-01",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmployeeAddressTest(APITestCase):
    def setUp(self):
        self.credentials = {"username": "vkashyap19", "password": "abcd1234"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_employee_address_model(self):
        return EmployeeAddress.objects.create\
            (
                address_type_id=1,
                address_id=1,
                employee_id=1
            )

    def test_create_ref_address_type_model(self):
        return RefAddressType.objects.create\
            (
                address_type='HOME',
                description=''
            )

    def test_create_employee_model(self):
        return Employee.objects.create\
            (
                employee_id='E001',
                first_name='abcd',
                middle_name='efgh',
                last_name='rrrr',
                date_of_birth='1996-01-01',
                gender_id=1,
                marital_status_id=1
            )

    def test_create_address_model(self):
        return Address.objects.create\
            (
                addr_line_one='16 A main',
                addr_line_two='HAL 2nd stage',
                addr_line_three='indiranagara',
                locality='bengaluru east',
                state_province_id=1,
                country_id=1,
                postal_code='560060',
                latitude=5,
                longitude=10
            )

    def test_create_ref_country_model(self):
        return RefCountry.objects.create\
            (
                country_name='India',
                country_iso_code='IN',
                country_code='91'
            )

    def test_create_ref_state_province_model(self):
        return RefStateProvince.objects.create\
            (
                state_name='Karnataka',
                state_code='KA',
                country_id=1
            )

    def test_check_employee_address(self):
        temp = self.test_create_employee_address_model()
        self.assertTrue(isinstance(temp, EmployeeAddress))

    def test_list_view_employee_address(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_ref_address_type_model()
        self.test_create_address_model()
        response = self.client.get('/api/1.0/employeeaddresses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_view_employee_address(self):
        self.test_login()
        self.test_create_employee_address_model()
        response = self.client.get('/api/1.0/employeeaddresses/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee_address(self):
        self.test_login()
        self.test_create_employee_address_model()
        response = self.client.delete('/api/1.0/employeeaddresses/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_view_employee_address(self):
        self.test_login()
        self.test_create_employee_model()
        self.test_create_ref_address_type_model()
        self.test_create_address_model()
        self.test_create_ref_state_province_model()
        self.test_create_ref_country_model()

        response = self.client.post('/api/1.0/employeeaddresses/', json.dumps({
            "address_type": 1,
            "address": 1,
            "employee": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "deleted_date": None
        }),content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_view_employee_address(self):
        self.test_login()
        self.test_create_employee_address_model()
        self.test_create_employee_model()
        self.test_create_ref_address_type_model()
        self.test_create_address_model()
        self.test_create_ref_state_province_model()
        self.test_create_ref_country_model()

        response = self.client.put('/api/1.0/employeeaddresses/1/', json.dumps({
            "address_type": 1,
            "address": 1,
            "employee": 1,
            "created_by": "systems",
            "last_updated_by": "systems",
            "deleted_status": False,
            "deleted_date": None
        }),content_type='application/json')

        self.assertEqual(response.status_code,status.HTTP_200_OK)
