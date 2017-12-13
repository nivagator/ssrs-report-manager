from django import forms

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