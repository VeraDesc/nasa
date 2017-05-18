
import logging

from django.conf import settings 
from django.shortcuts import get_object_or_404, render, redirect

# Get an instance of a logger
logger = logging.getLogger("django." + __name__)

# The map with active geotags
def index(request):
    #logger.info(dir(request.user))
    #if not request.user.is_authenticated():
    #    logger.info(request.user.__class__)
    #    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'relax/index.html')

