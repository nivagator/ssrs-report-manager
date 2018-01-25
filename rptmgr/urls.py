from django.urls import path

from .views import (
    ReportListView,
    ReportDetailView, 
    ReportUpdateView,
    ReportCreateView,
    editreport,
    report_update_view
)

app_name = 'rptmgr'
urlpatterns = [
    path('', ReportListView.as_view(), name='index'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report'),
    path('new/', ReportCreateView.as_view(), name='newreport'),
    path('<id>/edit', report_update_view, name='editreport'),
]
