"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('content/', include('content.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',include('author.urls')),
    path('author/login/',auth_views.LoginView.as_view(template_name='author/login.html'),name='login'),
    path('author/logout/',auth_views.LogoutView.as_view(template_name='author/logout.html'),name='logout'),
    path('content/',include('content.urls')),
    path('author/password-reset/',auth_views.PasswordResetView.as_view(template_name='author/password_reset.html'),name='password_reset'),
    path('author/password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='author/password_reset_done.html'),name='password_reset_done'),
    path('author/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='author/password_reset_confirm.html'),name='password_reset_confirm'),
    path('author/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete'),name='password_reset_complete'),
    path('author/password-change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='author/password_change_done.html'),name='password_change_done'),
    path('author/password-change/',auth_views.PasswordChangeView.as_view(template_name='author/password_change.html'),name='password_change'),

]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
