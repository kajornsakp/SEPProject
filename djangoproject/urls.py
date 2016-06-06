"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from djangoapp import views
import djangoapp
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^q',views.query),
    url(r'^history',views.history),
    url(r'^register',views.register),
    url(r'^login',views.login),
    url(r'^reminder',views.reminder),
    url(r'^deletereminder', views.deletereminder),
    url(r'^updatereminder', views.updatereminder),
    url(r'^note',views.note),
    url(r'^deletenote',views.deletenote),
    url(r'^updatenote',views.updatenote),
    url(r'^calendar', views.calendar),
    url(r'^updatecalendar',views.updatecalendar),
    url(r'^deletecalendar',views.deletecalendar),
    url(r'^hw', views.hardware),
    url(r'^updatehw',views.updatehw),
    url(r'^deletehw',views.deletehw),
]
