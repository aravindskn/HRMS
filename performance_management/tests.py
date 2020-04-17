from .models import PerformanceAssessmentRec, Goals, Milestone
from employee_management.models import Employee
from ref_data_management.models import RefPerformanceRecStatus, RefTargetUnit, RefRatingScale
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
import json


class PerformanceAssessmentRecTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'password': '1nn0vent3s'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_performance_assessment_rec(self):

        return PerformanceAssessmentRec.objects.create(employee_id_id=1,
                                                       assessment_year='2018-2019',
                                                       assessment_status_id=1,
                                                       overall_manager_comment='Okay',
                                                       overall_hod_comment='Okay',
                                                       overall_employee_comment='Okay')
    
    def test_create_ref_preforamance_rec_status(self):
        
        return RefPerformanceRecStatus.objects.create(status_name='pending')
    
    def test_create_employee(self):
        
        return Employee.objects.create(employee_id='E001',
                                       first_name='abc',
                                       last_name='def',
                                       date_of_birth='2019-09-09',
                                       gender_id=1)

    def test_performanceassessmentrec(self):
        performance_assessment_rec = self.test_create_performance_assessment_rec()
        self.assertTrue(isinstance(performance_assessment_rec, PerformanceAssessmentRec))

    def test_performanceassessmentrec_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/performanceassessmentrec/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performanceassessmentrec_list_view_wrong_url(self):
        self.test_login()
        response = self.client.get('/api/1.0/performanceassessment/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_retrieve_view(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performanceassessmentrec_retrieve_view_wrong_id(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_retrieve_view_wrong_url(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessment/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_emp_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'emp_id': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performanceassessmentrec_emp_querystring_wrong_url(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessment/', {'emp_id': 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_delete_view(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.delete('/api/1.0/performanceassessmentrec/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_performanceassessmentrec_delete_view_wrong_id(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.delete('/api/1.0/performanceassessmentrec/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_delete_view_wrong_url(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.delete('/api/1.0/performanceassessment/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_emp_status_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'emp_id': 1, 'status': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performanceassessmentrec_emp_status_nonstring_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'emp_id': 'w', 'status': 'w'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_emp_status_wrong_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'emp_id': 4, 'status': 4})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_status_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'status': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performanceassessmentrec_status_nonintegerstatus_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'status': 'w'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_emp_nonintegerempid_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'emp_id': 'w'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_status_wrongstatus_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'status': 4})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_emp_wrongempid_querystring(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        response = self.client.get('/api/1.0/performanceassessmentrec/', {'emp_id': 4})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performanceassessmentrec_create_view(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.post('/api/1.0/performanceassessmentrec/', json.dumps({
            "employee_id": 1,
            "assessment_year": "2019-2020",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Good",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": "2019-01-09",
            "created_date": "2019-01-09"}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_performanceassessmentrec_create_view_wrong_json(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.post('/api/1.0/performanceassessmentrec/', json.dumps({
            "assessment_year": "2019-2020",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Good",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": "2019-01-09",
            "created_date": "2019-01-09"}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_performanceassessmentrec_create_view_incomplete_json(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.post('/api/1.0/performanceassessmentrec/', json.dumps({
            "employee_id": 1,
            "assessment_year": " ",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Good",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": "2019-01-09",
            "created_date": "2019-01-09"}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_performanceassessmentrec_put_view(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.put('/api/1.0/performanceassessmentrec/1/', {
            "employee_id": 1,
            "assessment_year": "2019-2020",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Bad",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performanceassessmentrec_put_view_wrong_json(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.put('/api/1.0/performanceassessmentrec/1/', {
            "assessment_year": "2019-2020",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Bad",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_performanceassessmentrec_put_view_incomplete_json(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.put('/api/1.0/performanceassessmentrec/1/', {
            "employee_id": 1,
            "assessment_year": " ",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Bad",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_performanceassessmentrec_put_view_wrong_url(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        response = self.client.put('/api/1.0/performanceassessmentrec/4/', {
            "employee_id": 1,
            "assessment_year": "2019-2020",
            "assessment_status": 1,
            "overall_manager_comment": "Good",
            "overall_hod_comment": "Good",
            "overall_employee_comment": "Bad",
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GoalsTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'password': '1nn0vent3s'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_goals(self):
        return Goals.objects.create(description="Timepass",
                                    weightage="25",
                                    target_value=50,
                                    target_completion_date='2018-01-12',
                                    target_achieved_value=45,
                                    manager_comment="Good",
                                    achievment_comment="Good",
                                    performance_assessment_id=1,
                                    target_unit_id=1,
                                    self_rating_scale_id=1,
                                    manager_rating_scale_id=1
                                    )
    
    def test_create_performance_assessment_rec(self):
        return PerformanceAssessmentRec.objects.create(employee_id_id=1,
                                                       assessment_year='2018-2019',
                                                       assessment_status_id=1,
                                                       overall_manager_comment='Okay',
                                                       overall_hod_comment='Okay',
                                                       overall_employee_comment='Okay')

    def test_create_target_unit(self):
        return RefTargetUnit.objects.create(target_unit='days')

    def test_create_rating_scale(self):
        return RefRatingScale.objects.create(rating_value='Excellent')

    def test_goals(self):
        goals = self.test_create_goals()
        self.assertTrue(isinstance(goals, Goals))

    def test_goals_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/goals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_goals_list_view_wrong_url(self):
        self.test_login()
        response = self.client.get('/api/1.0/goal/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_goals_retrieve_view(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.get('/api/1.0/goals/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_goals_retrieve_view_wrong_id(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.get('/api/1.0/goals/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_goals_retrieve_view_wrong_url(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.get('/api/1.0/gols/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_goals_delete_view(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.delete('/api/1.0/goals/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_goals_delete_view_wrong_id(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.delete('/api/1.0/goals/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_goals_delete_view_wrong_url(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.delete('/api/1.0/gals/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performance_goals_list_view(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.get('/api/1.0/performanceassessmentrec/1/goals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_goals_list_view_wrong_id(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.get('/api/1.0/performanceassessmentrec/4/goals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_goals_list_view_wrong_url(self):
        self.test_login()
        self.test_create_goals()
        response = self.client.get('/api/1.0/performanceassessment/1/goals/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_goals_create_view(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.post('/api/1.0/goals/', json.dumps({
            "description": "Complete Task",
            "weightage": 25,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_goals_create_view_wrong_json(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.post('/api/1.0/goals/', json.dumps({
            "weightage": 25,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_goals_create_view_incomplete_json(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.post('/api/1.0/goals/', json.dumps({
            "weightage": 25,
            "target_value": 25,
            "target_completion_date": " ",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_goals_create_view_wrong_url(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.post('/api/1.0/goal/', json.dumps({
            "weightage": 25,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_goals_put_view(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.put('/api/1.0/goals/1/', {
            "description": "Complete Task",
            "weightage": 26,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_goals_put_view_wrong_json(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.put('/api/1.0/goals/1/', {
            "weightage": 26,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_goals_put_view_incomplete_json(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.put('/api/1.0/goals/1/', {
            "description": " ",
            "weightage": 26,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_goals_put_view_wrong_url(self):
        self.test_login()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_target_unit()
        self.test_create_rating_scale()
        response = self.client.put('/api/1.0/goal/1/', {
            "description": "Complete Task",
            "weightage": 26,
            "target_value": 25,
            "target_completion_date": "2019-01-09",
            "target_achieved_value": 25,
            "manager_comment": "Good",
            "achievment_comment": "Good",
            "performance_assessment": 1,
            "target_unit": 1,
            "self_rating_scale": 1,
            "manager_rating_scale": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-09",
            "deleted_date": None,
            "created_date": "2019-01-09"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class MilestonesTest(APITestCase):

    def setUp(self):
        self.credentials = {
            'username': 'innoventes',
            'password': '1nn0vent3s'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_create_milestones(self):
        return Milestone.objects.create(description="Timepass",
                                        target_value=50,
                                        target_completion_date='2018-10-12',
                                        achieved_target_value=45,
                                        goal_id=1
                                        )

    def test_create_goals(self):
        return Goals.objects.create(description="Timepass",
                                    weightage="25",
                                    target_value=50,
                                    target_completion_date='2018-01-12',
                                    target_achieved_value=45,
                                    manager_comment="Good",
                                    achievment_comment="Good",
                                    performance_assessment_id=1,
                                    target_unit_id=1,
                                    self_rating_scale_id=1,
                                    manager_rating_scale_id=1
                                    )

    def test_create_ref_preforamance_rec_status(self):
        return RefPerformanceRecStatus.objects.create(status_name='pending')

    def test_create_employee(self):
        return Employee.objects.create(employee_id='E001',
                                       first_name='abc',
                                       last_name='def',
                                       date_of_birth='2019-09-09',
                                       gender_id=1)

    def test_create_performance_assessment_rec(self):
        return PerformanceAssessmentRec.objects.create(employee_id_id=1,
                                                       assessment_year='2018-2019',
                                                       assessment_status_id=1,
                                                       overall_manager_comment='Okay',
                                                       overall_hod_comment='Okay',
                                                       overall_employee_comment='Okay')

    def test_milestones(self):
        milestones = self.test_create_milestones()
        self.assertTrue(isinstance(milestones, Milestone))

    def test_goals_list_view(self):
        self.test_login()
        response = self.client.get('/api/1.0/milestones/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_goals_list_view_wrong_url(self):
        self.test_login()
        response = self.client.get('/api/1.0/milestone/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_milestones_retrieve_view(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.get('/api/1.0/milestones/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_milestones_retrieve_view_wrong_id(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.get('/api/1.0/milestones/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_milestones_retrieve_view_wrong_url(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.get('/api/1.0/milestone/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_milestones_delete_view(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.delete('/api/1.0/milestones/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_milestones_delete_view_wrong_id(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.delete('/api/1.0/milestones/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_milestones_delete_view_wrong_url(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.delete('/api/1.0/milestone/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_performance_goals_list_view(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.get('/api/1.0/goals/1/milestones/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_goals_list_view_wrong_url(self):
        self.test_login()
        self.test_create_milestones()
        response = self.client.get('/api/1.0/goals/1/milestone/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_milestones_create_view(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        response = self.client.post('/api/1.0/milestones/', json.dumps({
            "description": "Complete Task 1-5",
            "target_value": 5,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_milestones_create_view_wrong_json(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        response = self.client.post('/api/1.0/milestones/', json.dumps({
            "target_value": 5,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_milestones_create_view_incomplete_json(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        response = self.client.post('/api/1.0/milestones/', json.dumps({
            "description": "Complete Task 1-5",
            "target_value": 5,
            "target_completion_date": " ",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_milestones_create_view_wrong_url(self):
        self.test_login()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_employee()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        response = self.client.post('/api/1/miestones/', json.dumps({
            "description": "Complete Task 1-5",
            "target_value": 5,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_milestones_put_view(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_milestones()
        response = self.client.put('/api/1.0/milestones/1/', {
            "description": "Complete Task 1-5",
            "target_value": 6,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_milestones_put_view_wrong_json(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_milestones()
        response = self.client.put('/api/1.0/milestones/1/', {
            "target_value": 6,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_milestones_put_view_incomplete_json(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_milestones()
        response = self.client.put('/api/1.0/milestones/1/', {
            "description": " ",
            "target_value": 6,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_milestones_put_view_wrong_url(self):
        self.test_login()
        self.test_create_employee()
        self.test_create_ref_preforamance_rec_status()
        self.test_create_performance_assessment_rec()
        self.test_create_goals()
        self.test_create_milestones()
        response = self.client.put('/api/1.0/mile/1/', {
            "description": "Complete Task 1-5",
            "target_value": 6,
            "target_completion_date": "2019-01-10",
            "achieved_target_value": 5,
            "goal": 1,
            "created_by": "system",
            "last_updated_by": "system",
            "deleted_status": False,
            "last_updated_date": "2019-01-10",
            "deleted_date": None,
            "created_date": "2019-01-10"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
