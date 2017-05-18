
import logging

from django.conf import settings 
from django.shortcuts import get_object_or_404, render, redirect
#from django.http import HttpResponse

# Get an instance of a logger
logger = logging.getLogger("django." + __name__)

# The map with active geotags
def index(request):
    #logger.info(dir(request.user))
    #if not request.user.is_authenticated():
    #    logger.info(request.user.__class__)
    #    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'yourmap/index.html')

# The application landing page (we will see what happens here)
def home(request):
    return render(request, 'yourmap/home.html')

# Create a new GeoTag
def add_geotag(request):
    return render(request, 'yourmap/add_geotag.html')

# Edit a GeoTag - can only be done by the creator of the tag
def edit_geotag(request):
    return render(request, 'yourmap/edit_geotag.html')

#    def results(request, question_id):
#        question = get_object_or_404(Question, pk=question_id)
#        return render(request, 'polls/results.html', {'question': question})

def profile(request):
    return render(request, 'yourmap/profile.html')
