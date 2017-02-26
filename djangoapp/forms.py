from django import forms
from .models import Computers, OperatingSystem, ComputersAudit


class ComputerForm(forms.ModelForm):
	class Meta:
		model = Computers
		fields = ['computer_name', 'IP_address', 'MAC_address','Operating_system','users_name','location','Unit']
	
	def clean_computer_name(self): # Validates the Computer Name Field
		computer_name = self.cleaned_data.get('computer_name')
		if (computer_name == ""):
			raise forms.ValidationError('This field cannot be left blank')
		return computer_name

	def clean_IP_address(self): # Validates the IP_address
		IP_address = self.cleaned_data.get('IP_address')
		if (IP_address == ""):
			raise forms.ValidationError('This field cannot be left blank')

		if len(str(IP_address)) < 10:
			raise forms.ValidationError('IP Address is not valid. IP Address should be like 192.168.1.1')
		
		for objects in Computers.objects.all():
			if (objects.IP_address == IP_address):
				raise forms.ValidationError('This IP is already assigned to ' + objects.computer_name)
		return IP_address

class ComputerSearchForm(forms.ModelForm):
	class Meta:
		model = Computers
		fields = ['computer_name', 'IP_address', 'location', 'export_to_CSV']

class ComputerEditForm(forms.ModelForm):
	class Meta:
		model = Computers
		fields = ['computer_name', 'IP_address', 'MAC_address','Operating_system','users_name','location','Unit']


class OperatingSystemForm(forms.ModelForm):
	class Meta:
		model =  OperatingSystem
		fields = ['Operating_system']


class ComputerAuditSearchForm(forms.ModelForm):
	class Meta:
		model = ComputersAudit
		fields = ['computer_name', 'IP_address', 'location', 'export_to_CSV']