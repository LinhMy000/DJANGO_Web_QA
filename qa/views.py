from django.shortcuts import render

from . import SBERT, PreProcess

def home_view(request):
    return render(request, 'home.html')

def sbert(request):
    query = request.POST['search']
    clean_test = PreProcess.clean(query)
    result = SBERT.bert(clean_test)

    context = {
        'query': query,
        'list': result
    }

    return render(request, 'result.html', context=context)


