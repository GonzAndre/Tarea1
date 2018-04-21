from django.contrib import admin

# Register your models here.
from Basketball.models import *

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','thumb')
    search_fields = ('name',)
    def thumb(self,obj):
        return mark_safe("<img src='%s' width='40' height='40'>"% obj.logo.url)
    thumb.allow_tags = True
    thumb.__name__ = 'logo'

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','thumb')
    search_fields = ('name','nickname','rut')
    list_filter = ('team',)
    list_filter = ('birthdate',)
    def thumb(self,obj):
        return mark_safe("<img src='%s' width='40' height='40'>"% obj.photo.url)
    thumb.allow_tags = True
    thumb.__name__ = 'photo'
    #filter_horizontal = ('birthdate',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name','age')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name','code')
