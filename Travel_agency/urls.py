"""Travel_agency URL Configuration

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
from django.conf.urls import url, include
from Travel import views as Travel_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf.urls.static import static
from Travel_agency import settings

urlpatterns = [
    url(r"^Travel/", include("Travel.urls")),
    url(r"^Travel/signup/$", Travel_views.signup, name="signup"),
    url(r"^Travel/login/$", auth_views.login, name="login"),
    url(r"^Travel/edit_profile/$", Travel_views.edit_profile, name="edit_profile"),
    url(r"^Travel/logout/$", auth_views.logout, name="logout"),
    url(r"^Travel/admin/", admin.site.urls),
    url(r"^$", RedirectView.as_view(url = "/Travel/")),
    url(r'^Travel/ckeditor/', include('ckeditor_uploader.urls')),
    url(r"^$", RedirectView.as_view(url = "/Travel/")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)