from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import requests
from datetime import datetime
from pandas import DatetimeIndex

from stocks.models import Stock

def stocks(request):
    stocks = Stock.objects.all()

    return render(request, 'stocks.html', ({
        'stocks': stocks,
    }))

def stock(request, stock_id=1):
    stock = get_object_or_404(Stock, id=stock_id)
    print stock.ticker

    data = get_stock_data(stock.ticker)

    return render(request, 'stock.html', ({
        'stock': stock,
        'stock_data': data,
    }))

def get_stock_data(stock):
    stock = 'GSPC'
    request_string = 'http://ichart.finance.yahoo.com/table.csv?s=^'+ stock + '%20&a=00&b=01&c=2010&g=d'
    print request_string
    data = requests.get(request_string)
    return data.content
