from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import path, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import (router, ColorLightAPI)

class MyFormView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        if request.GET.get('logout', None):
            logout(request)
            return HttpResponseRedirect(reverse('Server:home_page'))
        return super().get(request, *args, **kwargs)
@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
    return JsonResponse({'key': uploaded_file_url})


@api_view(('POST',))
def ColorLightAPIFun(request):
    print(request.data)
    try:
        cl_obj = ColorLightAPI.ColorLightAPI()
        response = cl_obj.singleLineMessage(request.data)
        return Response(response)
    except Exception as e:
        print("exception in ColorLightAPI", str(e))
    return Response("ColorLightAPI Trigered")


app_name = "Server"

urlpatterns = [
    path('', MyFormView.as_view(), name='home_page'),  # redirection after
    path('upload', upload ),  # redirection after
    path('api/ColorLightAPI', ColorLightAPIFun ),  # redirection after
]

urlpatterns += router.router.urls
