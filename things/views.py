from django.shortcuts import render

from things import models    

#importing necessities
from django.template import Context, loader
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.core.files.uploadedfile import SimpleUploadedFile
	
from django.core import serializers
from django.shortcuts import render, get_object_or_404



from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder



from django.forms import ModelForm


from django.core import serializers


from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


import re
import json 
import decimal
import time

from datetime import date 
from datetime import datetime, timedelta




#from things : model imports
from things.models import Thing
from things.models import Person
from things.models import LivePeople
from things.models import DeadPeople
from things.models import LiveThings
from things.models import DeadThings
from things.models import Holder



class objectview(object):
    def __init__(self, d):
        self.__dict__ = d



def display_stuff(request):


	new_list = Holder.objects.all()
	#things_list = []
	for item in new_list:
		string_value = str(item.value)
		string_value = string_value.replace(' ', '')
		string_value = string_value.replace('\n', '')
		string_list = re.split(";", string_value)
		#p=DeadPeople.objects.create(p_id=string_list[0], age_at_death=string_list[1])
		#p.save() 
	    
	things_list = DeadPeople.objects.all()

	'''for item in new_list:
		value = {'p_id':"b>"+str(item.t_id)+"<b"}
		new_entry = objectview(value)
		things_list.append(value)'''
	


	size = len(things_list)


	return render_to_response('base.html',{ 'things_list' : things_list, 'size': size ,}, context_instance=RequestContext(request))