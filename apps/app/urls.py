from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('apps/', views.app_list, name='app_list'),
    path('apps/<int:pk>/', views.app_detail, name='app_detail'),

    path('category/<int:pk>/apps/', views.category_apps, name='category_apps'),

    path('apps/<int:pk>/review/', views.review_create, name='review_create'),

    path('search/', views.app_search, name='app_search'),

    path('user/<int:pk>/profile/', views.user_profile, name='user_profile'),
]
