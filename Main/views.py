from django.shortcuts import render

# Create your views here.

#main pages
def index(request):
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')    

def leaderboard(request):
    return render(request, 'main/leaderboard.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')


# Challenge pages
def cookieMonster(request):
    return render(request, 'main/cookie.html')