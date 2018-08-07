from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
# Create your views here.
def add(request) :
	a = request.GET.get('a', 0)
	b = request.GET.get('b', 0)
	c = int(a) + int(b)
	t = loader.get_template(("home.html"))
	return HttpResponse(t.render({'str':str(c)}))

def add2(request, a, b) :
	c = int(a) + int(b)
	#t = loader.get_template("home.html")
	return render(request, 'home.html', {'str': str(c)})
	#return HttpResponse(t.reader({"str":str(c)}))

def index(request) :
	return render(request, "home.html")

def add3(request, a, b) :
	return HttpResponseRedirect(
		reverse('add2', args=(a,b))
	)