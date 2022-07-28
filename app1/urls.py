from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('homepage',views.homepage,name='homepage'),
    path('login',views.login,name='login'),
    path('loginuser',views.loginUser,name='loginuser'),
    path('signup',views.signup,name='signup'),
    path('inputfromsignup',views.inputfromsignup,name='inputfromsignup'),
    path('about',views.about,name='about'),
    path('buy',views.buy,name='buy'),
    path('buydemo',views.buydemo,name='buydemo'),
    path('addpost',views.addpost,name='addpost'),
    path('posts',views.posts,name='posts'),
    path('posted',views.posted,name='posted'),
    path('donate',views.donate,name='donate'),
    path('donated',views.donated,name='donated'),
    path('contact',views.contact,name='contact'),
    path('successuser',views.successuser,name='successuser'),
    path('addingitem',views.addingitem,name='addingitem'),
    path('addingitemfromdonatepage',views.addingitemfromdonatepage,name='addingitemfromdonatepage'),
    path('addingpost',views.addingpost,name='addingpost'),
    path('showfromposttable',views.showfromposttable,name='showfromposttable'),
    path('showfromitemtable',views.showfromitemtable,name='showfromitemtable'),
    path('showfromitemtabletohomepage',views.showfromitemtabletohomepage,name='showfromitemtabletohomepage'),
    path('myorders',views.myorders,name='myorders'),
]