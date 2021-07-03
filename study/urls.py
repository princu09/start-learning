from django.shortcuts import redirect
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    # Basic Page For Everyone
    url(r'^$', RedirectView.as_view(url='home')),
    path('home', views.index, name="Main Page"),

    # Start Learn
    path('start_learn/standard_<int:standard>' , views.start_learn , name="Start Learn"),
    # Get Lessions
    path('get_lessions/<str:standard>/<str:subject>' , views.get_lessions , name="Get Lessions"),
    # Lacture Details
    path('lacture_details/<int:id>' , views.lacture_details , name="Lacture Details"),
    # Add Lacture
    path('add_chapter/<str:sub>/<int:std>' , views.add_chapter , name="Add Chapter"),

    # Handle Comment
    path('comment/<int:id>' , views.comment , name="Save Comment"),

    # Login Page
    path('login', views.handleLogin, name="Login Page"),
    # Register Page
    path('register', views.handleRegister, name="Login Page"),
    # Logout Page
    path('logout', views.handleLogout, name="Logout Page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
