from django.db.models import F, FloatField, ExpressionWrapper, Sum
from django.db.models.functions import Abs
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *


class IndexView(View):
    def get(self, req):
        return render(req, 'index.html')


class ClubsView(View):
    def get(self, req):
        clubs = Club.objects.all()
        context = {
            'clubs': clubs
        }
        return render(req, 'clubs.html', context)


class ClubDetailsView(View):
    def get(self, req, club_id):
        club = get_object_or_404(Club, pk=club_id)
        context = {
            'club': club,
        }
        return render(req, 'club-details.html', context)


class LatestTransfersView(View):
    def get(self, req):
        transfers = Transfer.objects.filter(season=Season.objects.last())
        context = {
            'transfers': transfers
        }
        return render(req, 'latest-transfers.html', context)


class PlayerView(View):
    def get(self, req):
        players = Player.objects.all()
        context = {
            'players': players
        }
        return render(req, 'players.html', context)


class PlayerU20View(View):
    def get(self, req):
        players = Player.objects.filter(age__lte=20)
        context = {
            'players': players
        }
        return render(req, 'U-20 players.html', context)


class TryoutsView(View):
    def get(self, req):
        return render(req, 'tryouts.html')


class AboutView(View):
    def get(self, req):
        return render(req, 'about.html')


class TransferRecordsView(View):
    def get(self, req):
        transfers = Transfer.objects.order_by('-price')
        context = {
            'transfers': transfers
        }
        return render(req, 'stats/transfer-records.html', context)


class StatsView(View):
    def get(self, req):
        return render(req, 'stats.html')


class Top15PredictionsView(View):
    def get(self, request):
        transfers = Transfer.objects.annotate(
            accuracy=ExpressionWrapper(
                100 - (Abs(F('price') - F('price_tft')) / F('price') * 100),
                output_field=FloatField()
            )
        ).order_by('-accuracy')[:150]
        context = {
            'transfers': transfers
        }
        return render(request, 'stats/150-accurate-predictions.html', context)


class Top50ExpenditureView(View):
    def get(self, request):
        latest_season = Season.objects.last()
        clubs = Club.objects.annotate(
            total_income=Sum(
                'club_to__price',
                filter=models.Q(club_to__season=latest_season)
            )
        ).order_by('-total_income')[:50]
        context = {
            'clubs': clubs,
            'season': latest_season,
        }

        return render(request, 'stats/top-50-clubs-by-expenditure.html', context)



class Top50IncomesView(View):
    def get(self, request):
        latest_season = Season.objects.last()
        clubs = Club.objects.annotate(
            total_income=Sum(
                'club_from__price',
                filter=models.Q(club_from__season=latest_season)
            )
        ).order_by('-total_income')[:50]
        context = {
            'clubs': clubs,
            'season': latest_season,
        }

        return render(request, 'stats/top-50-clubs-by-income.html', context)
