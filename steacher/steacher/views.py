from django.http import Http404, HttpResponse
from django.template.loader import get_template

import datetime

def hello(request):
	return HttpResponse("Hello World!")

def about(request):
	text = "About Us:"
	t = get_template('includes/nav.html')
	html = t.render({'current_section': text})
	return HttpResponse(html)

def writers(request):
	text = "Parisa Daj"
	t = get_template('about.html')
	html = t.render({'title': text})
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render({'current_date': now})
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+ datetime.timedelta(hours=offset)
	t = get_template('hours_ahead.html')
	html = t.render({'next_time': dt, 'hour_offset': offset})
	return HttpResponse(html)