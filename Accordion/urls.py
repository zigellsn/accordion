"""Accordion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
                  path("", TemplateView.as_view(template_name="base.html"), name="base"),
                  path('admin/', admin.site.urls),
                  path("view1/", TemplateView.as_view(template_name="default.html",
                                                      extra_context={"description": "1 GET on load",
                                                                     "count": range(1, 2)}), name="view1"),
                  path("view2/", TemplateView.as_view(template_name="default.html",
                                                      extra_context={"description": "2 GET on load",
                                                                     "count": range(1, 4)}), name="view2"),
                  path("view3/", TemplateView.as_view(template_name="default.html",
                                                      extra_context={"description": "3 Always GET on click",
                                                                     "count": range(1, 3)}),
                       name="view3"),
                  path("view4/", TemplateView.as_view(template_name="default.html",
                                                      extra_context={"description": "4 GET once on click",
                                                                     "count": range(1, 5)}),
                       name="view4"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
