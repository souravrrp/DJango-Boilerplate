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
    # path('logout/', views.logout_view, name= "logout"),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name= "home"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
