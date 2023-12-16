"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import reviews.views
import reviews.api_views
from django.urls import include, path
from bookr.views import profile
# from reviews.admin import reviews_admin_site
# from .admin import main_admin_site
# from reviews import api_views

urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'),
                              namespace='accounts')),
    path("admin/", admin.site.urls),
    path('api/first_api_view', reviews.api_views.first_api_view),
    path('api/all_books', reviews.api_views.AllBooks.as_view()),
    path('api/login', reviews.api_views.Login.as_view(), name='login'),
    # path('api/login', api_views.Login.as_view(), name='login')
    # path("reviews/admin/", reviews_admin_site.urls),
    path('accounts/profile/', profile, name='profile'),
    path('', reviews.views.welcome_view, name='home'),
    path('books/', reviews.views.book_list, name='book_list')
]
