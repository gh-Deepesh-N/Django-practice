from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        # Safely get form data using .get()
        # If a field is missing, it will return an empty string '' instead of crashing
        first_name = request.POST.get('firstname', '')  # get firstname, or '' if missing
        last_name = request.POST.get('lastname', '')    # get lastname, or '' if missing
        username = request.POST.get('username', '')     # get username, or '' if missing
        email = request.POST.get('email', '')          # get email, or '' if missing    
        password1 = request.POST.get('password1', '')   # get password, or '' if missing
        password2 = request.POST.get('password2', '')   # get confirm password, or '' if missing

        # Check if any field is empty (if any field contains just '')
        if not all([first_name, last_name, username, email, password1, password2]):
            return render(request, 'register.html', {'error': 'All fields are required'})

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'register.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, 'register.html', {'error': 'Email already exists'})
            else:
                user = User.objects.create_user(username=username, password=password1, 
                                              email=email, first_name=first_name, 
                                              last_name=last_name)
                user.save()
                return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid credentials')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Username and password are required')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)  # Redirect to home page after logout
    return redirect('/')
