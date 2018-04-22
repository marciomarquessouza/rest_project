# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = {
    url('bucketlists/', views.CreateView.as_view(), name='create'),
}


urlpatterns = format_suffix_patterns(urlpatterns)
