from django.conf.urls import url
from .import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^add_school/$',views.add_school,name='add school'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout_,name='logout'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
]
