from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('dashboard/', views.dashboard, name='dashboard'),

    #Challenges
    path('start/', views.gettingStarted, name='start'),
    path('cookieMonster/', views.cookieMonster, name='cookieMonster'),
    path('POSTman/', views.POSTman, name='POSTman'),
    path('morse/', views.morse, name='morse'),
    path('vigil/', views.Vigil, name='vigil'),
    path('baseball/', views.baseball, name='baseball'),
    path('robots/', views.robots, name='robots'),
    path('aperisolve/', views.aperisolve, name='aperisolve'),





]