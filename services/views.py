from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductIntake
from .forms import ProductIntakeForm
from django.contrib import messages

# Product Development
@login_required
def pd_home(request):
    pd_apps = ProductIntake.objects.filter(user=request.user)

    context = {
        'pd_apps': pd_apps,
    }

    return render(request, 'services/pd-home.html', context)

@login_required
def product_development(request):
    if request.method == 'POST':
        form = ProductIntakeForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Your Product Development Application has been successfully submitted!")
            return redirect('pd_thank_you', pk=application.pk)
    else:
        form = ProductIntakeForm()
    context = {
        'form': form,
    }
    return render(request, 'services/product-development.html', context)


@login_required
def product_development_details(request, pk):
    pd_app = get_object_or_404(ProductIntake, pk=pk, user=request.user)

    context = {
        'pd_app': pd_app,
        'GOAL_CHOICES': ProductIntake.GOALS_CHOICES,
        'TARGET_MARKET_CHOICES': ProductIntake.TARGET_MARKET_CHOICES,
        'PACKAGING_CHOICES': ProductIntake.PACKAGING_CHOICES,
        'MARKET_TESTING_CHOICES': ProductIntake.MARKET_TESTING_CHOICES,
    }
    return render(request, 'services/product-development-details.html', context)


@login_required
def product_development_update(request, pk):
    product = get_object_or_404(ProductIntake, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProductIntakeForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Development application details updated successfully!")
            return redirect('pd_applications')
    else:
        form = ProductIntakeForm(instance=product)
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'services/product-development-update.html', context)


@login_required
def product_development_delete(request, pk):
    product = get_object_or_404(ProductIntake, pk=pk, user=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product Development application deleted successfully!")
        return redirect('pd_applications')
    context = {
        'product': product,
    }
    return render(request, 'services/product-development-delete.html', context)


@login_required
def pd_thank_you(request, pk):
    product = get_object_or_404(ProductIntake, pk=pk, user=request.user)
    context = {
        'product': product,
    }
    return render(request, 'services/pd-submission-thank-you.html', context)