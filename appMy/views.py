from django.shortcuts import render
from .models import *


def dashboardPage(request):
    gamecard = GameCard.objects.all()
    context = {
        'gamecard' : gamecard
    }
    return render(request,'dashboard.html',context)

def forumDetail(request):
    context = {}
    return render(request,'forumDetail.html',context)

def postDetail(request):
    context = {}
    return render(request,'postDetail.html',context)