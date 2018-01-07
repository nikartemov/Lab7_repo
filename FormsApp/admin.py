from django.contrib import admin

from FormsApp.models import Team, TeamAdmin

admin.site.register(Team, TeamAdmin)
