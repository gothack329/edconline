from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.contrib import messages
from .models import *
from userpage.models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.

def detail(request, article_id):

    #if request.user.is_authenticated :# and request.user.has_perm('cmdb.permit')):
    #    username = request.user.username
    #else:
    #    username = None

    art = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('comment_time')
    errors = []


    if request.method == 'GET':
        art.readtime = art.readtime + 1
        art.save(update_fields=['readtime'])
        comment_form = CommentForm(instance=None)
    elif request.method == 'POST' and request.user.is_authenticated:
        #Profile.objects.get()
        comment_form = CommentForm(request.POST,instance=None)
        commenter = User.objects.get(pk=request.user.id)
        
        user_p = Profile.objects.get(user=commenter)
        if user_p.point < 1:
            errors.append('您没有足够的积分进行评论！')
        elif comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.ip = request.META['REMOTE_ADDR']
            instance.save()

            point=1
            author = User.objects.get(username=art.author_id.user.username)
            
            updatepoint = Point.objects.create(user=author,point_record=point,event="commented")
            updatepoint = Point.objects.create(user=commenter,point_record=-point,event="comment")


            return redirect('.')
        else:
            messages.error(request, comment_form.errors)

    else:
        comment_form = CommentForm(instance=None)
        errors.append('请先登录!')



    return render(request,'article/detail.html',{'art':art,'comments':comments,'comment_form':comment_form,'errors':errors})
    #return HttpResponse("You're looking at article %s." % article_id)


def publish(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES,instance=None)
        
        if article_form.is_valid():
            instance = article_form.save(commit=False)
            instance.ip = request.META['REMOTE_ADDR']
            art = instance.save()
  
            point=2
            u = User.objects.get(pk=request.user.id)
            updatepoint = Point.objects.create(user=u,point_record=point,event="publish")
            #updatepoint.save()

            return redirect('/article/%d/' % (instance.pk,))
        else:
            messages.error(request, article_form.errors)
    else:
        article_form = ArticleForm(instance=None)



    return render(request,'article/publish.html',{'article_form':article_form,'operation':'发布'})


@login_required
@transaction.atomic
def update(request, article_id):
    art = Article.objects.get(pk=article_id)
    if request.user.username == art.author_id.user.username:
        pass
    else:
        return redirect('/article/%d/' % (article_id,))

    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES,instance=art)

        if article_form.is_valid():
            instance = article_form.save(commit=False)
            instance.ip = request.META['REMOTE_ADDR']
            art = instance.save()
  
            return redirect('/article/%d/' % (article_id,))
        else:
            messages.error(request, article_form.errors)
    else:
        article_form = ArticleForm(instance=art)

    return render(request,'article/publish.html',{'article_form':article_form,'operation':'编辑'})













