from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.LoginPage, name = "LoginPage"),
	url(r'^home/$', views.index, name = "Home"),
]