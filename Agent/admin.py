from django.contrib import admin
from .models import PredictAgent,Issue
# Register your models here.
admin.site.register(Issue)
admin.site.register(PredictAgent)