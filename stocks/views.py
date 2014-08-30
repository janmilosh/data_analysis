from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
import requests
from pandas.io.data import DataReader
from pandas import DataFrame, Series
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

    data = get_stock_data()

    return render(request, 'stock.html', ({
        'stock': stock,
        'stock_data': data,
    }))

def get_stock_data():
    data = DataReader('aapl', 'yahoo', start = '01-01-2014')

    high_json = data['High'].to_json(date_format='iso')
    
    return high_json


# data comes from yahoo api
# convert data into format for graphs (json object)
# return json to template for graphs
# need to hook up vega and D3