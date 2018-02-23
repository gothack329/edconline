from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response

# Create your views here.

def article(request):
    return HttpResponse('<p>Test</p>') 
