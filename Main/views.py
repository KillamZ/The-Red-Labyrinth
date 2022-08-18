from django.shortcuts import render, redirect
from Main.models import Challenges

# Create your views here.

#main pages
def index(request):
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')    

def leaderboard(request):
    return render(request, 'main/leaderboard.html')

def dashboard(request):
    user = request.user
    context = {'user': user, 'challenges': Challenges.objects.all().order_by('points')}
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/dashboard.html', context)


# Challenge pages

def gettingStarted(request):
    context = {"challenge": Challenges.objects.get(title="Getting Started")}
    return render(request, 'main/challenges/gettingstarted.html', context)


def cookieMonster(request):
    context = {"challenge": Challenges.objects.get(title="Cookie Monster")}
    return render(request, 'main/challenges/cookie.html', context)

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

def aperisolve(request):
    context = {"challenge": Challenges.objects.get(title="Aperisolve!")}
    return render(request, 'main/challenges/aperisolve.html', context)
