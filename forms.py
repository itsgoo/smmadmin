from django.forms import ModelForm, Form
from . import models

from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_acc, Posts, Accounts, Friends
from .models import Account
from django.contrib.admin import widgets


class FriendsCreate(ModelForm):
    class Meta:
        model = Friends
        fields = ['owners_friends', 'acc_owners_friends']

    def Save(self):
        new_friend = Friends.objects.create(
            owners_friends=self.cleaned_data['owners_friends'],
            acc_owners_friends=self.cleaned_data['acc_owners_friends'],
        )
        return new_friend




class Posts_Create_form(ModelForm):
    class Meta:
        model = Posts
        fields = ['account_for_post', 'soc_net_fot_post', 'name_for_post', 'text_fot_post', 'date_time_for_post',
                  'file_fot_post']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date_time_for_post'].widget = widgets.AdminSplitDateTime()
    # need js for usable widget

        widgets = {
            'id_post_creator': forms.HiddenInput(),
        }

    def Save(self):
        new_post = Posts.objects.create(
            account_for_post=self.cleaned_data['account_for_post'],
            soc_net_fot_post=self.cleaned_data['soc_net_fot_post'],
            name_for_post=self.cleaned_data['name_for_post'],
            text_fot_post=self.cleaned_data['text_fot_post'],
            date_time_for_post=self.cleaned_data['date_time_for_post'],
            file_fot_post=self.cleaned_data['file_fot_post']
        )
        return new_post


class User_acc_form(ModelForm):
    class Meta:
        model = User_acc
        fields = ['user_acc_name', 'user_acc_pass']

    def Save(self):
        new_user_acc = User_acc.objects.create(
            user_acc_name=self.cleaned_data['user_acc_name'],
            user_acc_padd=self.cleaned_data['user_acc_pass']
        )
        return new_user_acc


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
