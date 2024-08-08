






#from django.http import HttpResponse

#def home(request):
 #   return HttpResponse("<h1>This is our Home page</h1>")

from employees.models import *

from django.shortcuts import render
def home(request):
  employeess= Employee.objects.all()
  context = {

 'employee':employeess,

  }


 # print(employess)
  return render( request, 'home.html',context)
