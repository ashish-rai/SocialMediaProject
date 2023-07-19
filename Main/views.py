from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import UserProfile

User = get_user_model()

# Create your views here
@login_required
def Homepage(request):
    return render(request,'homepage.html')

def Signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = authenticate(username=username, password=password)
                login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = UserProfile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('homepage')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
    

def Login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'error': "Invalid Credential!!!"})
        
        login(request, user)
        return redirect('homepage')
    
    return render(request, 'login.html')

def Profile(request):
    current_user = request.user
    return render(request,'profile.html', {'user': current_user})

