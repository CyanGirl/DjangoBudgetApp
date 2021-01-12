from django.conf.urls import include, url
from .views import home,register,GetSpend,ViewSpends
from django.urls import path

urlpatterns=[
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r"",home,name="home"),
    path(r"register/",register,name="register"),
    path(r"add_spent/",GetSpend,name="spend"),
    path(r"view_spent/",ViewSpends,name="viewspends"),
]
