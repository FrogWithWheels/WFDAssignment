from django.contrib import admin
from Recruitment.models import Candidate
from Recruitment.models import Trainer

# registering models for admin control
admin.site.register(Candidate)
admin.site.register(Trainer)