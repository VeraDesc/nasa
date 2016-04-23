
import logging

from django.conf import settings 
from django.shortcuts import get_object_or_404, render, redirect
#from django.http import HttpResponse

# Get an instance of a logger
logger = logging.getLogger("django." + __name__)

# Create your views here.
def index(request):
    #logger.info(dir(request.user))
    if not request.user.is_authenticated():
        logger.info(request.user.__class__)
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'yourmap/index.html')

def home(request):
    return render(request, 'yourmap/home.html')

#    def results(request, question_id):
#        question = get_object_or_404(Question, pk=question_id)
#        return render(request, 'polls/results.html', {'question': question})

