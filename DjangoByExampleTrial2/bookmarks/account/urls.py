from django.conf.urls import url
from . import views

urlpatterns = [
    #url('login/', views.user_login, name='login'),
    url('login/', 'django.contrib.auth.views.login',  name='login'),
    url('logout/', 'django.contrib.auth.views.logout',  name='logout'),
    url('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    url('', views.dashboard, name="dashboard"),
]
