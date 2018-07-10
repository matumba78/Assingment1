from django.conf.urls import url
#from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from views import TestSum
from views import Studentdata
from views import Updatedata
from views import Deleterecord,Changedata

urlpatterns = [

	url(r'^sum/$', TestSum.as_view(),name='test-sum'),
	url(r'^update/',Studentdata.as_view(),name='s'),
	url(r'^create/',Updatedata.as_view(),name='biju-bro'),
	url(r'^delete/(?P<id>\d+)$',Deleterecord.as_view(),name='d'),
	url(r'^change/(?P<id>\d+)$',Changedata.as_view(),name='bij'),
	]
