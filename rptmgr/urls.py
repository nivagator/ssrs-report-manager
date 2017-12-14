from django.urls import path

from .views import (
    ReportListView,
    ReportDetailView, 
    ReportUpdateView,
    ReportCreateView,
    editreport
)

app_name = 'rptmgr'
urlpatterns = [
    path('', ReportListView.as_view(), name='index'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report'),
    path('new/', ReportCreateView.as_view(), name='newreport'),
    path('<int:pk>/edit', ReportUpdateView.as_view(), name='editreport'),
]
