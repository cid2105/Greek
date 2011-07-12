from django.shortcuts import *
from unis.models import *
from django.conf import settings

def index(request):
<<<<<<< HEAD
	return render_to_response('home/index.html', {}, context_instance=RequestContext(request))
=======
	return render_to_response('home/index.html', {'MEDIA_ROOT': settings.MEDIA_ROOT}, context_instance=RequestContext(request))
>>>>>>> c199b9df9b29327c52c1b92a2efa3c575b4e0c5a
	
	
def default_context(request):
	return {'MEDIA_ROOT': settings.MEDIA_URL}