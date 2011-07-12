from django.shortcuts import *

def index(request, university_id):
	frats = Frat.objects.all().order_by('-name')
	return render_to_response('frats/index.html', {'frats':frats})