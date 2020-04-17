from .models import (
                        RefStateProvince,
                        RefCountry,
                        RefAddressType,
                        RefContactType,
                        RefDepartment,
                        RefDesignation,
                        RefGender,
                        RefLeaveRequestStatus,
                        RefLeaveRevisionType,
                        RefLeaveType,
                        RefMaritalStatus,
                        RefRatingScale,
                        RefTargetUnit,
                        RefPerformanceRecStatus
                     )
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
import json


class RefCountryTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_ref_country(self):
        return RefCountry.objects.create(country_name='India',
                                         country_iso_code='IN',
                                         country_code='91')

    def test_country(self):
        country = self.test_create_ref_country()
        self.assertTrue(isinstance(country, RefCountry))

    def test_country_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/countries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_retrieve_view(self):
        self.test_login()
        self.test_create_ref_country()
        response = self.client.get('/api/1.0/ref/countries/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_delete_view(self):
        self.test_login()
        self.test_create_ref_country()
        response = self.client.delete('/api/1.0/ref/countries/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_country_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/countries/', json.dumps({
            "country_name": "India",
            "country_iso_code": "IN",
            "country_code": "91",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_country_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/countries/', json.dumps({
            "country_iso_code": "IN",
            "country_code": "91",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_country_put_view(self):
        self.test_login()
        self.test_create_ref_country()
        response = self.client.put('/api/1.0/ref/countries/1/', json.dumps({
            "country_name": "India",
            "country_iso_code": "IN",
            "country_code": "92",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_ref_country()
        response = self.client.put('/api/1.0/ref/countries/1/', json.dumps({
            "country_iso_code": "IN",
            "country_code": "92",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefStateProvinceTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_ref_country(self):
        return RefCountry.objects.create(country_name='India',
                                         country_iso_code='IN',
                                         country_code='91')

    def test_create_stateprovince(self):
        return RefStateProvince.objects.create(state_name='Karnataka',
                                               state_code='KA',
                                               country_id=1)

    def test_stateprovince_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/states/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stateprovince_retrieve_view(self):
        self.test_login()
        self.test_create_stateprovince()
        response = self.client.get('/api/1.0/ref/states/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stateprovince_delete_view(self):
        self.test_login()
        self.test_create_stateprovince()
        response = self.client.delete('/api/1.0/ref/states/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_state_list_view(self):
        self.test_login()
        self.test_create_stateprovince()
        self.test_create_ref_country()
        response = self.client.get('/api/1.0/ref/countries/1/states/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_state_province_post_view(self):
        self.test_login()
        self.test_create_ref_country()
        response = self.client.post('/api/1.0/ref/states/', json.dumps({
            "state_name": "Karnataka",
            "state_code": "KA",
            "country": 1,
            "country_name": "India",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": "2019-01-09",
            "last_updated_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_state_province_post_wrong_json_structure(self):
        self.test_login()
        self.test_create_ref_country()
        response = self.client.post('/api/1.0/ref/states/', json.dumps({
            "state_code": "KA",
            "country": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_state_province_put_view(self):
        self.test_login()
        self.test_create_stateprovince()
        self.test_create_ref_country()
        response = self.client.put('/api/1.0/ref/states/1/', json.dumps({
            "state_name": "Karnatak",
            "state_code": "KA",
            "country": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_state_province_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_stateprovince()
        self.test_create_ref_country()
        response = self.client.put('/api/1.0/ref/states/1/', json.dumps({
            "state_code": "KA",
            "country": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefAddressTypeTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_address_type(self):
        return RefAddressType.objects.create(address_type='Office',
                                             description='Office')

    def test_address_type(self):
        addresstype = self.test_create_address_type()
        self.assertTrue(isinstance(addresstype, RefAddressType))

    def test_address_type_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/addresstype/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_address_type_retireve_view(self):
        self.test_login()
        self.test_create_address_type()
        response = self.client.get('/api/1.0/ref/addresstype/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_address_type_delete_view(self):
        self.test_login()
        self.test_create_address_type()
        response = self.client.delete('/api/1.0/ref/addresstype/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_address_type_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/addresstype/', json.dumps({
            "address_type": "Office",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_address_type_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/addresstype/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_address_type_put_view(self):
        self.test_login()
        self.test_create_address_type()
        response = self.client.put('/api/1.0/ref/addresstype/1/', json.dumps({
            "address_type": "Home",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_address_type_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_address_type()
        response = self.client.put('/api/1.0/ref/addresstype/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefContactTypeTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_contact_type(self):
        return RefContactType.objects.create(contact_type='Office',
                                             description='Office')

    def test_contact_type(self):
        contacttype = self.test_create_contact_type()
        self.assertTrue(isinstance(contacttype, RefContactType))

    def test_contact_type_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/contacttype/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_type_retireve_view(self):
        self.test_login()
        self.test_create_contact_type()
        response = self.client.get('/api/1.0/ref/contacttype/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_type_delete_view(self):
        self.test_login()
        self.test_create_contact_type()
        response = self.client.delete('/api/1.0/ref/contacttype/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_contact_type_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/contacttype/', json.dumps({
            "contact_type": "Office",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_contact_type_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/contacttype/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_type_put_view(self):
        self.test_login()
        self.test_create_contact_type()
        response = self.client.put('/api/1.0/ref/contacttype/1/', json.dumps({
            "contact_type": "Home",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_type_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_contact_type()
        response = self.client.put('/api/1.0/ref/contacttype/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefDepartmentTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_department(self):
        return RefDepartment.objects.create(department_name='Engineering',
                                            department_code='ENGG',
                                            description='Office')

    def test_department(self):
        department = self.test_create_department()
        self.assertTrue(isinstance(department, RefDepartment))

    def test_department_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/departments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_department_retireve_view(self):
        self.test_login()
        self.test_create_department()
        response = self.client.get('/api/1.0/ref/departments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_department_delete_view(self):
        self.test_login()
        self.test_create_department()
        response = self.client.delete('/api/1.0/ref/departments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_department_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/departments/', json.dumps({
            "department_name": "Engineering",
            "department_code": "ENGG",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_department_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/departments/', json.dumps({
            "department_code": "ENGG",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_department_put_view(self):
        self.test_login()
        self.test_create_department()
        response = self.client.put('/api/1.0/ref/departments/1/', json.dumps({
            "department_name": "Engineering",
            "department_code": "ENGG",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_department_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_department()
        response = self.client.put('/api/1.0/ref/departments/1/', json.dumps({
            "department_code": "ENGG",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefDesignationTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_designation(self):
        return RefDesignation.objects.create(designation_name='Software Trainee',
                                            description='Office')

    def test_designation(self):
        designation = self.test_create_designation()
        self.assertTrue(isinstance(designation, RefDesignation))

    def test_designation_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/designations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_designation_retireve_view(self):
        self.test_login()
        self.test_create_designation()
        response = self.client.get('/api/1.0/ref/designations/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_designation_delete_view(self):
        self.test_login()
        self.test_create_designation()
        response = self.client.delete('/api/1.0/ref/designations/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_designation_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/designations/', json.dumps({
            "designation_name": "Software Trainee",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_designation_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/designations/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_designation_put_view(self):
        self.test_login()
        self.test_create_designation()
        response = self.client.put('/api/1.0/ref/designations/1/', json.dumps({
            "designation_name": "Software",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_designation_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_designation()
        response = self.client.put('/api/1.0/ref/designations/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefGenderTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_gender(self):
        return RefGender.objects.create(gender_type='Male',
                                        description='Male')

    def test_gender(self):
        gender = self.test_create_gender()
        self.assertTrue(isinstance(gender, RefGender))

    def test_gender_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/gender/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gender_retireve_view(self):
        self.test_login()
        self.test_create_gender()
        response = self.client.get('/api/1.0/ref/gender/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gender_delete_view(self):
        self.test_login()
        self.test_create_gender()
        response = self.client.delete('/api/1.0/ref/gender/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_gender_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/gender/', json.dumps({
            "gender_type": "Male",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_gender_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/gender/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_gender_put_view(self):
        self.test_login()
        self.test_create_gender()
        response = self.client.put('/api/1.0/ref/gender/1/', json.dumps({
            "gender_type": "Female",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gender_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_gender()
        response = self.client.put('/api/1.0/ref/gender/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefMaritalStatusTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_marital_status(self):
        return RefMaritalStatus.objects.create(marital_status='Single',
                                                description='Male')

    def test_marital_status(self):
        marital_status = self.test_create_marital_status()
        self.assertTrue(isinstance(marital_status, RefMaritalStatus))

    def test_marital_status_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/maritalstatus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_marital_status_retireve_view(self):
        self.test_login()
        self.test_create_marital_status()
        response = self.client.get('/api/1.0/ref/maritalstatus/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_marital_status_delete_view(self):
        self.test_login()
        self.test_create_marital_status()
        response = self.client.delete('/api/1.0/ref/maritalstatus/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_marital_status_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/maritalstatus/', json.dumps({
            "marital_status": "Single",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_marital_status_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/maritalstatus/', json.dumps({
            "description": "",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_marital_status_put_view(self):
        self.test_login()
        self.test_create_marital_status()
        response = self.client.put('/api/1.0/ref/maritalstatus/1/', json.dumps({
            "marital_status": "Married",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_marital_status_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_marital_status()
        response = self.client.put('/api/1.0/ref/maritalstatus/1/', json.dumps({
            "description": "",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefTargetUnitTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_target_unit(self):
        return RefTargetUnit.objects.create(target_unit='Days',
                                            description='Days')

    def test_target_unit(self):
        target_unit = self.test_create_target_unit()
        self.assertTrue(isinstance(target_unit, RefTargetUnit))

    def test_target_unit_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/targetunits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_target_unit_retireve_view(self):
        self.test_login()
        self.test_create_target_unit()
        response = self.client.get('/api/1.0/ref/targetunits/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_target_unit_delete_view(self):
        self.test_login()
        self.test_create_target_unit()
        response = self.client.delete('/api/1.0/ref/targetunits/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_target_unit_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/targetunits/', json.dumps({
            "target_unit": "Days",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_target_unit_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/targetunits/', json.dumps({
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_target_unit_put_view(self):
        self.test_login()
        self.test_create_target_unit()
        response = self.client.put('/api/1.0/ref/targetunits/1/', json.dumps({
            "target_unit": "Dollars",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_target_unit_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_target_unit()
        response = self.client.put('/api/1.0/ref/targetunits/1/', json.dumps({
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefRatingScaleTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_rating_scale(self):
        return RefRatingScale.objects.create(rating_value='Excellent',
                                             description='Good')

    def test_rating_scale(self):
        rating_scale = self.test_create_rating_scale()
        self.assertTrue(isinstance(rating_scale, RefRatingScale))

    def test_rating_scale_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/ratingscale/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rating_scale_retireve_view(self):
        self.test_login()
        self.test_create_rating_scale()
        response = self.client.get('/api/1.0/ref/ratingscale/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rating_scale_delete_view(self):
        self.test_login()
        self.test_create_rating_scale()
        response = self.client.delete('/api/1.0/ref/ratingscale/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_rating_scale_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/ratingscale/', json.dumps({
            "rating_value": "Excellent",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rating_scale_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/ratingscale/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rating_scale_put_view(self):
        self.test_login()
        self.test_create_rating_scale()
        response = self.client.put('/api/1.0/ref/ratingscale/1/', json.dumps({
            "rating_value": "Good",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rating_scale_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_rating_scale()
        response = self.client.put('/api/1.0/ref/ratingscale/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefPerformanceRecStatusTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_performance_rec_status(self):
        return RefPerformanceRecStatus.objects.create(status_name='Pending',
                                                      description='Good')

    def test_performance_rec_status(self):
        performance_rec_status = self.test_create_performance_rec_status()
        self.assertTrue(isinstance(performance_rec_status, RefPerformanceRecStatus))

    def test_performance_rec_status_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/performancerecstatus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_rec_status_retireve_view(self):
        self.test_login()
        self.test_create_performance_rec_status()
        response = self.client.get('/api/1.0/ref/performancerecstatus/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_rec_status_delete_view(self):
        self.test_login()
        self.test_create_performance_rec_status()
        response = self.client.delete('/api/1.0/ref/performancerecstatus/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_performance_rec_status_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/performancerecstatus/', json.dumps({
            "status_name": "Pending",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_performance_rec_status_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/performancerecstatus/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_performance_rec_status_put_view(self):
        self.test_login()
        self.test_create_performance_rec_status()
        response = self.client.put('/api/1.0/ref/performancerecstatus/1/', json.dumps({
            "status_name": "Approved",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_rec_status_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_performance_rec_status()
        response = self.client.put('/api/1.0/ref/performancerecstatus/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-09",
            "deleted_date": None,
            "last_updated_date": "2019-01-09"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefLeaveTypeTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_leave_type(self):
        return RefLeaveType.objects.create(leave_type_name='Sick',
                                            description='Good')

    def test_leave_type(self):
        leave_type = self.test_create_leave_type()
        self.assertTrue(isinstance(leave_type, RefLeaveType))

    def test_leave_type_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/leavetypes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_type_retireve_view(self):
        self.test_login()
        self.test_create_leave_type()
        response = self.client.get('/api/1.0/ref/leavetypes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_type_delete_view(self):
        self.test_login()
        self.test_create_leave_type()
        response = self.client.delete('/api/1.0/ref/leavetypes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_leave_type_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/leavetypes/', json.dumps({
            "leave_type_name": "Sick",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_leave_type_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/leavetypes/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_leave_type_put_view(self):
        self.test_login()
        self.test_create_leave_type()
        response = self.client.put('/api/1.0/ref/leavetypes/1/', json.dumps({
            "leave_type_name": "Casual",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_type_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_leave_type()
        response = self.client.put('/api/1.0/ref/leavetypes/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefLeaveRevisionTypeTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_leave_revision_type(self):
        return RefLeaveRevisionType.objects.create(leave_revision_type_name='Sick',
                                                    description='Good')

    def test_leave_revision_type(self):
        leave_revision_type = self.test_create_leave_revision_type()
        self.assertTrue(isinstance(leave_revision_type, RefLeaveRevisionType))

    def test_leave_revision_type_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/leaverevisiontypes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_revision_type_retireve_view(self):
        self.test_login()
        self.test_create_leave_revision_type()
        response = self.client.get('/api/1.0/ref/leaverevisiontypes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_revision_type_delete_view(self):
        self.test_login()
        self.test_create_leave_revision_type()
        response = self.client.delete('/api/1.0/ref/leaverevisiontypes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_leave_revision_type_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/leaverevisiontypes/', json.dumps({
            "leave_revision_type_name": "Annual",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_leave_revision_type_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/leaverevisiontypes/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_leave_revision_type_put_view(self):
        self.test_login()
        self.test_create_leave_revision_type()
        response = self.client.put('/api/1.0/ref/leaverevisiontypes/1/', json.dumps({
            "leave_revision_type_name": "Semi-Annual",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_revision_type_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_leave_revision_type()
        response = self.client.put('/api/1.0/ref/leaverevisiontypes/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RefLeaveRequestStatusTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'email': '',
            'password': '1nn0vent3s'}
        User.objects.create_superuser(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_leave_request_status(self):
        return RefLeaveRequestStatus.objects.create(leave_request_status_name='Pending',
                                                    description='Good')

    def test_leave_request_status(self):
        leave_request_status = self.test_create_leave_request_status()
        self.assertTrue(isinstance(leave_request_status, RefLeaveRequestStatus))

    def test_leave_request_status_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/ref/leaverequeststatus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_request_status_retireve_view(self):
        self.test_login()
        self.test_create_leave_request_status()
        response = self.client.get('/api/1.0/ref/leaverequeststatus/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_request_status_delete_view(self):
        self.test_login()
        self.test_create_leave_request_status()
        response = self.client.delete('/api/1.0/ref/leaverequeststatus/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_leave_request_status_post_view(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/leaverequeststatus/', json.dumps( {
            "leave_request_status_name": "Pending",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_leave_request_status_post_wrong_json_structure(self):
        self.test_login()
        response = self.client.post('/api/1.0/ref/leaverequeststatus/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_leave_request_status_put_view(self):
        self.test_login()
        self.test_create_leave_request_status()
        response = self.client.put('/api/1.0/ref/leaverequeststatus/1/', json.dumps({
            "leave_request_status_name": "Approved",
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leave_request_status_put_wrong_json_structure(self):
        self.test_login()
        self.test_create_leave_request_status()
        response = self.client.put('/api/1.0/ref/leaverequeststatus/1/', json.dumps({
            "description": "",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "created_date": "2019-01-23",
            "deleted_date": None,
            "last_updated_date": "2019-01-23"
            }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
