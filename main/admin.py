from django.contrib import admin
from .models import *

# Inline for Players in Club admin
class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1
    show_change_link = True

# Inline for Transfers in Player admin
class TransferInline(admin.TabularInline):
    model = Transfer
    extra = 1
    show_change_link = True

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'president', 'coach', 'found_date', 'country']
    search_fields = ['name', 'president', 'coach']
    list_filter = ['country']
    autocomplete_fields = ['country']
    inlines = [PlayerInline]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'position', 'number', 'price', 'club', 'country']
    search_fields = ['name', 'position']
    list_filter = ['position', 'club', 'country']
    autocomplete_fields = ['country', 'club']
    inlines = [TransferInline]


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['id', 'player', 'club_from', 'club_to', 'price', 'price_tft', 'date', 'season']
    search_fields = ['player__name', 'club_from__name', 'club_to__name']
    list_filter = ['season', 'date', 'club_from', 'club_to']
    autocomplete_fields = ['player', 'club_from', 'club_to', 'season']
