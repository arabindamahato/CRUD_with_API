from django import forms
from crudapp.models import Employee

class EmployeeForm(forms.ModelForm):
	def clean_esal(self): # when you call is_valid internally clean_esal is called
		inputsal = self.cleaned_data['esal']
		if inputsal<5000:
			raise forms.ValidationError('The minimum salary should be 5000')
		return inputsal

	class Meta:
		model = Employee
		fields = '__all__'