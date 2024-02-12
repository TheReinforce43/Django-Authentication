from django.shortcuts import render,redirect

from .forms import RegistrationForm,ChangeUserData
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def home(request):
    return render(request,'home.html')


def signup(request):

    if not request.user.is_authenticated:

        if request.method=='POST':
            form=RegistrationForm(request.POST)

            if form.is_valid():
                messages.success(request,'Account  Success mode')
                messages.warning(request,'Account warning mode')
                messages.info(request,'Account Info Mode')
                print(form.cleaned_data)
                form.save(commit=False)
        else :
            form=RegistrationForm()
        
        return render(request, 'signup.html',{'form':form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                Name=form.cleaned_data['username']
                UserPassword=form.cleaned_data['password']
                user_object=authenticate(username=Name,password=UserPassword)

                if user_object is not None:
                    login(request,user_object)
                    return redirect('profile')
        else :
            form=AuthenticationForm()
        return render(request, './login.html',{'form':form})
    else:
        return redirect('profile')


def profile(request):      

    if request.user.is_authenticated:
        if request.method=='POST':

            form=ChangeUserData(request.POST,instance=request.user) 

            if form.is_valid():
                messages.success(request,'Data Changed successfully!!')
               
                form.save()
                print(form.cleaned_data)
        else:
            form=ChangeUserData(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect('sign_up')

    



def user_logout(request):
    logout(request)
    return redirect('log_in')


def password_change(request):

    if request.method=='POST':

        form=PasswordChangeForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.cleaned_data['user'])
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)

    return render(request, 'password_change.html',{'form':form})
   


def pass_change_without_validation(request):

    if  request.user.is_authenticated:

        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        
        else:
            form=SetPasswordForm(user=request.user)
        
        return render(request,'pass_change_without_validation.html',{'form':form})
    
    else:
        return redirect('log_in')


# def ChangeDataUser(request):
#     if request.user.is_authenticated:

#         if request.method=='POST':

#             form=ChangeUserData(request.POST,instance=request.user) 

#             if form.is_vlaid():
#                 messages.success(request,'Data Changed successfully!!')
               
#                 form.save()
#                 print(form.cleaned_data)
#         else:
#             form=ChangeUserData()
#         return render(request,'profile.html/',{'form':form})
#     else:
#         return redirect('signup')


    
  

            
