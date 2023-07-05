from django.shortcuts import render,redirect
from .models import Registration
from django.contrib import messages,auth
from django.contrib .auth import authenticate

def Home(request):
    if request.user.is_authenticated:   
        return render(request,"Home.html")
    else:
        return render(request,"ulogin")
    
def ShopbyAgePage1(request):
    return render(request,'0-1year.html')

def ShopbyAgePage2(request):
    return render(request,'1-3year.html')

def ShopbyAgePage3(request):
    return render(request,'3+year.html')

def SchoolPage(request):
    return render(request,'School.html')

def AboutusPage(request):
    return render(request,"Aboutus.html")

def ContectPage(request):
    return render(request,"Contect.html")

def RegisterPage(request):
    return render(request,'Register.html')

def LoginPage(request):
    return render(request,'Login.html')

def Register2(request):
     if request.method=="POST":
        vfname=request.POST.get('fname')
        vlname=request.POST.get('lname')
        vuname=request.POST.get('uname')
        vemail=request.POST.get('email')
        vpasswd=request.POST.get('passwd')
        vcpasswd=request.POST.get('cpasswd')
        if vpasswd==vcpasswd:
            if Registration.objects.filter(username=vuname).exists():
                messages.success(request,"The username already registered here....")
                return redirect('/login')
            elif Registration.objects.filter(email=vemail).exists():
                 messages.success(request,'The Email addresssis already available')
                 return redirect('/login')  
            else:
                newuser=Registration()
                newuser.first_name=vfname
                newuser.last_name=vlname
                newuser.username=vuname
                newuser.email=vemail
                newuser.password=vpasswd
                newuser.save()
                return redirect('/login')         
            
def Userlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpasswd=request.POST.get('passwd')
        user=auth.authenticate(username=vuname,password=vpasswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return redirect('/home')
        
'''def LogOut(request):
    auth.logout(request)
    messages.success(request,"Successfully logged Out!!!")
    return redirect('/login')      '''

def LogOut(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/home")   