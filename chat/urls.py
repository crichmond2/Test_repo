from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'new/$', views.new_room,name='new_chat_room'),
  url(r'(?P<label>.+)/$',views.chat_room,name='chat_room'),
]
