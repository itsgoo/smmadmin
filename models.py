from django.db import models

from django.contrib.auth.models import User
from django import forms






class Accounts(models.Model):
    soc_net_options = (
        ('instagram', 'Instagram'),
        ('vkontakte', 'Vkontakte'),
        ('telegram', 'Ttelegram'),
    )
    name_for_accounts = models.CharField(max_length=30, verbose_name='name_for_accounts')
    acc_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='acc_owner')
    soc_net = models.CharField(max_length=20, choices=soc_net_options, verbose_name='soc_net')


    # account_posts = models.ManyToManyField(Posts, help_text="Select a genre for this book")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('acc_detail', args=[str(self.id)])

    def __str__(self):
        return self.name_for_accounts



class Friends(models.Model):
    owners_friends = models.IntegerField(verbose_name='owners_friend',)
    acc_owners_friends = models.IntegerField(verbose_name='acc_owners_friends',)




class Posts(models.Model):
    soc_net_fot_post_options = (
        ('instagram', 'Instagram'),
        ('vkontakte', 'Vkontakte'),
        ('telegram', 'Ttelegram'),
    )
    account_for_post = models.ForeignKey(Accounts, blank=True, on_delete=models.CASCADE)
    soc_net_fot_post = models.CharField(max_length=20, choices=soc_net_fot_post_options)
    name_for_post = models.CharField(max_length=30)
    text_fot_post = models.TextField(max_length=20, blank=True)
    date_time_for_post = models.DateTimeField(auto_now_add=False)
    file_fot_post = models.FileField(upload_to='file', blank=True)
    id_post_creator = models.IntegerField(verbose_name='id_post_creator_name',)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('posts_detail', args=[str(self.id)])

    def __str__(self):
        return self.name_for_post


class Example(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField()
    positive_small_field = models.PositiveSmallIntegerField()
    Big_integer_field = models.BigIntegerField()
    float_field = models.FloatField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=5)
    text_field = models.TextField(max_length=20)
    date_field = models.DateField(auto_now=True)
    date_time_field = models.DateTimeField(auto_now_add=True)
    decimal_field = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.EmailField()
    file_field = models.FileField(upload_to='file')
    image_field = models.ImageField(upload_to='images')


class Users(models.Model):
    tarif_options = (
        ('tarif_free', 'Tarif_free'),
        ('tarif_min', 'Tarif_min'),
        ('tarif_mid', 'tarif_mid'),
        ('tarif_max', 'Tarif_max'),
    )
    name_users = models.CharField(max_length=20)
    tarif_users = models.CharField(max_length=20, choices=tarif_options)

    def __str__(self):
        return self.name_users


class User_acc(models.Model):
    user_acc_name = models.CharField(max_length=200, verbose_name='Users name')
    user_acc_pass = models.CharField(max_length=200, verbose_name='User_acc_pass')


class Account(models.Model):
    acc_name = models.CharField(max_length=200, verbose_name='Autors name')
    acc_count_subscribers = models.CharField(max_length=200, verbose_name='acc_count_subscribers')


class Human(models.Model):
    CHOISE_COMPANY = (
        ('google', 'Google'),
        ('yandex', 'yandex'),
        ('yahoo', 'yahoo'),
        ('dell', 'dell'),
    )

    POSITION_CHOISE = (
        ('senior', 'Senior'),
        ('middle', 'Middle'),
        ('junior', 'Junior'),
    )

    PYTHON = 'python'
    JS = 'javascript'
    PHP = 'php'

    LANGUAGE_CHOISE = (
        (PYTHON, 'Python'),
        (JS, 'Javascript'),
        (PHP, 'PHP'),
    )

    name = models.CharField(max_length=150, verbose_name='name')
    surname = models.CharField(max_length=150, verbose_name='surname')
    birth = models.DateField(auto_now=False, auto_now_add=False)
    company = models.CharField(max_length=150, choices=CHOISE_COMPANY)
    position = models.CharField(max_length=150, choices=POSITION_CHOISE)
    language = models.CharField(max_length=150, choices=LANGUAGE_CHOISE, default=PYTHON)
    salary = models.IntegerField()

    def __str__(self):
        return 'name - {0} , surname - {1}, company - {2}'.format(self.name, self.surname, self.company)


class Peoples(models.Model):
    FIO = models.CharField(max_length=128)
    birthday = models.DateField()

# Create your models here.
