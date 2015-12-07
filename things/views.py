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


#stats stuff

import collections
import numpy as np

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d



def display_stuff(request):

	
	
	l_list = LiveThings.objects.all()
	d_list = DeadThings.objects.all()
	all_list = Thing.objects.all()

	combined_list = []	


 	new_living_list = []
 	new_dead_list = []
 	new_all_list = []

	for item in l_list:
		new_living_list.append(item.thing.t_id)

	for item in d_list:
	    new_dead_list.append(item.thing.t_id)

	for item in all_list:
		new_all_list.append(item.t_id)

	#list of union of living owned and dead owned
	union_list = new_living_list + new_dead_list

	live_set = set(new_living_list)
	living_set_len = len(list(live_set))

	dead_set = set(new_dead_list)
	dead_set_len = len(list(dead_set))

	#unique set of the above
	union_set = set(union_list)

	#length of union set
	union_set_len = len(list(union_set))

	#set of universal things
	universal_set = set(new_all_list)

	#length of universal set
	universal_set_len = len(list(universal_set))


	ll = set(new_living_list)
	dd = set(new_dead_list)
	u = set(new_all_list)

	a = union_set_len
	b = universal_set_len
	c = living_set_len
	d = dead_set_len

	

	


	return render_to_response('base.html',{'a': a, 'b': b,'c':c,'d':d,}, context_instance=RequestContext(request))

	#words = "apple banana apple strawberry banana lemon"
	#words = re.findall(r'\w+', words)
	#d = collections.Counter(words).most_common(1)

    ########
	#calculate top 100 code
	'''

    l_list = LiveThings.objects.all()
	d_list = DeadThings.objects.all()
	combined_list = []	

	for item in l_list:
		combined_list.append(item)

	for item in d_list:
		combined_list.append(item)

 	new_list = []
 	#cnt = Counter()

	for item in combined_list:
		new_list.append(item.thing.t_id)


	a = dict(collections.Counter(new_list).most_common(100))
	d = collections.OrderedDict(sorted(a.items(), key=lambda t: t[1]))


	'''
	##########
	# set of things owned only by the living/dead

	'''
	new_living_list = []
 	new_dead_list = []
 	

	for item in l_list:
		new_living_list.append(item.thing.t_id)

	for item in d_list:
	    new_dead_list.append(item.thing.t_id)

	ll = set(new_living_list)
	dd = set(new_dead_list)
	d = []
	d = list(ll - dd) '''
  

  #probabilities