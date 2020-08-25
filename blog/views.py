from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from blog.models import User, Blog, Comment


def hello(request):



    return HttpResponse('hello world')


def login(request):
    data={
        'msg':None,
        'code':200
    }
    if request.method=='GET':
        return render(request, 'html/login.html')
    if request.method=='POST':
        name=request.POST.get('username')
        user=User.objects.filter(name=name).first()
        if user:
            password=request.POST.get('password')
            if user.password==password:
                request.session['id']=user.id
                return redirect(reverse('blog:main'))
            data['msg']='密码错误'
            data['code']=101
            return render(request,'html/login.html',context=data)
        data['msg']='用户名不存在'
        data['code']=100
        return render(request, 'html/login.html', context=data)


def register(request):
    if request.method=='GET':
        return render(request, 'html/register.html')
    if request.method=='POST':
        name=request.POST.get('username')
        passwrod=request.POST.get('password')
        User.objects.get_or_create(name=name,password=passwrod)
        return redirect(reverse('blog:login'))


def main(request):
    data={}
    id=request.session.get('id')
    user=User.objects.get(id=id)
    blogs=Blog.objects.all()



    return render(request,'html/main.html',context=locals())
    # return redirect(reverse('blog:login'))


def add_blog(request):
    if request.method=='GET':
        return render(request, 'html/main.html')
    content=request.POST.get('blog_content')
    id=request.session.get('id')
    Blog.objects.create(content=content,user_id_id=id)
    return redirect(reverse('blog:main'))


def comment(request):
    id=request.session.get('id')
    review=request.POST.get('review')
    b_id=request.POST.get('b_id')
    Comment.objects.create(review=review,c_blog_id=b_id,c_user_id=id)
    return redirect(reverse('blog:main'))
