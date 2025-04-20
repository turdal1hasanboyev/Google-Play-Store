from django.db import models

from django.db.models import Q

from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import App
from apps.review.models import Review
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
