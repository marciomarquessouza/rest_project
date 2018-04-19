# djangorest/urls.py

from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'ˆadmin/', admin.site.urls),
    url(r'ˆ', include('api.urls'))

]
