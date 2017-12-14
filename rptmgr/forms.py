from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Report

class ReportModelForm(forms.ModelForm):
    # content = forms.CharField(
    #     label=''
    # )
    class Meta:
        model = Report
        fields = [
            'report_name',
            'report_file_name',
            'base_url',
            'active'
        ]
        labels ={
            'report_name': _('Report Name'),
            'report_file_name': _('Report File Name'),
            'base_url': _('Base Url'),
        }