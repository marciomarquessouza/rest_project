# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
    url('auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('bucketlist/$', views.CreateView.as_view(), name='create'),
    url('bucketlist/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url('users/', views.UserView.as_view(), name="users"),
    url('users/(?P<pk>[0-9]+)$', views.UserDetailsView.as_view(), name="user_details"),
    url('get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
