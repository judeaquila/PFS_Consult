from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import EmailAuthenticationForm, CustomUserCreationForm, FDAApplicationForm, BusinessCertificateForm
from .models import FDAApplication, BusinessCertificateApplication, UserActivity


# Redirect for logged in users
def not_logged_in(user):
    return not user.is_authenticated


# Log In View
def login_view(request):
    storage = get_messages(request)
    for _ in storage:
        pass

    # Prevent logged in users from accessing login page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('user-dashboard')

    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in!")

            # Redirect user based on status
            if user.is_superuser or user.is_staff:
                return redirect('admin-dashboard')
            else:
                return redirect('user-dashboard')
    else:
        form = EmailAuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'registration/login.html', context)

# Sign Up View
def sign_up_view(request):
    # Prevent logged in users from accessing sign up page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('user-dashboard')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been successfully created!")
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
    messages.success(request, "Successfully logged out!")
    return redirect('home')


# USER DASHBOARD
@login_required
def user_dashboard(request):
    all_fda_applications = FDAApplication.objects.filter(user=request.user)
    product_total_count = all_fda_applications.count()
    product_pending_count = FDAApplication.objects.filter(user=request.user, application_status='pending').count()
    product_in_review_count = FDAApplication.objects.filter(user=request.user, application_status='in_review').count()
    product_completed_count = FDAApplication.objects.filter(user=request.user, application_status='completed_documentation').count()

    all_business_cert_applications = BusinessCertificateApplication.objects.filter(user=request.user)
    business_cert_total_count = all_business_cert_applications.count()
    business_cert_pending_count = BusinessCertificateApplication.objects.filter(user=request.user, application_status='pending').count()
    business_cert_in_review_count = BusinessCertificateApplication.objects.filter(user=request.user, application_status='in_review').count()
    business_cert_completed_count = BusinessCertificateApplication.objects.filter(user=request.user, application_status='completed_documentation').count()

    recent_activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')[:5]

    context = {
        'all_fda_applications': all_fda_applications,
        'product_total_count': product_total_count,
        'product_pending_count': product_pending_count,
        'product_in_review_count': product_in_review_count,
        'product_completed_count': product_completed_count,

        'business_cert_total_count': business_cert_total_count,
        'business_cert_pending_count': business_cert_pending_count,
        'business_cert_in_review_count': business_cert_in_review_count,
        'business_cert_completed_count': business_cert_completed_count,
        'all_business_cert_applications': all_business_cert_applications,

        'recent_activites': recent_activities,
    }

    return render(request, 'account/user-dashboard.html', context)


# CREATE FDA PRODUCT APPLICATION
@login_required
def create_fda_product_application(request):
    if request.method == 'POST':
        form = FDAApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            UserActivity.objects.create(
                user=request.user,
                activity_type='submit_product',
                description=f"Submitted FDA application for {application.business_name}"
            )

            messages.success(request, "Your FDA Application has been successfully submitted!")
            return redirect('fda-product-application-details', pk=application.pk)
        
    else:
        form = FDAApplicationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/fda-product-application.html', context)


# VIEW FDA PRODUCT APPLICATION
@login_required
def view_fda_product_application(request, pk):
    fda_application = get_object_or_404(FDAApplication, pk=pk, user=request.user)

    context = {
        'fda_application': fda_application,
    }

    return render(request, 'account/fda-product-application-details.html', context)

@login_required
def edit_fda_product_application(request, pk):
    fda_product_application = get_object_or_404(FDAApplication, id=pk)

    if request.method == 'POST':
        form = FDAApplicationForm(request.POST, request.FILES, instance=fda_product_application)

        if form.is_valid():
            form.save()
            messages.success(request, "Business Certificate Application details updated!")
            return redirect('business-cert-application-details', pk=fda_product_application.pk)
        
    else:
        form = BusinessCertificateForm(instance=fda_product_application)

    context = {
        'form': form,
        'fda_product_application': fda_product_application,
    }

    return render(request, 'account/edit-fda-product-application-details.html', context)


# ALL FDA APPLICATIONS
@login_required
def user_applications(request):
    fda_applications = FDAApplication.objects.filter(user=request.user)
    business_cert_applications = BusinessCertificateApplication.objects.filter(user=request.user)

    context = {
        'fda_applications': fda_applications,
        'business_cert_applications': business_cert_applications,
    }

    return render(request, 'account/all-user-applications.html', context)


# CREATE BUSINESS CERTIFICATE APPLICATION
@login_required
def create_business_cert_application(request):
    if request.method == 'POST':
        form = BusinessCertificateForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            UserActivity.objects.create(
                user=request.user,
                activity_type='submit_business',
                description=f"Submitted Business Certificate application for {application.business_name}"
            )

            messages.success(request, "Your Business Certificate Application has been successfully submitted!")
            return redirect('business-cert-application-details', pk=application.pk)
        
    else:
        form = BusinessCertificateForm()

    context = {
        'form': form,
    }

    return render(request, 'account/business-application.html', context)

@login_required
def view_business_cert_application(request, pk):
    business_cert_application = get_object_or_404(BusinessCertificateApplication, pk=pk, user=request.user)

    context = {
        'business_cert_application': business_cert_application,
    }

    return render(request, 'account/business-cert-application-details.html', context)


@login_required
def edit_business_cert_application(request, pk):
    business_cert_application = get_object_or_404(BusinessCertificateApplication, id=pk)

    if request.method == 'POST':
        form = BusinessCertificateForm(request.POST, instance=business_cert_application)

        if form.is_valid():
            form.save()
            messages.success(request, "Business Certificate Application details updated!")
            return redirect('business-cert-application-details', pk=business_cert_application.pk)
        
    else:
        form = BusinessCertificateForm(instance=business_cert_application)

    context = {
        'form': form,
        'business_cert_application': business_cert_application,
    }

    return render(request, 'account/edit-business-cert-application.html', context)

@login_required
def support_page(request):
    return render(request, 'account/user-support.html')

@login_required
def settings_page(request):
    return render(request, 'account/user-settings.html')