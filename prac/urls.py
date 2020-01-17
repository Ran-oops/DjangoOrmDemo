from django.conf.urls import include, url
from django.contrib import admin
from . import views

# urlpatterns = [

#     url(r'^subtostu$',views.subtostu, name="subtostu"),
#     url(r'^stutoteacher$',views.stutoteacher, name="stutoteacher")

# ]

urlpatterns = [
    url(r'addbook$',views.addbook, name='addbook'),
    url(r'deletebook$',views.deletebook, name='deletebook'),
    url(r'updatebook$',views.updatebook, name='updatebook'),
    url(r'showbook$',views.showbook, name='showbook')
]


