from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from badapatra import views
from django.urls import path, include
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('building', views.BuildingViewset)

urlpatterns = routers.urls # + [url(r'^count/$', views.Counter.as_view())]
