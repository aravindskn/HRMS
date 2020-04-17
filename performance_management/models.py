"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/performance_management/models.py
    Description: This module contains all model definitions that are common across the different
    categories of entities in hrms application.
--------------------------------------------------------------------------------------------------
"""
from django.db import models
from employee_management.models import Employee
from ref_data_management.models import (AbstractBaseModel,
                                             RefRatingScale,
                                             RefTargetUnit,
                                             RefPerformanceRecStatus)


class PerformanceAssessmentRec(AbstractBaseModel):
    """
        This module defines all the attributes in Performance Assessment Records entity.
        Attributes:
            employee_id (ForeignKey(Employee), mandatory): Employee ID.
            assessment_year (CharField, mandatory) : Year of Assessment.
            assessment_status (CharField, mandatory): Status of the performance assessment.
            overall_manager_comment (TextField, mandatory): Manager's comment on the assessment.
            overall_hod_comment (TextField, manadatory): HOD's comment on the assessment.
            overall_employee_comment (TextField, mandatory): Employee's comment on the assessment.
    """
    employee_id = models.ForeignKey(Employee,
                                    null=False,
                                    blank=False,
                                    verbose_name='Employee ID',
                                    related_name='employee',
                                    on_delete=models.PROTECT)
    assessment_year = models.CharField(max_length=255, null=False, blank=False, verbose_name='Assessment year')
    assessment_status = models.ForeignKey(RefPerformanceRecStatus,
                                          null=False,
                                          blank=False,
                                          verbose_name='Performance Status',
                                          related_name='performance_status',
                                          on_delete=models.PROTECT)
    overall_manager_comment = models.TextField(null=False, blank=False, verbose_name='Overall manager comment')
    overall_hod_comment = models.TextField(null=False, blank=False, verbose_name='Overall HOD comment')
    overall_employee_comment = models.TextField(null=False, blank=False, verbose_name='Overall employee comment')

    def __str__(self):
        """
            The string function returns employee's ID, year of assessment, status of the assessment.
        """
        return '{}, {}, {}'.format(self.employee_id, self.assessment_year, self.assessment_status)

    class Meta:
        db_table = 'hrms_performance_assessment_rec'


class Goals(AbstractBaseModel):
    """
        This module defines all the attributes in Goals entity.
        Attributes:
            description (TextField, mandatory): Description.
            weightage (IntegerField, mandatory): Weightage.
            target_value (IntegerField, mandatory): Target value.
            target_completion_date (DateField, mandatory): Target Completion Date.
            target_achieved_value (IntegerField, mandatory): Target Achieved Value.
            manager_comment (TextField, mandatory): Manager Comment.
            achievement_comment (TextField, mandatory): Achievment comment.
            performance_assessment (ForeignKey(PerformanceAssessmentRec), mandatory): Performance Assessment.
            target_unit (ForeignKey(RefTargetUnit), mandatory): Target Unit.
            self_rating_scale (ForeignKey(RefRatingScale), mandatory): Self Rating Scale.
            manager_rating_scale (ForeignKey(RefRatingScale), mandatory): Manager Rating Scale.
    """
    description = models.TextField(null=False, blank=False, verbose_name='Description')
    weightage = models.IntegerField(null=False, blank=False, verbose_name='Weightage(%)')
    target_value = models.IntegerField(null=False, blank=False, verbose_name='Target value')
    target_completion_date = models.DateField(null=False, blank=False, verbose_name='Target completion date')
    target_achieved_value = models.IntegerField(null=False, blank=False, verbose_name='Target achieved value')
    manager_comment = models.TextField(null=False, blank=False, verbose_name='Manager comment')
    achievment_comment = models.TextField(null=False, blank=False, verbose_name='Achievment comment')
    performance_assessment = models.ForeignKey(PerformanceAssessmentRec,
                                               null=False,
                                               blank=False,
                                               verbose_name='Performance assessment',
                                               on_delete=models.PROTECT,
                                               related_name='performanceassessment')
    target_unit = models.ForeignKey(RefTargetUnit,
                                    null=False,
                                    blank=False,
                                    verbose_name='Target unit',
                                    on_delete=models.PROTECT,
                                    related_name='targetunit')
    self_rating_scale = models.ForeignKey(RefRatingScale,
                                          null=False,
                                          blank=False,
                                          verbose_name='Self rating scale',
                                          on_delete=models.PROTECT,
                                          related_name='selfratingscale')
    manager_rating_scale = models.ForeignKey(RefRatingScale,
                                             null=False,
                                             blank=False,
                                             verbose_name='Manager rating scale',
                                             on_delete=models.PROTECT,
                                             related_name='managerratingscale')

    def __str__(self):
        """
            This method returns performance assessment id, goal id and the description of the goal.
        """
        return '{},{},{}'.format(self.performance_assessment, self.id, self.description)

    class Meta:
        db_table = 'hrms_goals'


class Milestone(AbstractBaseModel):
    """
        This module defines all the attributes in Milestone entity.
        Attributes:
            description (TextField, mandatory): Description.
            target_value (IntegerField, mandatory): Targeted Amount to be Achieved.
            target_completion_date (DateField, mandatory): Date of completion of the target.
            achieved_target_value (IntegerField, mandatory): Achieved Target Value.
            goal (ForeignKey(Goal), mandatory): The goal to which the milestone is of.
    """
    description = models.TextField(null=False, blank=False, verbose_name='Description')
    target_value = models.IntegerField(null=False, blank=False, verbose_name='Target value')
    target_completion_date = models.DateField(null=False, blank=False, verbose_name='Target completion date')
    achieved_target_value = models.IntegerField(null=False, blank=False, verbose_name='Achieved target value')
    goal = models.ForeignKey(Goals,
                             null=False,
                             blank=False,
                             verbose_name='Goal',
                             on_delete=models.PROTECT,
                             related_name='goals')

    def __str__(self):
        """
            This method returns goal id, milestone id and description of the milestone.
        """
        return '{},{},{}'.format(self.goal, self.id, self.description)

    class Meta:
        db_table = 'hrms_milestone'
