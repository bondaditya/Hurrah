"""simulation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from case.views import ProductCreateView, ForcastCreateView, IntroductionView, ReportView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quarter$', ProductCreateView,name='product'),
    url(r'^quarter2$', ProductCreateView,name='product2'),
    url(r'^quarter3$', ProductCreateView,name='product3'),
    url(r'^quarter4$', ProductCreateView,name='product4'),
    url(r'^forcast$', ForcastCreateView,name='forcast'),
    url(r'^intro$', IntroductionView,name='intro'),
    url(r'^report$', ReportView,name='reports'),
    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
