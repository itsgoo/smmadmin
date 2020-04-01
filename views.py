from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader

from .models import Human
from .models import Accounts, Posts, Friends
from .models import Peoples
from django.contrib.auth import get_user

from . import forms
from .forms import UserCreateForm
from .forms import Posts_Create_form, FriendsCreate
from .filters import AccsFilterForm
# from .forms import AccsFilterForm

from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets

from django.shortcuts import redirect

import calendar
import time


# Create your views here.


def accaccountstyle(request):
    return render(request, 'style/style.css')


class acc_account_add(View):
    def get(self, request):

        accounts_list = Accounts.objects.all()
        first_acc = Accounts.objects.all()[0]
        accounts_list_inst = Accounts.objects.filter(soc_net='instagram', acc_owner_id=request.user.id)
        accounts_list_vk = Accounts.objects.filter(soc_net='vkontakte', acc_owner_id=request.user.id)
        accounts_list_ok = Accounts.objects.filter(soc_net='telegram', acc_owner_id=request.user.id)
        form = Posts_Create_form()

        return render(request, 'add_account.html', context={
            'accounts_list_inst': accounts_list_inst,
            'accounts_list_vk': accounts_list_vk,
            'accounts_list_ok': accounts_list_ok,
            'first_acc': first_acc,
            'accounts_list': accounts_list,
            'form': form,
        })

    # inside condition to output accounts.acc_owner_id == user.id

    def post(self, request):
        form_post = Posts_Create_form(request.POST)
        form = Posts_Create_form()
        if form_post.is_valid():
            new_user = form_post.save()
            ctx = 'Post was create!'
            accounts_list = Accounts.objects.all()
            return render(request, 'smmstartapp/accounts_detail.html',
                          context={'ctx': ctx, 'accounts_list': accounts_list})
        else:
            return render(request, 'correct_form.html/', context={'form': form})


def base_generic(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    accounts_list = Accounts.objects.all()
    accounts_list_count = Accounts.objects.all().count()
    name_acc_count = Accounts.objects.filter(soc_net='instagram').count()
    posts_list = Posts.objects.all()
    first_acc = Accounts.objects.all()[0]

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(request, 'index.html', context={'first_acc': first_acc,
                                                  'posts_list': posts_list,
                                                  'name_acc_count': name_acc_count,
                                                  'accounts_list': accounts_list,
                                                  'accounts_list_count': accounts_list_count})


class AccountsListView(ListView):
    model = Accounts

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the posts
        context['posts_list'] = Posts.objects.all()
        context['first_acc'] = Accounts.objects.all()[0]
        return context


class AccountDetailView(generic.DetailView):
    model = Accounts

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all elements

        from datetime import date, datetime, time
        import calendar

        # get the date and time now
        now = datetime.now()

        # fill in variable with hours in day
        var_time_fix8 = time(hour=8, minute=00)
        var_time_fix9 = time(hour=9, minute=00)
        var_time_fix10 = time(hour=10, minute=00)
        var_time_fix11 = time(hour=11, minute=00)
        var_time_fix12 = time(hour=12, minute=00)
        var_time_fix13 = time(hour=13, minute=00)
        var_time_fix14 = time(hour=14, minute=00)
        var_time_fix15 = time(hour=15, minute=00)
        var_time_fix16 = time(hour=16, minute=00)
        var_time_fix17 = time(hour=17, minute=00)
        var_time_fix18 = time(hour=18, minute=00)
        var_time_fix19 = time(hour=19, minute=00)
        var_time_fix20 = time(hour=20, minute=00)
        var_time_fix21 = time(hour=21, minute=00)
        var_time_fix22 = time(hour=22, minute=00)

        time_line = [var_time_fix8,
                     var_time_fix9,
                     var_time_fix10,
                     var_time_fix11,
                     var_time_fix12,
                     var_time_fix13,
                     var_time_fix14,
                     var_time_fix15,
                     var_time_fix16,
                     var_time_fix17,
                     var_time_fix18,
                     var_time_fix19,
                     var_time_fix20,
                     var_time_fix21,
                     var_time_fix22,
                     ]

        # fill in list with the names of the days of the week
        calend_month = calendar.day_name
        weeks = 0
        calend_month_all_all = []
        while weeks < 7:
            for lists in calend_month:
                calend_month_all_all.append(lists)
            weeks += 1
        common_list_names = calend_month_all_all

        # get the this month
        this_month = date.today()  # get the this month
        var_mounth = date.today().month  # get the this month
        var_year = date.today().year  # get the this year

        # clear this month data
        calend_month_calc = calendar.monthcalendar(var_year, var_mounth)
        clear_this_month_data = []
        for lists in calend_month_calc:
            for i in lists:
                clear_this_month_data.append(i)
        common_list = dict(zip(clear_this_month_data, common_list_names))  # combine two lists for this month
        common_list = common_list.items()

        # get the next month
        t = date.today()
        try:
            n = t.replace(t.year, t.month + 1, 1)
        except ValueError:
            n = t.replace(t.year + 1, 1, 1)
        next_month = n.month

        # clear next month data
        calend_month_calc_next = calendar.monthcalendar(var_year, next_month)
        clear_next_month_data = []
        for lists in calend_month_calc_next:
            for i in lists:
                clear_next_month_data.append(i)
        common_list_next = dict(zip(clear_next_month_data, common_list_names))  # combine two lists for this month

        form = Posts_Create_form()



        # Catch all accounts id
        friends_id = Friends.objects.all()
        qs = Accounts.objects.all()
        list_acc_id = []
        for acc in qs:
            list_acc_id.append(acc.id)

        # Catch all friends accounts id
        list_friends_acc_id = []
        for friend in friends_id:
            list_friends_acc_id.append(friend.acc_owners_friends)

        # Take all accounts id that have no friends
        for i in list_friends_acc_id:
            list_acc_id.remove(i)

        context['list_acc_id'] = list_acc_id
        context['friends_id'] = friends_id

        context['accounts_list'] = Accounts.objects.all()
        context['posts_detail_in_acc'] = list(Posts.objects.order_by('-date_time_for_post'))
        context['first_acc'] = Accounts.objects.all()[0]
        context['form'] = form
        context['now'] = now
        context['common_list'] = common_list  # list with all dates this month and all names of days of week
        context['common_list_next'] = common_list_next  # list with all dates of next month and all days names
        context['time_line'] = time_line  # list with time of day
        context['this_month'] = this_month
        return context
        # inside condition to output accounts.acc_owner_id == user.id

    def post(self, request, pk):
        form_post = Posts_Create_form(request.POST)
        form = Posts_Create_form()
        if form_post.is_valid():
            new_user = form_post.save(commit=False)
            new_user.id_post_creator = request.user.id
            new_user.save()
            ctx = 'Post was create!'
            accounts_list = Accounts.objects.all()
            return render(request, 'smmstartapp/accounts_detail.html',
                          context={'ctx': ctx,
                                   'accounts_list': accounts_list,
                                   'new_user': new_user,
                                   })
        else:
            return render(request, 'correct_form.html/', context={'form': form, 'form_post': form_post})


class AccSearchListView(ListView):
    model = Accounts
    template_name = 'acc_account_search.html'

    def get_context_data(self, **kwargs, ):
        # Call the base implementation first to get a context
        context = super(AccSearchListView, self).get_context_data(**kwargs)

        filter_form = AccsFilterForm(self.request.GET)

        # Catch all accounts id
        friends_id = Friends.objects.all()
        qs = Accounts.objects.all()
        list_acc_id = []
        for acc in qs:
            list_acc_id.append(acc.id)

        # Catch all friends accounts id
        list_friends_acc_id = []
        for friend in friends_id:
            list_friends_acc_id.append(friend.acc_owners_friends)

        # Take all accounts id that have no friends
        for i in list_friends_acc_id:
            list_acc_id.remove(i)

        # Filters
        if 'name_for_accounts' in self.request.GET:
            name_for_accounts_query = self.request.GET['name_for_accounts']
            if name_for_accounts_query != '' and name_for_accounts_query is not None:
                qs = qs.filter(name_for_accounts__icontains=name_for_accounts_query)
        if 'soc_net' in self.request.GET:
            soc_net_query = self.request.GET['soc_net']
            if soc_net_query != '' and soc_net_query is not None:
                qs = qs.filter(soc_net__icontains=soc_net_query)

        form = Posts_Create_form()

        context['form'] = form
        context['accounts_list_filter'] = qs

        context['list_acc_id'] = list_acc_id

        context['friends_id'] = friends_id
        context['filter_form'] = filter_form
        
        return context

    def post(self, request):
        form_post = Posts_Create_form(request.POST)
        form = Posts_Create_form()

        form_friend_filled = FriendsCreate(request.POST)
        form_friend = FriendsCreate()

        # New post save
        if form_post.is_valid():
            new_user = form_post.save()
            ctx = 'Post was create!'
            accounts_list = Accounts.objects.all()
            return render(request, 'smmstartapp/accounts_detail.html',
                          context={'ctx': ctx, 'accounts_list': accounts_list})

        # New friends save
        elif form_friend_filled.is_valid():
            new_friend = form_friend_filled.save()
            ctx = 'Friend was create!'
            return render(request, 'acc_account_search.html', context={
                'new_friend': new_friend,
                'ctx': ctx,
            })

        else:
            return render(request, 'correct_form.html/', context={'form': form,
                                                              'form_friend': form_friend
                                                              })



class FriendsDelete(DeleteView):
    model = Friends
    success_url = reverse_lazy('search_accs')


class testfriends(View):
    def get(self, request):
        form_friend = FriendsCreate()
        accs = Accounts.objects.all()
        return render(request, 'testfriends.html', context={
            'form_friend': form_friend,
            'accs': accs,
        })

    def post(self, request):
        form_friend_filled = FriendsCreate(request.POST)
        form_friend = FriendsCreate()

        if form_friend_filled.is_valid():
            new_friend = form_friend_filled.save()
            ctx = 'Post was create!'
            return render(request, 'testfriends.html', context={
                'new_friend': new_friend,
                'ctx': ctx,
            })
        else:
            return render(request, 'correct_form_field.html', context={'form_friend': form_friend})


class PostsView(View):
    def get(self, request, pk):
        posts_detail = Posts.objects.get(pk=pk)
        posts_all = Posts.objects.all()
        return render(request, 'smmstartapp/posts_detail.html', context={'posts_detail': posts_detail,
                                                                         'posts_all': posts_all})


class accountsCreate_instagram(CreateView):
    model = Accounts
    fields = '__all__'
    initial = {'soc_net': 'instagram', }


class accountsCreate_telegram(CreateView):
    model = Accounts
    fields = '__all__'
    initial = {'soc_net': 'telegram', }


class accountsCreate_vkontakte(CreateView):
    model = Accounts
    fields = '__all__'
    initial = {'soc_net': 'vkontakte', }



class accountsUpdate(UpdateView):
    model = Accounts
    fields = ['name_for_accounts', 'date_time_for_post']


class accountsDelete(DeleteView):
    model = Accounts
    success_url = reverse_lazy('accs_add')



class postUpdate(UpdateView):
    model = Posts
    fields = ['text_fot_post', 'name_for_post', 'date_time_for_post', 'file_fot_post']


class postDelete(DeleteView):
    model = Posts
    success_url = reverse_lazy('accs_add')
