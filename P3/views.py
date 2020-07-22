from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>welcome to P3</marquee>")
 
def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={"data":"Yoki","name":"Yokesh"})
    
def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{"fruits":fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':50})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def ac(request,ac):
    a=ac.split(" ")
    sum = int(a[0]) + int(a[1])
    return HttpResponse(str(sum))

def grt(request,grt):
    b = grt.split(" ")
    if int(b[0]) > int(b[1]):
        return HttpResponse(str(b[0]))
    else:
        return HttpResponse(str(b[1]))

def vowel(request,str):
    vow = 'aeiouAEIOU'
    v = 0
    c = 0
    for i in str:
        if i in vow:
            v+=1
        else:
            c+=1
    return render(request,"directory/vowel.html", context={'a':v, 'b':c})