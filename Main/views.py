from django.shortcuts import render, redirect
from Main.models import Challenges
from accounts.models import Player
import random
from django.db.models import Count

from django.contrib.auth import get_user
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
import json
import random
import uuid

# Create your views here.

#main pages
def index(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')    

def leaderboard(request):
    print("RUNNING")
    if not request.user.is_authenticated:
        return redirect('login')
    all_players = Player.objects.all().order_by('-score')

    context = {'player':Player.objects.get(username=request.user), 'players': all_players}
    return render(request, 'main/leaderboard.html', context)

def page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)

def dashboard(request):
    user = request.user
    context = {'user': user,'player':Player.objects.get(username=user), 'total_players':Player.objects.count(), 'challenges': Challenges.objects.all().order_by('points')[:]}
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/dashboard.html', context)


# Challenge pages

def gettingStarted(request):
    context = {"challenge": Challenges.objects.get(title="Getting Started")}
    return render(request, 'main/challenges/gettingstarted.html', context)


def cookieMonster(request):
    # return render(request, 'main/challenges/cookie.html', context)
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        flag = Challenges.objects.get(title="Cookie Monster").flag
        if not request.COOKIES.get('CookieJar'):
            who = user.username
        else:
            who = request.COOKIES.get("CookieJar")
        context = {"challenge": Challenges.objects.get(title="Cookie Monster"), "code": flag, "who": who}
        to_rend = render(request, "main/challenges/cookie.html", context)
        to_rend.set_cookie("CookieJar", who)

        return to_rend

    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))['code']

        return JsonResponse({"success": data == Challenges.objects.get(title="Cookie Monster").flag})

def POSTman(request):
    context = {"challenge": Challenges.objects.get(title="POSTman")}
    return render(request, 'main/challenges/POSTman.html', context)

def morse(request):
    context = {"challenge": Challenges.objects.get(title="Dot-Dash-Dot")}
    return render(request, 'main/challenges/morse.html', context)

def Vigil(request):
    context = {"challenge": Challenges.objects.get(title="Vigenere on Rail")}
    return render(request, 'main/challenges/vigil.html', context)

def baseball(request):
    context = {"challenge": Challenges.objects.get(title="BASEball Player")}
    return render(request, 'main/challenges/baseball.html', context)

def robots(request):
    context = {"challenge": Challenges.objects.get(title="Baymax Rocks!")}
    return render(request, 'main/challenges/robots.html', context)

def robotstxt(request):
    context = {"challenge": Challenges.objects.get(title="Baymax Rocks!")}
    return render(request, 'main/challenges/robotstxt.html', context)

def aperisolve(request):
    context = {"challenge": Challenges.objects.get(title="Aperisolve!")}
    return render(request, 'main/challenges/aperisolve.html', context)

def killam(request):
    show_flag = True if request.headers['User-Agent'].lower() == "killam" else False
    flag = Challenges.objects.get(title="Killam").flag
    context = {"challenge": Challenges.objects.get(title="Killam"), "show_flag": show_flag, "flag": flag}
    return render(request, 'main/challenges/killam.html', context)

def blankspace(request):
    context = {"challenge": Challenges.objects.get(title="Blank Space by Taylor Swift")}
    return render(request, 'main/challenges/blankspace.html', context)

