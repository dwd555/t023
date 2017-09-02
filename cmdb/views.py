from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb.models import liuyan
import json,time
import logging; logging.basicConfig(level=logging.INFO)
# Create your views here.
def index(request):
	return render(request, "index.html")

def getData(request):
	if request.method=="GET":
		list=liuyan.objects.all()
		if len(list)==0:
			str=json.dumps({"data":"err"})
			return HttpResponse(str,content_type='application/json')
		# logging.info(list)
		ulist=[]
		for i in list:
			ulist.append({"name":i.name,"dateTime":i.dateTime,"content":i.content})

		logging.info(ulist)
		return HttpResponse(json.dumps({"data":ulist}),content_type='application/json')


def setData(request):
	if request.method=="POST":
		uname=request.POST.get("uname",None)
		content=request.POST.get("content",None)
		# if uname!=""or content!="":
		dateTime=time.time()
		liuyan.objects.create(name=uname,dateTime=dateTime,content=content)
		str=json.dumps({"data":"succ"})
		return HttpResponse(str,content_type='application/json')