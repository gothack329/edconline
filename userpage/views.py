from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Template,Context,loader,defaultfilters
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from django.contrib import messages
from article.models import *

# Create your views here.

@login_required
@transaction.atomic
def profile(request, username):
    inst_user = User.objects.get(username=username)
    inst_profile = Profile.objects.get(user=inst_user)

    arts = Article.objects.filter(author_id=inst_profile)
    comments = Comment.objects.filter(user=inst_profile).filter(invalid='N')
    


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

    return render(request, 'userpage/profile.html', {'member':inst_user,'arts':arts,'comments':comments,'user_form': user_form,
'profile_form': profile_form})