from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('signs.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^sign/', include('signs.urls')),
]
