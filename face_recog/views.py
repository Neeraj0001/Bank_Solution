from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CreateUserForm,profile_form
from .models import Profile,Bank_Chit
from .decorator import allowed_user,admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            print('True')
            login(request,user)
            
            place = Profile.objects.get(user=user)
            
            print(place)
            x=str(place.id)
            print(x)
            return redirect('../user/'+x+'/')
        else:
            messages.info(request,'Usernaame Or Password is not correct')
    context={}
    return render(request,'login.html',context)
def registration(request):
    form=CreateUserForm()
    if request.method == 'POST' :
        print(request.POST)
        form=CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            
            group=Group.objects.get(name='user')
            user.groups.add(group)
            username=form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
                )
            messages.success(request,"Account Successfully created of "+username)
            return redirect('../login/')


            
    
    context={'form':form}
    return render(request,'registration.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['Admin'])
def a_dash(request):
    Bank_Chits=Bank_Chit.objects.all()
    context={'Bank':Bank_Chits}
    return render(request,'admin_dashboard.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['user'])
def user_form(request):
    user=request.user.profile
    
    form=profile_form(instance=user)
    if request.method == 'POST':
        form = profile_form(request.POST, request.FILES, instance=user)
        if form.is_valid():
           
            form.save()
            
            x=str(request.user.profile.id)
            return redirect('../user/'+x+'/')
    context={'form':form}
    return render(request,'update_form.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['user'])
def user(request,pk_test):
    pk_test=int(pk_test)
    profile=Profile.objects.get(id=pk_test)
    context={'profile':profile}
    return render(request,'user_dashboard.html',context)
def logoutUser(request):
    logout(request)
    return redirect('../login/')