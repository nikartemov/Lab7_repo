from django.contrib import admin
from django.db import models


class Team(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    coach = models.CharField(max_length=30, default='')
    games = models.IntegerField(default=0)
    win = models.IntegerField(default=0)


class CountryFilter(admin.SimpleListFilter):
    title = 'Country'
    parameter_name = 'description'

    def lookups(self, request, model_admin):
        return [
            ('Russian', 'Российские клубы')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'Russian':
            return queryset.filter(description='Профессиональый футбольный клуб')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'games', 'win', 'percent_win')
    search_fields = ['name']
    list_filter = (CountryFilter,)

    def percent_win(self, obj):
        return '{0:.1%}'.format(obj.win/obj.games)

