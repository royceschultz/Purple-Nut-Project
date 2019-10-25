"""PurpleNut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views
from events import views as event_views
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',event_views.home, name='home'), # List events
    url(r'^event/(\d+)/', event_views.event_detail, name='event detail'),
    url(r'^event/create/', event_views.create_event, name='create event'),
    url(r'^register/',user_views.register,name='register'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='users/login.html') ,name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='users/logout.html') ,name='logout'),

    
    url(r'^event_edit/(\d+)', event_views.edit_event, name='event edit'),


    url(r'^profile/(\d+)/',user_views.profile,name='profile'),
    url('^profile/edit/', user_views.edit_profile, name = 'edit profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
