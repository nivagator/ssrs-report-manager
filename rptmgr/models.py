from django.db import models

# Create your models here.

class Report(models.Model):
    report_name = models.CharField(max_length=100, null=False, blank=False)
    report_file_name = models.CharField(max_length=1000, null=False, blank=False)
    base_url = models.CharField(max_length=1000, null=False, blank=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.report_name)

    class Meta:
        ordering = ['report_name']
