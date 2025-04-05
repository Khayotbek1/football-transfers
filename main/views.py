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
        transfers = Transfer.objects.all()
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
    def get(self,req):
        players = Player.objects.filter(age__lte=20)
        context = {
            'players': players
        }
        return render(req, 'U-20 players.html',context)


class TryoutsView(View):
    def get(self,req):
        return render(req, 'tryouts.html')

class AboutView(View):
    def get(self,req):
        return render(req, 'about.html')