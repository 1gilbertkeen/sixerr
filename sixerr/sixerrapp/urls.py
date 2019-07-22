from django.urls import path, re_path
from sixerrapp import views

app_name='sixerrapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^projects/(?P<id>[1-9]+)/$', views.project_detail, name='project_detail'),
]
