# -*- coding: utf-8 -*-
# 간단 게시판 예제
from django.conf.urls import patterns, include, url
from sample_board import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_board.views.home', name='home'),
    # url(r'^dj_board/', include('dj_board.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', views.home),
    url(r'^show_write_form/$', views.show_write_form),   
    url(r'^DoWriteBoard/$', views.DoWriteBoard),
    url(r'^viewWork/$', views.viewWork),
    url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
    
    
        
    
)
