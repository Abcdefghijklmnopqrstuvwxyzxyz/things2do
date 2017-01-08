from django.conf.urls import url, include
from . import views

account_urls = [
	url(r'^new/$', views.reg),
	url(r'^$', views.user_index),
	url(r'^edit/$', views.edit_plan),
	url(r'^add/$', views.add_plan),
	url(r'^settings/$', views.user_setting),
	url(r'^save$', views.submit_plan),
]

api_urls = []

urlpatterns = [
	url(r'^$', views.index),
	url(r'^about/$', views.about),
	url(r'^account/', include(account_urls)),
	url(r'^login/$', views.login),
	url(r'^logout$', views.logout),
	url(r'^apis/', include(api_urls)),
]