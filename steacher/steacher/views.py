from django.http import Http404, HttpResponse

import datetime

def hello(request):
	return HttpResponse("Hello World!")

def about(request):
	return HttpResponse("about us:")

def writers(request):
	html = "<html><body>Parisa Daj<br />Donya Sharafoddin</body></html>"
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body> It is now %s.<br /></body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+ datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
	return HttpResponse(html)