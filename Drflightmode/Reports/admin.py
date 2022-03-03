from atexit import register
from django.contrib import admin

from Reports.models import PatientTestDetail

# Register your models here.

admin.site.register(PatientTestDetail)

# @register