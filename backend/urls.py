"""backend URL Configuration

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
from base64 import b64encode

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse, include
from django.views import View
from rest_framework.authentication import BasicAuthentication
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class LoginCheck(View):
    template_name = 'LoginView.html'

    def get(self, request, *args, **kwargs):
        try:
            return render(request, 'LoginView.html')
        except Exception as e: print('Exception In Login', str(e))
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        error = None
        try:
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                 us_pass = request.POST.get('username')+':'+request.POST.get('password')
                 login(request, user)
                 return HttpResponseRedirect(reverse('Server:home_page'))
            else:
                error = 'Username or Password Incorrect'
        # No backend authenticated the credential
        except Exception as e:
            error = str(e)

        return render(request, self.template_name, context={'error': error})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('Auth/logincheck', LoginCheck.as_view(), name='login_check'),
    # only admin user can able to see the docs
    url(r'^docs/api', include_docs_urls(title='VMSS API Docs',
                                           authentication_classes=[BasicAuthentication],
                                           permission_classes=[IsAuthenticated, IsAdminUser])
        ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
