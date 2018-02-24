from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response

# Create your views here.

def homepage(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

