# imports
from django.contrib import admin
from .models import UserModel
from .models import Candidate

# registering models for admin control
admin.site.register(Candidate)