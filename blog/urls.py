from django.conf.urls import url

from blog import views

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^main/',views.main,name='main'),
    url(r'^add_blog/',views.add_blog,name='add_blog'),
    url(r'^comment/',views.comment,name='comment'),
]