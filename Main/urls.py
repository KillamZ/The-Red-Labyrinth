from django.urls import path
from . import views 
from accounts import views as accountViews

urlpatterns = [
    path('', views.index, name='index'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cookieMonster/', views.cookieMonster, name='cookieMonster'),

]