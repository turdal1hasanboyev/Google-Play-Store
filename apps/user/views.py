from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from .models import CustomUser


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        image = request.FILES.get('image')
        bio = request.POST.get('bio')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            image=image,
            bio=bio,
        )
        user.save()
        messages.success(request, 'Account created successfully')
        login(request, user)
        return redirect('user_profile')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('user_profile')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home_page')
