"""P3 URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index"),
    path('',views.home,name="home"),
    path('second/',views.second,name="second"),
    path('third/',views.third,name="third"),
    path('fourth/',views.fourth,name="fourth"),
    path('fifth/',views.fifth,name="fifth"),
    path("url_data/<name>",views.urls_data,name="urls_data"),
    path("ab/<a>/<b>",views.ab,name="ab"),
    path("ac/<ac>",views.ac,name="ac"),
    path("grt/<grt>",views.grt, name ="grt"),
    path("vowel/<str>", views.vowel, name = "vowel"),
]
