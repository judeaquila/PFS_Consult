from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductIntakeForm

# Product Development
@login_required
def product_development(request):
    if request.method == 'POST':
        form = ProductIntakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ProductIntakeForm()

    context = {
        'form': form,
    }

    return render(request, 'services/product-development.html', context)