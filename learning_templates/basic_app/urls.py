from django.conf.urls import url
from basic_app import views

#Template Taging
app_name = 'basic_app'

urlpatterns =[
    url(r'^$',views.index, name='index'),
    url('^relative/$',views.relative, name='relative'),
    url('^other/$',views.other, name='other'),
]
