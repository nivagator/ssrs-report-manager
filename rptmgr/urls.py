from django.urls import path

from .views import index, report, editreport

urlpatterns = [
    path('', index, name='index'),
    path('<int:report_id>/', report, name='report'),
    path('<int:report_id>/edit', editreport, name='editreport'),
]
