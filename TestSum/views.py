from django.shortcuts import render
from django.shortcuts import render , redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import FieldDoesNotExist
from django.db import IntegrityError
# Create your views here.

from django.views.generic import View
from .models import Student
from django.http import HttpResponse,QueryDict

class TestSum(View):

    def get(self, request):
        try:
            p1 = request.GET['p1']
            p2 = request.GET['p2']
            result = int(p1) + int(p2)
            r2= int(p1)-int(p2)
            r3= int(p1)*int(p2)
            r4= int(p1)/int(p2)
            return HttpResponse('sum is : ' + str(result) + 'Difference is :' + str(r2) + 'Product is :' + str(r3) + 'Division is : ' + str(r4), status=200)
        except Exception as exception:
            print str(exception)
            return HttpResponse("Internal Server Error", status=500)
from TestSum.models import Student

class Studentdata(View):

    def get(self,request):
        result=[]
        students=Student.objects.all()
        for student in students:
            res={}
            res['rollno']=student.rollno
            res['first_name']=student.first_name
            res['last_name']=student.last_name
            res['Mobile_number']=student.Mobile_number
            res['Address']=student.Address
            res['College']=student.College
            result.append(res)
        return HttpResponse(result,status = 200)

class Updatedata(View):

    def post(self,request):
     try:
        rollno=request.POST["rollno"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        Mobile_number=request.POST["Mobile_number"]
        Address=request.POST["Address"]
        College=request.POST["College"]

        student_info=Student(rollno=rollno,first_name=first_name,last_name=last_name,
        Mobile_number=Mobile_number,Address=Address,College=College)
        student_info.save()
        return HttpResponse(request)
     except IntegrityError:
        return HttpResponse("IntegrityError")

class Deleterecord(View):

   def delete(self,request,id):
     try:
       ##rollno=request.POST["rollno"]
       #instance=Student.objects.get["id"]
       ##instance.delete()
       Student.objects.get(id=id).delete()
       #Student.objects.filter(rollno=rollno).delete()
       ##Student.save()
       return HttpResponse("Delete Successful")
     except ObjectDoesNotExist:
       return HttpResponse("Object Does Not Exist")

class Changedata(View):

    def put(self,request,id):
        #update=request.POST["rollno"]
        #r1=request.POST["College"]
        #instance=Student.objects.get(rollno=update)
     try:
        data=QueryDict(request.body)
        update_data=Student.objects.get(id=id)



        if data.get('first_name'):
           update_data.first_name=data.get('first_name')
        if(data.get('last_name')):
           update_data.last_name=data.get('last_name')
        if(data.get('Mobile_number')):
           update_data.Mobile_number=data.get('Mobile_number')
        if(data.get('Address')):
           update_data.Address=data.get('Address')
        if(data.get('College')):
           update_data.College=data.get('College')
        update_data.save()
        return HttpResponse("Updation Successful")
     except ObjectDoesNotExist:
        return HttpResponse("Object Does Not Exist")




        #instance=Student.objects.filter(rollno=update).update(College=r1)
