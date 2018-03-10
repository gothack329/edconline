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
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

@login_required
@transaction.atomic
def profile(request, username):
    inst_user = User.objects.get(username=username)
    inst_profile = Profile.objects.get(user=inst_user)

    arts = Article.objects.filter(author_id=inst_profile).filter(visible="Y")
    comments = Comment.objects.filter(user=inst_profile).filter(invalid='N')
    
    if username == request.user.username:
        # update profile 
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                #messages.success(request, '用户资料更新成功!')
                return redirect('.')

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

        # point record
        print(inst_user)
        point = Point.objects.filter(user=inst_user).order_by('-record_time')
        print(point)


        return render(request, 'userpage/profile.html', {'member':inst_user,'arts':arts,'comments':comments,'user_form': user_form,'profile_form': profile_form,'notice':msgs,'points':point,'unread':unread})
    else:    
        return render(request, 'userpage/profile.html', {'member':inst_user,'arts':arts,'comments':comments})



def userlogin(request):

    if request.method == 'POST':
        print(request.POST['referer'])
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
                return redirect(request.POST['referer'])
            else:
                errors.append('请输入正确的验证码！')
        else:
            errors.append('用户名不存在或密码错误!')
        return render(request, 'userpage/login.html', {'errors':errors})
    else:
        if 'HTTP_REFERER' in request.environ:
            refer = request.environ['HTTP_REFERER']
            if '/userpage/register/' not in refer:
                pass
            else:
                refer = '/'
        else:
            refer = '/'
        return render(request,'userpage/login.html',{'referer':refer})

def userlogout(request):
    logout(request)
    return redirect('/')

def register(request):
    errors = []
    if 'HTTP_REFERER' in request.environ:
        refer = request.environ['HTTP_REFERER']
        if '/userpage/register/' not in refer:
            pass
        else:
            refer = '/'
    else:
        refer = '/'
    if request.method == 'POST':
        # print(request.POST)
        obj = forms.RegisterForm(request.POST)
        post_check_code =  request.POST.get('check_code')
        session_check_code = request.session['check_code']

        if obj.is_valid():
            if post_check_code.lower() ==  session_check_code.lower():
            # values = obj.clean()
                data = obj.cleaned_data
                #print(data)
                username= data.get('username')
                password= data.get('pwd')
                email= data.get('email')
                User.objects.create(username=username,email = email )
                u = User.objects.get(username=username)
                u.set_password(password)
                u.save()

                point=10

                invite = request.GET.get('invite_code')
                if invite:
                    u_p = Profile.objects.get(invite_code=invite)
                    p = 5
                    Point.objects.create(user=u_p.user,point_record=p,event="invite")
                else:
                    p = 0


                point = point + p
                updatepoint = Point.objects.create(user=u,point_record=point,event="register")

                user = authenticate(request, username=username, password=password)
                login(request, user)

                return redirect(request.POST['referer'])
        else:
            errors = obj.errors
            print(errors)
    else:
        obj = forms.RegisterForm()
    return render(request,'userpage/register.html',{'form':obj,'referer':refer})

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'密码修改成功!')
        else:
            #print(form.errors.as_data())
            messages.error(request,form.errors.as_json())
            #print(dir(messages))
            pass
        return redirect('.')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'userpage/change.html',{'change_form':form})
    