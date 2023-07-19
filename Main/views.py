from django.shortcuts import render, redirect

# Create your views here.
def Homepage(request):
    return render(request,'homepage.html')

def Signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        print(username, email, password1, password2)
        return redirect('homepage')

    return render(request,'signup.html')

def Login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return redirect('homepage')
    return render(request, 'login.html')

def Profile(request):
    current_user = request.user
    return render(request,'profile.html', {'user': current_user})

