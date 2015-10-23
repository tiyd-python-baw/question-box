"""question_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from box.views import UserPage, AllQuestionsView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^question/(?P<question_pk>\d*)?$', 'box.views.question_detail', name = 'question_detail'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
       {'template_name': 'question_box/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register', 'box.views.register_user', name='register_user'),
    url(r'^new', 'box.views.new_question', name='newquestion'),
    url(r'^home/(?P<pk>[\w.]+)', UserPage.as_view(), name='home_page'),
    url(r'^$', AllQuestionsView.as_view(), name='questions'),
]
