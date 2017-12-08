from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Report

# Create your views here.
def index(request):
    latest_report_list = Report.objects.order_by('report_name')
    context = {
        'latest_report_list': latest_report_list,
    }
    return render(request, 'rptmgr/index.html', context)

# CRUD - function and class based views
# Create/Retrieve/Update/Delete
def report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    context = {
        'report': report
    }
    return render(request, 'rptmgr/report.html', context)
    # return HttpResponse("You're looking at report ID #%s." % report_id)

def editreport(request, report_id):
    return HttpResponse("You're editing report ID #%s." % report_id)