from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def hello(request):
    name = 'Jan'
    html = "<html><body><h1>My name is %s, and this is my webpage!</h1></body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Jan"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)