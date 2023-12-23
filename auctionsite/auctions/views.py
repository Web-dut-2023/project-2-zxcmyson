from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from auctions import models
from django.contrib import messages
from datetime import datetime
import os

# Create your views here.
def index(request):
    goods = models.goods_list.objects.all()
    return render(request, "auctions/index.html",{'goods':goods})


def my_login(request):
    if request.method == "GET":
        return render(request, 'auctions/login.html')
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    user = authenticate(request, username=name, password=pwd)
    if user is not None:
            login(request, user) 
            return redirect('/auctions')
    data_list = models.Users.objects.all()
    for data in data_list:
        if data.username == name and data.password == pwd:
            request.session['username'] = data.username
            return redirect('/auctions')
    return render(request, 'auctions/login.html')

def logout_view(request):
    logout(request)
    return redirect('/auctions/')

def Register(request):
    if request.method=='GET':
        return render(request,'auctions/register.html')
    userid=request.POST.get('username')
    userpassword=request.POST.get('password')
    data_list = models.Users.objects.all()
    for data in data_list:
        if data.username == userid and data.password == userpassword:
            return render(request, 'auctions/register.html')
    user = models.Users(username=userid, password=userpassword)
    user.save()
    return redirect('/auctions/login')

def create(request):
    if request.method == 'GET':
        return render(request,"auctions/create_list.html")
    else:
        name=request.POST.get('name')
        category=request.POST.get('category')
        price=request.POST.get('price')
        intro=request.POST.get('introduction')
        image=request.FILES.get('picture')
        username = request.session.get('username')
        item = models.goods_list(name=name,category=category,price=price,introduction=intro,picture=image)
        item.save()
        price = models.price_list(name=name,pidname=username,price=price)
        price.save()
    return render(request,"auctions/create_list.html")

def Watch(request):
    goods = models.goods_list.objects.all()
    comments = models.comment.objects.all()
    if request.method == 'GET':
        return render(request,"auctions/watch_list.html",{'goods':goods})
    else:
        price=request.POST.get('price')
        if price:
             price = int(price)
        else :
             price = 0
        comment = request.POST.get('article')
        product_id = request.POST.get('product_id')
        good = models.goods_list.objects.get(id=product_id)
        pidname = request.session.get('username')
        name = good.name
        good_price=int(good.price)
        if price>=good_price:
            price_list = models.price_list.objects.get(name=good.name)
            price_list_price = int(price_list.price)
            if price >=price_list_price :
                            if pidname:
                                item = models.price_list(name=name,pidname=pidname,price=str(price))
                                item.save()
                                price_list.delete()
                            else:
                                return redirect('/auctions/login')
        comment = models.comment(name=name,commentname=pidname,article=comment)
        comment.save()

    return render(request,"auctions/watch_list.html",{
                                                      'comments':comments,
                                                      'goods':goods})

def categories(request):
    categories=models.goods_list.objects.all()
    type = request.POST.get('type')
    goods_list = models.goods_list.objects.all()
    goods = goods_list
    if type:
        goods = goods_list.filter(category=type)
    return render(request,"auctions/categories.html",{
                                                      'categories':categories,
                                                      'goods':goods})

def watch(request,good_id):
    good = models.goods_list.objects.get(id=good_id)
    username = request.session.get('username')
    user = models.Users.objects.get(username=username)
    if user.watch==good.name:
        user.watch=""
    else:
        user.watch=good.name
    user.save()
    return redirect('/auctions/watch_list')

def close(request,good_id):
    good = models.goods_list.objects.get(id=good_id)
    username = request.session.get('username')
    if good.publisher==username:
        price_list=models.price_list.objects.get(name=good.name)
        good.price=price_list.price
        good.name="已拍卖"
        good.save()
        price_list.delete()
    return redirect('/auctions/watch_list')