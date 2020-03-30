from django.shortcuts import render
from django.views.generic import View
from crudapp.models import Employee
from django.http import HttpResponse
from crudapp.mixins import SerializeMixin
from crudapp.mixins import HttpResponseMixin
import json
from crudapp.utils import is_json
from crudapp.forms import EmployeeForm

# We can serialize python object in three differents method
# 1. by using json.dumps()
# 2. by using serialize()
# 3. by using serialization in rest_framework

'''for particular data by ID'''
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self, request,id, *args, **kwargs):
    	# Below 3 lines is main line others are for postmortem Retrive operation
    	# emp = Employee.objects.get(id=id)
    	# json_data= self.xyz([emp,])
    	# return HttpResponse(json_data, content_type='Application/json', status=200)
    	try:
    		emp = Employee.objects.get(id=id)
    	except Employee.DoesNotExist:
    		json_data = json.dumps({'msg':'Your requested resource is not available'})
    		return self.return_to_http_response(json_data, status=404)
    	else:
    		json_data= self.xyz([emp,])
    		return self.return_to_http_response(json_data)


'''for all data'''
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self, request, *args, **kwargs):
    	'''
    	# *** Serialize by Using Core Python by json.dumps()***
    	data = {
    		'name':'Dinga',
    		'college':'Vidyasagar uviversity',
    		'degree':'MCA',
    	}
    	json_data=json.dumps(data)
    	''' 
    	# *** Serialize by Using serialize() function which is import from django.core.serializers***
    	qs = Employee.objects.all()
    	
    	y= self.xyz(qs)

    	# return HttpResponse(json_data, content_type='Application/json')
    	return HttpResponse(y, content_type='Application/json')



    def post(self, request, *args, **kwargs):
        # json_data = json.dumps({'msg':'This is from post request'})
        # return self.return_to_http_response(json_data)

        ''' The below line is taking data from client application'''
        data = request.body # request.body receive the data from client application which is send by test.py
        valid_json = is_json(data) # This is_json method is written in utils.py
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data only'})
            return self.return_to_http_response(json_data, status=400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource created successfully'})
            return self.return_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.return_to_http_response(json_data, status=400)



        