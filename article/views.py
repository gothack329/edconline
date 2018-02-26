from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response
from django.contrib import messages
from .models import *

# Create your views here.

def homepage(request):
    return render(request,'base.html') 


def detail(request, article_id):
    art = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('comment_time')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST,instance=None)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        comment_form = CommentForm(instance=None)

    secs = Section.objects.all()

    return render(request,'article/detail.html',{'art':art,'comments':comments,'comment_form':comment_form,'secs':secs})
    #return HttpResponse("You're looking at article %s." % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on article %s." % article_id)
