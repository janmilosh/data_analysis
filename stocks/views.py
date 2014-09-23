from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import requests, json
from datetime import datetime

from stocks.models import Stock

def stocks(request):
    stocks = Stock.objects.all()

    return render(request, 'stocks.html', ({
        'stocks': stocks,
    }))

def stock(request, stock_id=1):
    stock = get_object_or_404(Stock, id=stock_id)

    data = get_stock_data(stock.ticker)

    #Test weather data
    city = 'Columbus,%20Ohio'
    weather_data = get_weather_data(city)
    weather_data = json.loads(weather_data)

    hourly_temps = []

    weather_data = weather_data['hourly_forecast']
    
    start_date_base = weather_data[0]['FCTTIME']
    month = start_date_base['month_name']
    day = start_date_base['mday']
    year = start_date_base['year']
    start_date = '%s %s, %s' % (month, day, year)

    for data in weather_data:
        hourly_temps.append({
            'temp': data['temp']['english'],
            'time': data['FCTTIME']['epoch'],
        })

    return render(request, 'stock.html', ({
        'hourly_temps': hourly_temps,
        'start_date': start_date,
        'stock': stock,
        'stock_data': data,
    }))

def get_stock_data(stock):
    stock = 'GSPC'
    request_string = 'http://ichart.finance.yahoo.com/table.csv?s=^'+ stock + '%20&a=00&b=01&c=2010&g=d'
    data = requests.get(request_string)
    return data.content

def get_weather_data(city):
    api_key = 'e7abc77487d7e3eb'
    request_string = 'http://api.wunderground.com/api/' + api_key + '/hourly/q/' + city + '.json'
    data = requests.get(request_string)
    return data.content

