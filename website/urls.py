from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from qa import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    path('result', views.sbert, name='result'),

    path('qa/', include('qa.url')),  # urls for qa

    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
