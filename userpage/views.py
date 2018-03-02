from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from django.contrib import messages
from article.models import *
from notification.models import *
from . import forms
from django.contrib.auth import authenticate, login

# Create your views here.

@login_required
@transaction.atomic
def profile(request, username):
    inst_user = User.objects.get(username=username)
    inst_profile = Profile.objects.get(user=inst_user)

    arts = Article.objects.filter(author_id=inst_profile)
    comments = Comment.objects.filter(user=inst_profile).filter(invalid='N')
    
    if username == request.user.username:
        # update profile 
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
    
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                #messages.success(request, '用户资料更新成功!')
                return redirect('.')
                #return redirect('settings:profile')
            else:
                messages.error(request, user_form.errors)
                #messages.error(request, _('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        # end update profile
    
        # notification
        msgs = Msg.objects.filter(mention_user=inst_profile).order_by('-comment_time')
        for i in msgs:
            i.unread='N'
            i.save()
        unread = inst_profile.unread
        inst_profile.unread=0
        inst_profile.save()
        # end notification


        return render(request, 'userpage/profile.html', {'member':inst_user,'arts':arts,'comments':comments,'user_form': user_form,'profile_form': profile_form,'notice':msgs,'unread':unread})
    else:    
        return render(request, 'userpage/profile.html', {'member':inst_user,'arts':arts,'comments':comments})



def userlogin(request):

    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        errors = []

        post_check_code = request.POST.get('check_code')
        session_check_code = request.session['check_code']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if post_check_code.lower() == session_check_code.lower() :
                login(request, user)
                if request.POST.get('auto_login'):
                    request.session.set_expiry(60 * 60 * 24 *30)
                return redirect('/')
            else:
                errors.append('请输入正确的验证码！')
        else:
            errors.append('用户名不存在或密码错误!')
        return render(request, 'userpage/login.html', {'errors':errors})
    else:
        return render(request,'userpage/login.html')

def logout(request):
    try:
        #删除is_login对应的value值
        del request.session['is_login']
        del request.session['user']
    except KeyError:
        pass
    #点击注销之后，直接重定向回登录页面
    return redirect('/')

def register(request):
    # username = models.CharField(max_length=16, verbose_name='用户名')
    # password = models.CharField(max_length=16, verbose_name='密码')
    # nickname = models.CharField(max_length=16,verbose_name='昵称')
    # email = models.EmailField(max_length=16, verbose_name='邮箱')
    # img = models.ImageField(verbose_name='头像',upload_to='static/img/user/',default='static/img/user/1.jpg')
    # ctime = models.DateTimeField(auto_created=True,verbose_name='创建时间')

    if request.method == 'GET':
        obj = forms.Register()
        # return render(request,'register.html',{'form':obj})
    elif request.method == 'POST':
        # print(request.POST)
        obj = forms.Register(request.POST)
        post_check_code =  request.POST.get('check_code')
        session_check_code = request.session['check_code']
        print(post_check_code,session_check_code)
        if obj.is_valid():
            if post_check_code ==  session_check_code:
            # values = obj.clean()
                data = obj.cleaned_data
                print(data)
                # models.User.objects.create(
                username= data.get('username')
                password= data.get('pwd')
                email= data.get('email')
                nickname = data.get('username')
                # )
                models.User.objects.create(username=username,nickname =nickname,password =password,email = email )
                request.session['is_login'] = 'true'
                request.session['user'] = data.get('username')
                return redirect('/')
        else:
            errors = obj.errors
            print('hello')

    return render(request,'userpage/register.html',{'form':obj})















