from django.db import models

from django.db.models import Q

from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import App
from apps.review.models import Review
from apps.category.models import Category
from apps.user.models import CustomUser


def home_page(request):
    apps = App.objects.filter(is_active=True).order_by('-created_at')[:10]

    return render(request, 'home.html', {'apps': apps})


def app_list(request):
    apps = App.objects.filter(is_active=True).order_by('-created_at')

    return render(request, 'app_list.html', {'apps': apps})


def app_detail(request, pk):
    app = App.objects.get(id=pk)
    reviews = Review.objects.filter(app=app)
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

    context = {
        'app': app,
        'reviews': reviews,
        'avg_rating': avg_rating
    }

    return render(request, 'app_detail.html', context)


@login_required
def app_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        logo = request.FILES.get('logo')
        apk_file = request.FILES.get('apk_file')
        version = request.POST.get('version')
        size = request.POST.get('size')
        is_free = bool(request.POST.get('is_free'))
        price = request.POST.get('price') or 0

        App.objects.create(
            developer=request.user,
            title=title,
            description=description,
            category=category,
            logo=logo,
            apk_file=apk_file,
            version=version,
            size=size,
            is_free=is_free,
            price=price
        )

        messages.success(request, 'App created successfully')
        return redirect('app_list')

    categories = Category.objects.filter(is_active=True)

    return render(request, 'app_form.html', {'categories': categories})


@login_required
def app_update(request, pk):
    app = App.objects.get(id=pk)
    if app.developer != request.user:
        return redirect('app_list')

    if request.method == 'POST':
        app.title = request.POST.get('title')
        app.description = request.POST.get('description')
        app.category_id = request.POST.get('category')
        if request.FILES.get('logo'):
            app.logo = request.FILES.get('logo')
        if request.FILES.get('apk_file'):
            app.apk_file = request.FILES.get('apk_file')
        app.version = request.POST.get('version')
        app.size = request.POST.get('size')
        app.is_free = bool(request.POST.get('is_free'))
        app.price = request.POST.get('price') or 0
        app.save()

        messages.success(request, 'App updated successfully')
        return redirect('app_detail', pk=app.id)

    categories = Category.objects.filter(is_active=True)

    return render(request, 'app_form.html', {'app': app, 'categories': categories})


@login_required
def app_delete(request, pk):
    app = App.objects.get(id=pk)

    if app.developer == request.user:
        app.delete()
        messages.success(request, 'App deleted successfully')
    else:
        messages.error(request, 'You are not the developer of this app')

    return redirect('app_list')


def category_apps(request, pk):
    apps = App.objects.filter(category_id=pk, is_active=True)

    return render(request, 'category_app_list.html', {'apps': apps})


@login_required
def review_create(request, pk):
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')

        app = App.objects.get(id=pk)

        Review.objects.create(user=request.user, app=app,
                              rating=rating, comment=comment)

        messages.success(request, 'Review created successfully')

    return redirect('app_detail', pk=pk)


def app_search(request):
    query = request.GET.get('q', '')

    apps = App.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query),
        is_active=True
    )

    return render(request, 'app_search.html', {'apps': apps, 'query': query})


@login_required
def user_profile(request, pk):
    user = CustomUser.objects.get(id=pk)
    user_apps = App.objects.filter(developer=user)

    return render(request, 'profile.html', {'user_profile': user, 'user_apps': user_apps})
