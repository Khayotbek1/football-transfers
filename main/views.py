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
    def get (self,req):
        transfers = Transfer.objects.all()
        context = {
            'transfers': transfers
        }

        return render (req, 'latest-transfers.html', context)