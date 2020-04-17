from django.contrib import admin

from .models import (
                        LeaveEligibility,
                        LeaveRevision,
                        LeaveRequest
                    )

admin.site.register(LeaveEligibility)
admin.site.register(LeaveRevision)
admin.site.register(LeaveRequest)