from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import PlayerNameForm
from .models import player, player_score
from random import randint
from django.views.decorators.cache import never_cache


class Index(View):
    def get(self, request):
        request.session['bg'] = '##f4f1de'
        request.session['bt'] = 'GUESS'
        return render(request, 'index.html')


class PlayerNameRecord(View):
    def post(self, request):
        player(player_name=request.POST.get('player_name')).save()
        return redirect('play_game')


def redirect_to_great_number(request):
    return redirect('/Great_Number')


class PlayGame(View):
    def get(self, request):
        if 'number' not in request.session:
            request.session['number'] = randint(1, 100)
        return render(request, 'game.html')


class ProcessNumber(View):
    def post(self, request):
        randomNumber = int(request.session.get('number'))
        userNumber = int(request.POST.get('user_number'))
        if userNumber > randomNumber:
            request.session['bg'] = '#ffadad'
            request.session['bt'] = 'GUESS LOW'
        elif userNumber < randomNumber:
            request.session['bg'] = '#fdffb6'
            request.session['bt'] = 'GUESS HIGH'
        else:
            request.session.pop('number')
            request.session['bg'] = '##f4f1de'
            request.session['bt'] = 'GUESS'
            return redirect('complete_game')

        return redirect('play_game')


def CompleteGame(request):
    return render(request, 'win_game.html')
