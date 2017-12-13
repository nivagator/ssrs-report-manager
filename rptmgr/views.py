from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.conf import settings
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ReportModelForm
from .models import Report

class ReportListView(ListView):
    template_name = 'rptmgr/index.html'
    context_object_name = 'latest_report_list'
    
    def get_queryset(self):
        return Report.objects.order_by('report_name')

class ReportDetailView(DetailView):
    print("class based ReportDetailView")
    model = Report
    template_name = 'rptmgr/report.html'

    # def get(self, request, *args, **kwargs):
    
    # def post(self, request, *args, **kwargs):
    # https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/#handling-forms-with-class-based-views


class ReportUpdateView(UpdateView):
    # model = Report
    queryset = Report.objects.all()
    form_class = ReportModelForm
    template_name = 'rptmgr/editreport.html'


# Create your views here.
# def index(request):
#     latest_report_list = Report.objects.order_by('report_name')
#     context = {
#         'latest_report_list': latest_report_list,
#     }
#     return render(request, 'rptmgr/index.html', context)

# CRUD - function and class based views
# Create/Retrieve/Update/Delete
# def report(request, report_id):
#     report = get_object_or_404(Report, pk=report_id)
#     context = {
#         'report': report,
#         'root_report_url': settings.SSRS_SERVER_BASE_URL
#     }
#     return render(request, 'rptmgr/report.html', context)
#     # return HttpResponse("You're looking at report ID #%s." % report_id)

def editreport(request, report_id):
    return HttpResponse("You're editing report ID #%s." % report_id)


