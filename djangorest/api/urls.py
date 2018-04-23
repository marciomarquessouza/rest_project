# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = {
    url(r'ˆauth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bucketlist/$', views.CreateView.as_view(), name='create'),
    url(r'^bucketlist/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
