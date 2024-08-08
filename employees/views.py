from django.http import Http404, HttpResponse
from django.shortcuts import render

from employees.models import Employee


def employee_detail(request,pk):
     try:
          empl= Employee.objects.get(pk=pk)
          print(empl)
     except:
        raise Http404
     return HttpResponse(empl)
