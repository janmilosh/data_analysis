from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


def hello(request):
    name = 'Jan'
    html = "<html><body><h1>My name is %s, and this is my webpage!</h1></body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Jan"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = "Jan"
    return render_to_response('hello.html', {'name': name})

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Jan (in the class)'
        return context