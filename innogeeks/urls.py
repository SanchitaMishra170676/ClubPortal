"""innogeeks URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# handler404 = 'dashboard.views.not_found404'
# # handler500 = 'dashboard.views.custom_error_view'
# # handler403 = 'dashboard.views.custom_permission_denied_view'
# # handler400 = 'dashboard.views.custom_bad_request_view'

admin.site.site_header ='Innogeeks Admin'
admin.site.site_title ='Admin Panel'
admin.site.index_header ='Innogeeks Admin Panel'
urlpatterns = [
    path('innogeeks/private/admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/',include('accounts.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('member/',include('member.urls')),
]  +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
