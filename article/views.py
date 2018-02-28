from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.contrib import messages
from .models import *


# Create your views here.

def detail(request, article_id):

    #if request.user.is_authenticated :# and request.user.has_perm('cmdb.permit')):
    #    username = request.user.username
    #else:
    #    username = None

    art = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('comment_time')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST,instance=None)
        print(comment_form)
        
        
        instance = comment_form.save(commit=False)
        instance.ip = request.META['REMOTE_ADDR']

        instance.save()
        return redirect('.')
        #else:
        #    messages.error(request, 'Please correct the error below.')
    else:
        art.readtime = art.readtime + 1
        art.save(update_fields=['readtime'])
        comment_form = CommentForm(instance=None)


    return render(request,'article/detail.html',{'art':art,'comments':comments,'comment_form':comment_form})
    #return HttpResponse("You're looking at article %s." % article_id)


def publish(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,instance=None)
        
        if article_form.is_valid():
            instance = article_form.save(commit=False)
            instance.ip = request.META['REMOTE_ADDR']
            art = instance.save()
  

            return redirect('/article/%d/' % (instance.pk,))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        article_form = ArticleForm(instance=None)

    return render(request,'article/publish.html',{'article_form':article_form,'operation':'发布'})


def update(request, article_id):
    art = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,instance=art)

        if article_form.is_valid():
            instance = article_form.save(commit=False)
            instance.ip = request.META['REMOTE_ADDR']
            art = instance.save()
  
            return redirect('/article/%d/' % (article_id,))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        article_form = ArticleForm(instance=art)

    return render(request,'article/publish.html',{'article_form':article_form,'operation':'编辑'})













