from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'addbook$',views.addbook, name='addbook'),
    url(r'deletebook$',views.deletebook, name='deletebook'),
    url(r'updatebook$',views.updatebook, name='updatebook'),
    url(r'showbook$',views.showbook, name='showbook'),

    url(r'^addAuthDetail',views.addAuthDetail, name='addAuthDetail'),
    url(r'^deleteAuthDetail',views.deleteAuthDetail, name='deleteAuthDetail'),
    url(r'^updateAuthDetail',views.updateAuthDetail, name='updateAuthDetail'),
    url(r'^showAuthDetail',views.showAuthDetail, name='showAuthDetail')
]


