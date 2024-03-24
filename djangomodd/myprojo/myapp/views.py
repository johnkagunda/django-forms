from django.http import HttpResponse
from django.template import loader
from .models import Member
import requests
from django.shortcuts import render

from myapp.forms import Formy


def input_form(request):
  form= Formy()
  

  return render(request,'home.html',{'form':form})





def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))




