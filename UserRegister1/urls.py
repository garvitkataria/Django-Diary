from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.regester, name='regester'),
	url(r'login', views.login, name='login'),
]