from article.models import *
from userpage.models import *


def settings(request):
	secs = Section.objects.all()
	return {'secs':secs} 