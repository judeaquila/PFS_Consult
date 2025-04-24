from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmailAuthenticationForm, CustomUserCreationForm, FDAApplicationForm
from .models import FDAApplication

# Log In View
def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user-dashboard')
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
            return redirect('user-dashboard')
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


# USER DASHBOARD
@login_required
def user_dashboard(request):
    return render(request, 'account/user-dashboard.html')

@login_required
def create_fda_application(request):
    if request.method == 'POST':
        form = FDAApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('user-dashboard')
        
    else:
        form = FDAApplicationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/fda-application.html', context)

@login_required
def view_fda_application(request, pk):
    fda_application = get_object_or_404(FDAApplication, pk=pk, user=request.user)

    context = {
        'fda_application': fda_application,
    }

    return render(request, 'account/fda-application-details.html', context)