
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'yourmap/index.html')

def home(request):
    return render(request, 'yourmap/home.html')

#    def results(request, question_id):
#        question = get_object_or_404(Question, pk=question_id)
#        return render(request, 'polls/results.html', {'question': question})

