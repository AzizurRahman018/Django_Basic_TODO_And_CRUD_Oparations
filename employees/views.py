from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from employees.models import Employee


     # def employee_detail(request,pk):
     #      try:
     #           empl= Employee.objects.get(pk=pk)
     #           context = {
     #           'emp':empl,

     #           }
     #           print(empl)
     #      except:
     #      raise Http404
     #      return render(request,'employee_detail.html',context)


def employee_detail(request,pk):
    
     empl= get_object_or_404(Employee,pk=pk)
     context = {
          'emp':empl,

     }
  
     return render(request,'employee_detail.html',context)
