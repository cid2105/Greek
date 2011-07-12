from django.shortcuts import *
from unis.models import *
from django.conf import settings

def index(request):
	return render_to_response('home/index.html', {}, context_instance=RequestContext(request))
	
	
def default_context(request):
	return {'MEDIA_ROOT': settings.MEDIA_URL}