from article.models import *
from userpage.models import *


def settings(request):
    secs = Section.objects.all()
    if request.user.is_authenticated:
        userid = request.user.id
        user =Profile.objects.get(user=userid)

        return {'secs':secs,'user':user} 
    else:
        return {'secs':secs}