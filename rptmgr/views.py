from django.shortcuts import render, get_object_or_404, redirect
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


# class ReportUpdateView(View):
#     # https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/#handling-forms-with-class-based-views
#     def get(self, request, *args, **kwargs):
#         form = ReportModelForm()
#         queryset = Report.objects.all()
#         context = {
#             "form": form,
#             "queryset": queryset,
#             # "pk":pk
#         }
#         template_name = 'rptmgr/editreport.html'
#         return render(request, template_name, context)

#     def post(self, request, *args, **kwargs):
#         pass


class ReportCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ReportModelForm()
        context = {
            "form": form,
            "title": "Create New Report", 
            "value_text": "Create",
        }
        return render(request, "rptmgr/editreport.html", context)

    def post(self, request, *args, **kwargs):
        form = ReportModelForm(request.POST)
        context = {
            "form": form,
            "title": "New Report Created", 
            "value_text": "Create",
        }
        template = "rptmgr/editreport.html"
        if form.is_valid():
            cl_report_name = form.cleaned_data.get("report_name")
            cl_report_file_name = form.cleaned_data.get("report_file_name")
            cl_base_url = form.cleaned_data.get("base_url")
            cl_active = form.cleaned_data.get("active")
            obj, created = Report.objects.get_or_create(report_name=cl_report_name,report_file_name=cl_report_file_name,base_url=cl_base_url,active=cl_active)
            if created:
                # print(obj.id)
                context = {
                    "object": obj,
                    "created": created,
                }   
                
                # template = "rptmgr/index.html"
                return redirect("rptmgr:report", pk=obj.id)
            else:
                print("not created")
                return render(request, template, context)




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


