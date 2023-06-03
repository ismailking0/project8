from django.shortcuts import render
from django.http import HttpResponse
from .models import models
from django.views import View
from .models import RegView
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class reg(View):
    def post(self,request):
        fname=request.POST['t1']
        lname=request.POST['t2']
        uname=request.POST['t3']
        pwd=request.POST['t4']
        cpwd=request.POST['t5']
        molno=request.POST['t6']
        email=request.POST['t7']
        r1=reg(fristname=fname,lastname=lname,username=uname,password=pwd,confirmpassword=cpwd,mobilenumber=molno,email=email)
        r1=save()
        return HttpResponse(" your registion succeful")



