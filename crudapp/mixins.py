import json
from django.core.serializers import serialize
from django.http import HttpResponse

class SerializeMixin(object):
	def xyz(self, qs):
        # Line no 7 to 13 is for removing meta data which is privide by serialize function
		json_data = serialize('json', qs) #This json_data var contain extra data. serialize() gives the data with meta data. for clarity print(json_data)
		'''for getting the actual data we need to convert json to python dict '''
		pydata = json.loads(json_data) #pydata stores json data with extra meta data
		dict_list = []
		for each_obj in pydata:
			dict_obj = each_obj['fields'] # fields is a key which content only emp data
			dict_list.append(dict_obj)
		json_data2 = json.dumps(dict_list)
		return json_data2

		'''
		here we are using the for loop for removing meta data from employee obj multiple
		time , writing code is not a good programmer habit , so we will  be going now 
		mixin concept. Whose main advantage is : It reduces code redundancies. 
		It's a class . 
'''




class HttpResponseMixin(object):
	def return_to_http_response(self, json_data, status=200):
		return HttpResponse(json_data, content_type='Application/json', status=status)