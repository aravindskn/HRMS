from django.db import models

from ref_data_management.models import (
                                            AbstractBaseModel,
                                            RefLeaveType,
                                            RefLeaveRequestStatus,
                                            RefLeaveRevisionType
                                       )

from employee_management.models import Employee


class LeaveRevision(AbstractBaseModel):
    """
        This model provides representation of Leave Eligibility
        attributes:
            number_of_days = Integer Field, mandatory
            revision_type = ForeignKey(RefLeaveRevisionType), mandatory
            leave_type = ForeignKey(RefLeaveType), mandatory
    """
    number_of_days = models.CharField(max_length=255, null=False, blank=False, verbose_name='Number of days')

    leave_type = models.ForeignKey(
                                        RefLeaveType,
                                        null=False,
                                        blank=False,
                                        on_delete=models.PROTECT,
                                        verbose_name='Leave type',
                                        related_name='revision_leave_types'
                                  )

    revision_type = models.ForeignKey(
                                            RefLeaveRevisionType,
                                            null=False,
                                            blank=False,
                                            on_delete=models.PROTECT,
                                            verbose_name='Revision type',
                                            related_name='revision_leave_types'
                                     )

    def __str__(self):
        return '{}, {}'.format(self.number_of_days, self.leave_type)

    class Meta:
        db_table = 'leave_revision'


class LeaveEligibility(AbstractBaseModel):
    """
        This model provides representation of Leave Eligibility
        attributes:
            number_of_days = Integer Field, mandatory
            employee = ForeignKey(Employee), mandatory
            leave_type = ForeignKey(RefLeaveType), mandatory
    """
    number_of_days = models.ForeignKey(
                                            LeaveRevision,
                                            null=False,
                                            blank=False,
                                            on_delete=models.PROTECT,
                                            verbose_name='Number of days',
                                            related_name='leave_eligibility'
                                        )

    employee = models.ForeignKey(
                                        Employee,
                                        null=False,
                                        blank=False,
                                        on_delete=models.PROTECT,
                                        verbose_name='Employee id',
                                        related_name='leave_eligibility'
                                )

    leave_type = models.ForeignKey(
                                        RefLeaveType,
                                        null=False,
                                        blank=False,
                                        on_delete=models.PROTECT,
                                        verbose_name='Leave type',
                                        related_name='leave_types'
                                  )

    def __str__(self):
        return '{}, {}'.format(self.leave_type, self.employee)

    class Meta:
        db_table = 'leave_eligibility'


class LeaveRequest(AbstractBaseModel):
    """
        This model provides representation of Leave Requests
        attributes:
            leave_start_date = Date Field, mandatory
            leave_end_date = Date Field, mandatory
            comments = TextField, optional
            employee = ForeignKey(Employee), mandatory
            leave_type = ForeignKey(RefLeaveType), mandatory
            leave_request_status = ForeignKey(RefLeaveRequestStatus), mandatory
    """
    leave_start_date = models.DateField(null=False, blank=False, verbose_name='Leave start date')
    leave_end_date = models.DateField(null=False, blank=False, verbose_name='Leave end date')
    comments = models.TextField(null=True, blank=True, verbose_name='Comments')

    employee = models.ForeignKey(
                                    Employee,
                                    null=False,
                                    blank=False,
                                    on_delete=models.PROTECT,
                                    verbose_name='Employee ID',
                                    related_name='leave_requests'
                                )

    request_status = models.ForeignKey(
                                            RefLeaveRequestStatus,
                                            null=False,
                                            blank=False,
                                            on_delete=models.PROTECT,
                                            verbose_name='Request status',
                                            related_name='leave_requests'
                                      )

    leave_type = models.ForeignKey(
                                    RefLeaveType,
                                    null=False,
                                    blank=False,
                                    on_delete=models.PROTECT,
                                    verbose_name='Leave type',
                                    related_name='request_leave_types'
                                  )

    def __str__(self):
        return '{}, {}'.format(self.employee, self.leave_type)

    class Meta:
        db_table = 'leave_request'