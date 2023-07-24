from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import UserProfile, Post
from main.forms import UserProfileForm, PostForm
from django.contrib.auth.models import User

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

def logout_view(request):
    logout(request)
    return redirect('homepage') 

def Profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})

# class ProfileUpdateView(View):
#     def get(self, request, slug):
#         profile = get_object_or_404(UserProfile, user__username=slug)
#         form = ProfileForm(instance=profile)
#         context = {
#             'form': form
#         }
#         return render(request, 'edit.html', context)

#     def post(self, request, slug):
#         profile = get_object_or_404(UserProfile, user__username=slug)
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile', slug=slug)
#         return render(request, 'edit.html', {'form': form})

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

def homepage(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.user = request.user  
            post.save() 
            return redirect('homepage')

    else:
        form = PostForm()

    posts = Post.objects.all()
    users = User.objects.exclude(pk=request.user.pk)
    return render(request, 'homepage.html', {'form': form, 'posts': posts, 'users': users},)

def view_post(request):
    posts = Post.objects.all()
    return render(request,'ViewPost.html', {'posts': posts})
