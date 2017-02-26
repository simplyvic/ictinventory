from django.shortcuts import render, redirect
from .forms import ComputerForm, ComputerSearchForm, ComputerEditForm, OperatingSystemForm, ComputerAuditSearchForm
from .models import Computers, ComputersAudit
from django.shortcuts import get_object_or_404
from django.contrib import messages
import csv
from django.http import HttpResponse


def home(request):
	title = 'FOR AUTHORIZED XYZ COMPANY STAFFS ONLY'
	context = {
		"title": title,
	}
	if request.user.is_authenticated():
		title = 'Welcome: ' + str(request.user)
		context = {
		"title": title,
	}
	return render(request, "base.html",context)

def computer_entry(request):
	title = 'Add Computer'
	form = ComputerForm(request.POST or None) #(this form has to be imported from .forms)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.added_by = str(request.user)
		instance.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/computer_list')
	context = {
		"title": title,
		"form": form,
	}		
	return render(request, "computer_entry.html",context)


def computer_list(request):
	title = 'List Of Computers'
	queryset = Computers.objects.all().order_by('-id')
	form = ComputerSearchForm(request.POST or None)
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		}
	if request.method == 'POST':
			queryset = Computers.objects.all().order_by('-id').filter(computer_name__icontains=form['computer_name'].value(), IP_address__icontains=form['IP_address'].value(), location__icontains=form['location'].value())
			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			}
	if form['export_to_CSV'].value() == True:
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="Computers.csv"'
		writer = csv.writer(response)
		writer.writerow(['computer_name', 'IP_address', 'MAC_address', 'users_name','location', 'timestamp'])
		instance = queryset 
		for row in instance:
			writer.writerow([row.computer_name , row.IP_address , row.MAC_address, row.users_name, row.location, row.timestamp])
		return response
	return render(request, "computer_list.html",context)


def computer_edit(request, id=None):	
	instance = get_object_or_404(Computers, id=id)
	form = ComputerEditForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		for objects in Computers.objects.all():
			if (objects.computer_name != instance.computer_name):
				print 'Computer' 

			# if (objects.IP_address != instance.IP_address):
			# 	print 'IP Address'
		
			# if (objects.MAC_address != instance.MAC_address):
			# 	print 'MAC Address' 
			
			# if (objects.Operating_system != instance.Operating_system):
			# 	print 'OS' 
				
			# if (objects.users_name != instance.users_name):
			# 	print 'User' 
				
			# if (objects.location != instance.location):
			# 	print 'Location' 
			
			# if (objects.Unit != instance.Unit):
			# 	print 'Unit' 

			if (
				objects.computer_name != instance.computer_name or 
				objects.IP_address != instance.IP_address or 
				objects.MAC_address != instance.MAC_address or 
				objects.Operating_system != instance.Operating_system or 
				objects.users_name != instance.users_name or 
				objects.location != instance.location or 
				objects.Unit != instance.Unit
				):
				instance.edited_by = str(request.user)
				instance.save()
				messages.success(request, 'Successfully Saved')
			return redirect('/computer_list')
	context = {
			"title": 'Edit ' + str(instance.computer_name),
			"instance": instance,
			"form": form,
		}
	return render(request, "computer_edit.html", context)

def computer_delete(request, id=None):
	instance = get_object_or_404(Computers, id=id)
	instance.delete()
	messages.error(request, 'Successfully deleted')
	return redirect("computer_list")


def computer_audit(request):
	title = 'List of computers'
	queryset = ComputersAudit.objects.all().order_by('id')
	form = ComputerAuditSearchForm(request.POST or None)
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
		}
	if request.method == 'POST':
			queryset = ComputersAudit.objects.all().order_by('id').filter(computer_name__icontains=form['computer_name'].value(), IP_address__icontains=form['IP_address'].value(), location__icontains=form['location'].value())
			context = {
			"title": title,
			"queryset": queryset,
			"form": form,
			}
	if form['export_to_CSV'].value() == True:
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="Computers.csv"'
		writer = csv.writer(response)
		writer.writerow(['computer_name', 'IP_address', 'MAC_address', 'users_name','location', 'timestamp'])
		instance = queryset 
		for row in instance:
			writer.writerow([row.computer_name , row.IP_address , row.MAC_address, row.users_name, row.location, row.timestamp])
		return response
	return render(request, "computer_audit.html",context)


def settings(request):
	title = 'Add IP Address'
	form = OperatingSystemForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/computer_list')
	context = {
		"title": title,
		"form": form,
	}		
	return render(request, "settings.html",context)

