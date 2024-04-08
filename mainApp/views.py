from django.shortcuts import render
from django.views import View

from django.conf import settings
from django.conf.urls.static import static

from mainApp.models import *
from statsApp.models import Transfer


class Home(View):
    def get(self, reuests):
        return render(reuests, 'index.html')

class About(View):
    def get(self, requests):
        return render(requests, 'about.html')

class Tryouts(View):
    def get(self, requests):
        return render(requests, 'tryouts.html')

class Clubs(View):
    def get(self, requests):
        context = {
            'clublar': Club.objects.order_by('-kapital'),
        }
        return render(requests, 'clubs.html', context)

class Players(View):
    def get(self, requests):
        context = {
            'players': Player.objects.order_by('-ism'),
        }
        return render(requests, 'players.html', context)

class Player_20(View):
    def get(self, requests):
        context = {
            'player_20': Player.objects.filter(yosh__lte=20).order_by('-narx'),
        }
        return render(requests, 'U-20 players.html', context)

class Transfers_record(View):
    def get(self, requests):
        context = {
            'transfers': Transfer.objects.order_by('narx'),
        }
        return render(requests, 'latest-transfers.html', context)