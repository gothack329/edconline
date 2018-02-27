from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.contrib import messages
from .models import *

# Create your views here.

def homepage(request):
    return render(request,'base.html') 


def detail(request, article_id):

    if request.user.is_authenticated :# and request.user.has_perm('cmdb.permit')):
        username = request.user.username
    else:
        username = None

    art = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('comment_time')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST,instance=None)
        comment_form.save()
        if comment_form.is_valid():
            return redirect('.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        comment_form = CommentForm(instance=None)

    secs = Section.objects.all()

    return render(request,'article/detail.html',{'username':username,'art':art,'comments':comments,'comment_form':comment_form,'secs':secs})
    #return HttpResponse("You're looking at article %s." % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on article %s." % article_id)
