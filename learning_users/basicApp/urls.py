from basicApp import views
from django.conf.urls import url

#Template Tagging
app_name = 'basicApp'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]

