from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import word_search.searchUtils as searchUtils

def index(request):
    return render(request, 'word_search/index.html', {})
    
def search(request):
    searchTypeMap = {
        'basic': searchUtils.basicSearch, 
        'start': searchUtils.startSearch, 
        'end': searchUtils.endSearch, 
        'contain': searchUtils.containSearch, 
        'make': searchUtils.usingLettersSearch
    }
    if request.POST['search_type'] in searchTypeMap:
        searchFunction = searchTypeMap[request.POST['search_type']]
        words = searchFunction(request.POST['search_text'])
    else:
        # Return some kind of error message here? Bad Http response?
        # For now just don't do a search
        words = []
    return render(request, 'word_search/results.html', {
        'words': words,
        'input': request.POST['search_text']
    })
    

