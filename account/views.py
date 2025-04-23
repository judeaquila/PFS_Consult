from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import EmailAuthenticationForm, CustomUserCreationForm

# Log In View
def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = EmailAuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'registration/login.html', context)

# Sign Up View
def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/signup.html', context)

# Log Out View
def logout_view(request):
    logout(request)
    return redirect('home')