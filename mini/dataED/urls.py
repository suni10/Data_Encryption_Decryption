from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('encrypt',views.encrypt,name='encrypt'),
    path('resencrypt',views.resencrypt,name='resencrypt'),
    path('resdecrypt',views.resdecrypt,name='resdecrypt'),
    path('home1',views.home1,name='home1'),
    path('dec',views.dec,name='dec'),
    path('home2',views.home2,name='home2'),
    path('enc',views.enc,name='enc')
]