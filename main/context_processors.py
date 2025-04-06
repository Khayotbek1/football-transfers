from .models import *
from django.db.models import Count

def get_clubs_by_country(request):
    countries = Country.objects.annotate(club_count=Count('club')).filter(club_count__gt=0).order_by('-club_count')
    l  = countries.count()

    if l % 2 == 0:
        countries_left = countries[:l // 2]
        countries_right= countries[l // 2:]
    else:
        countries_left = countries[:l // 2 + 1]
        countries_right = countries[l // 2 + 1:]
    context = {
        'countries_left': countries_left,
        'countries_right': countries_right
    }
    return context
