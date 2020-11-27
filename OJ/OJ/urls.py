"""OJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , include('index.urls')),
    path('' , include('signup.urls')),
    path('' , include('signin.urls')),
    path('user/' , include('user.urls')),
    path('ratings/' , include('ratings.urls')),
    path('follow/', include('follow.urls')),
    path('usertalk/', include('message.urls')),
    path('problem/', include('problem.urls')),
    path('contest/', include('contest.urls')),
    path('submission/', include('submission.urls')),
    path('problemset/', include('problemset.urls')),
    path('admin/', include('admin.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )