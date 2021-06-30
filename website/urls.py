from django.contrib import admin
from django.urls import path, include

from qa import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    path('result', views.sbert, name='result'),

    path('qa/', include('qa.url')),  # urls for qa

]
