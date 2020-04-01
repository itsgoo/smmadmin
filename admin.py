from django.contrib import admin
from . import models
from .models import Human
from .models import Peoples

admin.site.register(models.Example)
admin.site.register(models.Users)


class Accountsadmin(admin.ModelAdmin):
    list_display = ['name_for_accounts', 'acc_owner']
    class Meta:
        model = models.Accounts


admin.site.register(models.Accounts, Accountsadmin)


class Postsadmin(admin.ModelAdmin):
    list_display = ['name_for_post', 'account_for_post']
    class Meta:
        model = models.Accounts


admin.site.register(models.Posts, Postsadmin)
admin.site.register(Human)
admin.site.register(Peoples)
