from django.shortcuts import render

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