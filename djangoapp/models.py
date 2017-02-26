from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class OperatingSystem(models.Model):
		Operating_system = models.CharField(max_length=200, default='', blank=True, null=True)
		def __unicode__(self):
			return self.Operating_system 


class Computers(models.Model):
    computer_name = models.CharField(max_length=30, blank=True, null=True)
    IP_address = models.CharField(max_length=30, blank=True, null=True)
    MAC_address = models.CharField(max_length=30, blank=True, null=True)
    Operating_system = models.ForeignKey(OperatingSystem, blank=True, null=True)
    users_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    unit_choice = (
            ('IT Unit', 'IT Unit'),
            ('HR Unit', 'HR Unit'),
            ('Accounting Unit', 'Accounting Unit'),
            ('Treasury Unit', 'Treasury Unit'),
		)
    Unit = models.CharField(max_length=50, default='', blank=True, null=True, choices=unit_choice)
    added_by = models.CharField(max_length=30, blank=True, null=True)
    edited_by = models.CharField(max_length=30, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    date_edited = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
		return self.computer_name

    def get_absolute_url(self):
		return reverse("computer_edit", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("computer_delete", kwargs={"id": self.id})


class ComputersAudit(models.Model):
    computer_name = models.CharField(max_length=30, blank=True, null=True)
    IP_address = models.CharField(max_length=30, blank=True, null=True)
    MAC_address = models.CharField(max_length=30, blank=True, null=True)
    Operating_system = models.ForeignKey(OperatingSystem, blank=True, null=True)
    users_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    unit_choice = (
            ('IT Unit', 'IT Unit'),
            ('HR Unit', 'HR Unit'),
            ('Accounting Unit', 'Accounting Unit'),
            ('Treasury Unit', 'Treasury Unit'),
        )
    Unit = models.CharField(max_length=50, default='', blank=True, null=True, choices=unit_choice)
    added_by = models.CharField(max_length=30, blank=True, null=True)
    edited_by = models.CharField(max_length=30, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    date_edited = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __unicode__(self):
        return self.computer_name