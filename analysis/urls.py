from django.urls import path
from .views import *

app_name = 'analysis'

urlpatterns = [
    path('reports', ReportView.as_view(), name='reports'),
    path('report/generate', GenerateReportView.as_view(), name='generate_report'),
]