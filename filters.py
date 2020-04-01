from .models import Accounts
from django import forms
from django.forms import ModelForm, CharField, Textarea
from django.db import models


class AccsFilterForm(ModelForm):


    # def __init__(self, *args, **kwargs):
    #     # first call parent's constructor
    #     super(AccsFilterForm, self).__init__(*args, **kwargs)
    #     # there's a `fields` property now
    #     self.fields['name_for_accounts'].required = False


    soc_net_options = (
        ('instagram', 'Instagram'),
        ('vkontakte', 'Vkontakte'),
        ('telegram', 'Ttelegram'),
    )
    name_for_accounts = forms.CharField(required=False)
    soc_net = forms.IntegerField(widget=forms.RadioSelect(choices=soc_net_options), required=False, )

    class Meta:
        model = Accounts
        fields = [
            'name_for_accounts',
            'soc_net'
        ]
        # widgets = {
        #     'name_for_accounts': Textarea(required=False),
        # }
        # name_for_accounts = forms.CharField(label='accounts name', required=False)
