from article.models import *
from userpage.models import *


def settings(request):
    if request.user.is_authenticated :
        userid = request.user.id
    user =Profile.objects.get(user=userid)
    secs = Section.objects.all()
    return {'secs':secs,'user':user} 