"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "api"

urlpatterns = [
    path('',views.index,name='index'),
    path('signup', views.signup_request, name='signup'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name= 'logout'),
    path('profile', views.profile, name='profile'),
    path('service', views.service, name='service'),
    path('project', views.project, name='project'),
    path('feature', views.feature, name='feature'),
    path('support', views.support, name='support'),
    path('team', views.team, name='support'),
    path('terms', views.terms, name='terms'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
