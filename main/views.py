from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from account.models import CustomUser, FDAApplication, BusinessCertificateApplication
from account.forms import FDAApplicationForm, BusinessCertificateForm
from itertools import chain
from django.contrib import messages

# Home Page
def home(request):
    return render(request, 'main/index.html')

# FDA Services Page
def fda_services(request):
    return render(request, 'main/fda-services.html')

# Other Services Page
def other_services(request):
    return render(request, 'main/other-services.html')

# Redirect to Login Page
def login_redirect(request):
    return render(request, 'main/redirect-to-login.html')



# ADMIN DASHBOARD
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_dashboard(request):
    all_users = CustomUser.objects.all()
    all_users_count = all_users.count()

    all_fda_product_applications = FDAApplication.objects.all()
    all_business_cert_applications = BusinessCertificateApplication.objects.all()

    all_fda_product_applications_count = all_fda_product_applications.count()
    all_business_cert_applications_count = all_business_cert_applications.count()
    total_submissions = all_fda_product_applications_count + all_business_cert_applications_count

    pending_fda_product_applications = all_fda_product_applications.filter(application_status='pending')
    pending_busines_cert_applications = all_business_cert_applications.filter(application_status='pending')

    pending_fda_product_applications_count = pending_fda_product_applications.count()
    pending_busines_cert_applications_count = pending_busines_cert_applications.count()
    total_pending = pending_busines_cert_applications_count + pending_fda_product_applications_count

    in_review_fda_product_applications = all_fda_product_applications.filter(application_status='in_review')
    in_review_busines_cert_applications = all_business_cert_applications.filter(application_status='in_review')

    in_review_fda_product_applications_count = in_review_fda_product_applications.count()
    in_review_busines_cert_applications_count = in_review_busines_cert_applications.count()
    total_in_review = in_review_busines_cert_applications_count + in_review_fda_product_applications_count

    complete_documentation_fda_product_applications = all_fda_product_applications.filter(application_status='completed_documentation')
    complete_documentation_busines_cert_applications = all_business_cert_applications.filter(application_status='completed_documentation')

    complete_documentation_fda_product_applications_count = complete_documentation_fda_product_applications.count()
    complete_documentation_busines_cert_applications_count =     complete_documentation_busines_cert_applications.count()
    total_completed_documentation = complete_documentation_fda_product_applications_count + complete_documentation_busines_cert_applications_count

    approved_fda_product_applications = FDAApplication.objects.filter(application_status='approved')
    approved_busines_cert_applications = BusinessCertificateApplication.objects.filter(application_status='approved')
    approved_fda_product_applications_count = approved_fda_product_applications.count()
    approved_busines_cert_applications_count = approved_busines_cert_applications.count()
    total_approved = approved_fda_product_applications_count + approved_busines_cert_applications_count

    rejected_fda_product_applications = FDAApplication.objects.filter(application_status='rejected')
    rejected_busines_cert_applications = BusinessCertificateApplication.objects.filter(application_status='rejected')
    rejected_fda_product_applications_count = rejected_fda_product_applications.count()
    rejected_busines_cert_applications_count = rejected_busines_cert_applications.count()
    total_rejected = rejected_fda_product_applications_count + rejected_busines_cert_applications_count


    all_applications = sorted(
        chain(all_fda_product_applications, all_business_cert_applications),
        key=lambda application: application.submitted_at,
        reverse=True
    )[:10]

    context = {
        'all_users': all_users,
        'all_users_count': all_users_count,
        'all_fda_product_applications': all_fda_product_applications,
        'all_fda_product_applications_count': all_fda_product_applications_count,
        'all_business_cert_applications': all_business_cert_applications,
        'all_business_cert_applications_count': all_business_cert_applications_count,
        'total_submissions': total_submissions,
        'pending_fda_product_applications': pending_fda_product_applications,
        'pending_fda_product_applications_count': pending_fda_product_applications_count,
        'pending_business_cert_applications': pending_busines_cert_applications,
        'pending_business_cert_applications_count': pending_busines_cert_applications_count,
        'total_pending': total_pending,
        'in_review_fda_product_applications': in_review_fda_product_applications,
        'in_review_busines_cert_applications': in_review_busines_cert_applications,
        'in_review_fda_product_applications_count': in_review_fda_product_applications_count,
        'in_review_busines_cert_applications_count': in_review_busines_cert_applications_count,
        'total_in_review': total_in_review,
        'complete_documentation_fda_product_applications': complete_documentation_fda_product_applications,
        'complete_documentation_busines_cert_applications': complete_documentation_busines_cert_applications,
        'complete_documentation_fda_product_applications_count': complete_documentation_fda_product_applications_count,
        'complete_documentation_busines_cert_applications_count': complete_documentation_busines_cert_applications_count,
        'total_completed_documentation': total_completed_documentation,
        'approved_fda_product_applications': approved_fda_product_applications,
        'approved_busines_cert_applications': approved_busines_cert_applications,
        'approved_fda_product_applications_count': approved_fda_product_applications_count,
        'approved_busines_cert_applications_count': approved_busines_cert_applications_count,
        'total_approved': total_approved,
        'rejected_fda_product_applications': rejected_fda_product_applications,
        'rejected_busines_cert_applications': rejected_busines_cert_applications,
        'rejected_fda_product_applications_count': rejected_fda_product_applications_count,
        'rejected_busines_cert_applications_count': rejected_busines_cert_applications_count,
        'total_rejected': total_rejected,

        'all_applications': all_applications,
    }

    return render(request, 'main/admin-dashboard.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_business_cert_application_details(request, pk):
    business_cert_application = get_object_or_404(BusinessCertificateApplication, id=pk)

    context = {
        'business_cert_application': business_cert_application,
    }

    return render(request, 'main/business-cert-application-details.html', context)

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_fda_product_application_details(request, pk):
    fda_product_application = get_object_or_404(FDAApplication, id=pk)

    context = {
        'fda_product_application': fda_product_application,
    }

    return render(request, 'main/fda-product-application-details.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_admin_business_cert_application_details(request, pk):
    business_cert_application = get_object_or_404(BusinessCertificateApplication, id=pk)

    if request.method == 'POST':
        form = BusinessCertificateForm(request.POST, instance=business_cert_application)

        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
        
    else:
        form = BusinessCertificateForm(instance=business_cert_application)
    
    context = {
        'form': form,
        'business_cert_application': business_cert_application,
    }

    return render(request, 'main/edit-business-cert-application-details.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_admin_fda_product_application_details(request, pk):
    fda_product_application = get_object_or_404(FDAApplication, id=pk)

    if request.method == 'POST':
        form = FDAApplicationForm(request.POST, request.FILES, instance=fda_product_application)

        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
        
    else:
        form = FDAApplicationForm(instance=fda_product_application)

    context = {
        'form': form,
        'fda_product_application': fda_product_application,
    }

    return render(request, 'main/edit-fda-product-application-details.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def change_business_cert_application_status(request, pk, new_status):
    application = get_object_or_404(BusinessCertificateApplication, pk=pk)
    allowed_statuses = ['pending', 'in_review', 'completed_documentation', 'approved', 'rejected']

    if new_status in allowed_statuses:
        application.application_status = new_status
        application.save()
        return redirect('admin-business-cert-application-details', pk=pk)
    return render(request, 'main/business-cert-application-details.html')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def change_fda_product_application_status(request, pk, new_status):
    application = get_object_or_404(FDAApplication, pk=pk)
    allowed_statuses = ['pending', 'in_review', 'completed_documentation', 'approved', 'rejected']

    if new_status in allowed_statuses:
        application.application_status = new_status
        application.save()
        return redirect('admin-fda-product-application-details', pk=pk)
    return render(request, 'main/fda-product-application-details.html')


# USER MANAGEMENT
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def manage_users(request):
    users = CustomUser.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'main/manage_users.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def add_user(request):
    if request.method == 'POST':
        data = request.POST
        user = CustomUser.objects.create_user(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data.get('last_name', ''),
            phone_number=data.get('phone_number', ''),
            whatsapp_number=data.get('whatsapp_number', ''),
            instagram_handle=data.get('instagram_handle', ''),
            facebook_handle=data.get('facebook_handle', ''),
            company_name=data.get('company_name', ''),
            password='defaultpassword123'
        )
        messages.success(request, f"{user.first_name}'s account has been created successfully.")
        return redirect('manage-users')
    
    return render(request, 'main/manage_users.html')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        data = request.POST
        user.first_name = data['first_name']
        user.last_name = data.get('last_name', '')
        user.username = data['username']
        user.email = data['email']
        user.phone_number = data.get('phone_number', '')
        user.whatsapp_number = data.get('whatsapp_number', '')
        user.instagram_handle = data.get('instagram_handle', '')
        user.facebook_handle = data.get('facebook_handle', '')
        user.company_name = data.get('company_name', '')
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('manage-users')
    
    return render(request, 'main/manage_users.html')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('manage-users')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def toggle_user_active(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    user.is_active = not user.is_active
    user.save()
    state = "activated" if user.is_active else "deactivated"
    messages.success(request, f'User {state} successfully.')
    return redirect('manage-users')