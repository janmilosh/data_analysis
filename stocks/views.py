from django.shortcuts import render
from django.shortcuts import get_object_or_404
from stocks.models import Stock

def stocks(request):
    stocks = Stock.objects.all()

    return render(request, 'stocks.html', ({
        'stocks': stocks
    }))

def stock(request, stock_id=1):
    stock = get_object_or_404(stock, id=stock_id)

    return render(request, 'stock.html', ({
        'stock': stock
    }))