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
def cookieMonster(request):
    context = {"challenge": Challenges.objects.get(title="Cookie")}
    return render(request, 'main/challenges/cookie.html', context)