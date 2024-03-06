from django.urls import  re_path as url, include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^resources$', views.resources, name= 'resources'),
    url(r'^about$', views.about, name= 'about'),
    url(r'^activities$', views.activities, name= 'activities'),
    url(r'^donate$', views.donate, name= 'donate'),
    url(r'^events$', views.events, name= 'events'),
     url(r'^vacancies$', views.events, name= 'vacancies'),
  
  
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)