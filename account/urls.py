from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/', views.login , name='login'),
    url(r'register/', views.register, name='register'),
    url(r'extend/', views.extend_profile, name='extend'),
    url(r'logout/', views.logout_user , name='logout'),

]
