from django.shortcuts import render
from utils import check_code
from io import BytesIO
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def create_code_img(request):
   f = BytesIO() #直接在内存开辟一点空间存放临时生成的图片

   img, code = check_code.create_validate_code() #调用check_code生成照片和验证码
   request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
   img.save(f,'PNG') #生成的图片放置于开辟的内存中
   png = f.getvalue()

   return HttpResponse(f.getvalue(),content_type='image/png')  #将内存的数据读取出来，并以HttpResponse返回

