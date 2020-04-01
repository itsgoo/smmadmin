from django.urls import re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

from . import forms

urlpatterns = [
    re_path(r'^$', views.base_generic, name='index'),
    url(r'^accs/$', views.AccountsListView.as_view(), name='accs_list'),
    url(r'^accs/(?P<pk>\d+)$', views.AccountDetailView.as_view(), name='acc_detail'),
    url(r'^post/(?P<pk>\d+)$', views.PostsView.as_view(), name='posts_detail'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.postDelete.as_view(), name='posts_delete'),
    url(r'^post/(?P<pk>\d+)/update/$', views.postUpdate.as_view(), name='posts_delete'),


    url(r'^testfriends/$', views.testfriends.as_view(), name='testfriends'),



    re_path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^acc_add/$', views.acc_account_add.as_view(), name='accs_add'),
    url(r'^acc_add/instagram/$', views.accountsCreate_instagram.as_view(), name='accounts_create_instagram'),
    url(r'^acc_add/telegram/$', views.accountsCreate_telegram.as_view(), name='accounts_create_telegram'),
    url(r'^acc_add/vkontakte/$', views.accountsCreate_vkontakte.as_view(), name='accounts_create_vkontakte'),
    url(r'^accs/(?P<pk>\d+)/update/$', views.accountsUpdate.as_view(), name='accounts_update'),
    url(r'^accs/(?P<pk>\d+)/delete/$', views.accountsDelete.as_view(), name='accounts_delete'),





    # url(r'^post_add/$', views.postCreate.as_view(), name='post_create'),

    re_path(r'^acc_search/$', views.AccSearchListView.as_view(), name='search_accs'),

    url(r'^friend/(?P<pk>\d+)/delete/$', views.FriendsDelete.as_view(), name='friends_delete'),


    # re_path(r'^acc_search/(?P<pk>\d+)/$', views.AccSearchListView.as_view(), name='search_accs'),

    re_path(r'^acc/account/style/style.css$', views.accaccountstyle),




]






