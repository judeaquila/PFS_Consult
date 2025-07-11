from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import user_passes_test
from account.models import CustomUser, FDAApplication, BusinessCertificateApplication, FDAFoodRequirement
from .models import FAQ
from .forms import FAQForm
from services.models import ProductIntake
from account.forms import FDAApplicationForm, BusinessCertificateForm, CustomUserUpdateForm
from itertools import chain
from django.contrib import messages

# Home Page
def home(request):
    faqs = FAQ.objects.filter(is_active=True)
    context = {
        'faqs': faqs,
    }
    # Prevent logged in users from accessing home page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('user-dashboard')
        
    return render(request, 'main/index.html', context)

# FDA Services Page
def fda_services(request):
    # Prevent logged in users from accessing FDA services page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('user-dashboard')
        
    return render(request, 'main/fda-services.html')


# FDA Rates Page
def fda_rates(request):
    # Prevent logged in users from accessing FDA rates page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('user-dashboard')
        
    return render(request, 'main/fda-rates.html')

# Other Services Page
def other_services(request):
    # Prevent logged in users from accessing Other services page
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('user-dashboard')
        
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

    # Product Development
    pd_apps = ProductIntake.objects.all()
    pd_apps_count = pd_apps.count()
    pd_apps_pending = pd_apps.filter(application_status='pending').count()
    pd_apps_in_review = pd_apps.filter(application_status='in_review').count()
    pd_apps_completed = pd_apps.filter(application_status='completed_documentation').count()
    pd_apps_approved = pd_apps.filter(application_status='approved').count()
    pd_apps_rejected = pd_apps.filter(application_status='rejected').count()

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
        # Product Development
        'pd_apps_count': pd_apps_count,
        'pd_apps_pending': pd_apps_pending,
        'pd_apps_in_review': pd_apps_in_review,
        'pd_apps_completed': pd_apps_completed,
        'pd_apps_approved': pd_apps_approved,
        'pd_apps_rejected': pd_apps_rejected,
    }

    return render(request, 'main/admin-dashboard.html', context)


# FAQs
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def faq_list(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'main/faqs_list.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def faq_add(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a FAQ!')
            return redirect('admin-faq-list')
    else:
        form = FAQForm()
    context = {
        'form': form,
    }
    return render(request, 'main/faq_form.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def faq_edit(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ edited successfully!')
            return redirect('admin-faq-list')
    else:
        form = FAQForm(instance=faq)
    context = {
        'form': form,
    }
    return render(request, 'main/faq_edit.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    faq.delete()
    return redirect('admin-faq-list')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def toggle_faq_active(request, pk):
    faq = get_object_or_404(FAQ, id=pk)
    faq.is_active = not faq.is_active
    faq.save()
    state = "activated" if faq.is_active else "deactivated"
    messages.success(request, f'FAQ {state} successfully.')
    return redirect('admin-faq-list')


# SETTINGS
def admin_settings(request):
    return render(request, 'main/admin-settings.html')

# BUSINESS CERTIFICATE APPLICATIONS
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_business_cert_application_details(request, pk):
    business_cert_application = get_object_or_404(BusinessCertificateApplication, id=pk)

    context = {
        'business_cert_application': business_cert_application,
    }

    return render(request, 'main/business-cert-application-details.html', context)


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
def change_business_cert_application_status(request, pk, new_status):
    application = get_object_or_404(BusinessCertificateApplication, pk=pk)
    allowed_statuses = ['pending', 'in_review', 'completed_documentation', 'approved', 'rejected']

    if new_status in allowed_statuses:
        application.application_status = new_status
        application.save()
        return redirect('admin-business-cert-application-details', pk=pk)
    return render(request, 'main/business-cert-application-details.html')


# FDA PRODUCT APPLICATIONS
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def fda_food_checklist(request):
    submissions = FDAFoodRequirement.objects.all().order_by('-submitted_at')
    context = {
        'submissions': submissions,
    }
    return render(request, 'main/admin-fda-food-checklist.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_fda_product_application_details(request, pk):
    fda_product_application = get_object_or_404(FDAApplication, id=pk)

    context = {
        'fda_product_application': fda_product_application,
    }

    return render(request, 'main/fda-product-application-details.html', context)


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
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('manage-users')
    else:
        form = CustomUserUpdateForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'main/edit-users.html', context)


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



################## SERVICES #######################
# 1. BUSINESS CERTIFICATE
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_business_cert_application_details(request, pk):
    business_cert_application = get_object_or_404(BusinessCertificateApplication, id=pk)
    context = {
        'business_cert_application': business_cert_application,
    }
    return render(request, 'main/business-cert-application-details.html', context)


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
def change_business_cert_application_status(request, pk, new_status):
    application = get_object_or_404(BusinessCertificateApplication, pk=pk)
    allowed_statuses = ['pending', 'in_review', 'completed_documentation', 'approved', 'rejected']
    if new_status in allowed_statuses:
        application.application_status = new_status
        application.save()
        return redirect('admin-business-cert-application-details', pk=pk)
    return render(request, 'main/business-cert-application-details.html')


# 2. FDA PRODUCT APPLICATION
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_fda_product_application_home(request):
    fda_prod_apps = FDAApplication.objects.all().order_by('-submitted_at')
    query = request.GET.get('q') or ''
    if query:
        fda_prod_apps = fda_prod_apps.filter(custom_id__icontains=query)
    context = {
        'fda_prod_apps': fda_prod_apps,
        'query': query,
    }
    return render(request, 'main/admin-fda-product-application-home.html', context)


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
def admin_fda_product_application_details(request, pk):
    fda_product_application = get_object_or_404(FDAApplication, id=pk)
    context = {
        'fda_product_application': fda_product_application,
    }
    return render(request, 'main/fda-product-application-details.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def change_fda_product_application_status(request, pk, new_status):
    application = get_object_or_404(FDAApplication, pk=pk)
    allowed_statuses = ['pending', 'in_review', 'completed_documentation', 'approved', 'rejected']
    if new_status in allowed_statuses:
        application.application_status = new_status
        application.save()
        return redirect('admin-fda-product-application-details', pk=pk)
    return render(request, 'main/fda-product-application-details.html')


# 3. PRODUCT DEVELOPMENT
def admin_pd_home(request):
    pd_apps = ProductIntake.objects.all().order_by('-submitted_at')
    query = request.GET.get('q') or ''
    if query:
        pd_apps = pd_apps.filter(custom_id__icontains=query)
    context = {
        'pd_apps': pd_apps,
        'ProductIntake': ProductIntake,
        'query': query,
    }
    return render(request, 'main/admin-pd-home.html', context)


def admin_pd_details(request, pk):
    pd_app = get_object_or_404(ProductIntake, pk=pk)
    context = {
        'pd_app': pd_app,
        'GOAL_CHOICES': ProductIntake.GOALS_CHOICES,
        'TARGET_MARKET_CHOICES': ProductIntake.TARGET_MARKET_CHOICES,
        'PACKAGING_CHOICES': ProductIntake.PACKAGING_CHOICES,
        'MARKET_TESTING_CHOICES': ProductIntake.MARKET_TESTING_CHOICES,
    }
    return render(request, 'main/admin-pd-details.html', context)


def admin_pd_app_status_change(request, pk):
    pd_app = get_object_or_404(ProductIntake, pk=pk)
    if request.method == 'POST':
        app_id = pd_app.custom_id
        update_status = request.POST.get("application_status")
        pd_app.application_status = update_status
        pd_app.save()
        messages.success(request, f"{app_id} status changed to {pd_app.get_application_status_display()}!")
        return redirect('admin_pd_home')
    

def admin_pd_payment_status_change(request, pk):
    pd_app = get_object_or_404(ProductIntake, pk=pk)
    if request.method == 'POST':
        app_id = pd_app.custom_id
        update_payment_status = request.POST.get("payment_status")
        pd_app.payment_status = update_payment_status
        pd_app.save()
        messages.success(request, f"{app_id} payment status changed to {pd_app.get_payment_status_display()}")
        return redirect('admin_pd_home')


def admin_pd_delete(request, pk):
    pd_app = get_object_or_404(ProductIntake, pk=pk)
    if request.method == 'POST':
        pd_app.delete()
        messages.success(request, f"Successfully deleted application { pd_app.custom_id }")
        return redirect('admin_pd_home')


def download_pd_pdf(request, pk):
    pd_app = get_object_or_404(ProductIntake, pk=pk)
    template_path = 'main/pdf_template.html'
    context = {
        'pd_app': pd_app,
        'GOAL_CHOICES': ProductIntake.GOALS_CHOICES,
        'TARGET_MARKET_CHOICES': ProductIntake.TARGET_MARKET_CHOICES,
        'PACKAGING_CHOICES': ProductIntake.PACKAGING_CHOICES,
        'MARKET_TESTING_CHOICES': ProductIntake.MARKET_TESTING_CHOICES,
    }
    response = HttpResponse(content_type='pd_app/pdf')
    response['Content-Disposition']=f'attachment; filename="pd_app_{pk}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors with PDF generation.")
    return response