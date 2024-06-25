from django.shortcuts import render
from dotenv import load_dotenv
# from .models import SetOfNews, News, Commodities, Forex, Indicator, Stock
import os
import requests
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def calculator(request):
    return render(request, 'calculator.html')

def news(request):
    return render(request, 'news.html')

def prices(request):
    return render(request, 'prices.html')

def weather(request):
    return render(request, 'weather.html')

def maps(request):
    return render(request, 'maps.html')