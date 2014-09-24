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
    city = 'Columbus'
    state = 'Ohio'
    location = city + ',%20' + state
    weather_data = get_weather_data(location)
    weather_data = json.loads(weather_data)

    weather_data = weather_data['hourly_forecast']
    
    start_date_base = weather_data[0]['FCTTIME']
    start_month = start_date_base['month_name_abbrev']
    start_day = start_date_base['mday']
    start_year = start_date_base['year']
    start_date = '%s %s, %s' % (start_month, start_day, start_year)
    
    last_index = len(weather_data) - 1
    end_date_base = weather_data[last_index]['FCTTIME']
    end_month = end_date_base['month_name_abbrev']
    end_day = end_date_base['mday']
    end_year = end_date_base['year']
    end_date = '%s %s, %s' % (end_month, end_day, end_year)

    hourly_temps = []

    for data in weather_data:
        time = data['FCTTIME']
        hour = time['hour_padded']
        day = time['mday_padded']
        month = time['mon_padded']
        year = time['year']
        hourly_temps.append({
            'temp': data['temp']['english'],
            'time': '%s %s %s %s' % (hour, day, month, year),
        })

    return render(request, 'stock.html', ({
        'city': city,
        'state': state,
        'hourly_temps': hourly_temps,
        'start_date': start_date,
        'end_date': end_date,
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

