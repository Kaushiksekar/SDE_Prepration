from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    freq_dict = {}

    for item in word_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1

    freq_dict = dict(sorted(freq_dict.items(), key=lambda x:x[1], reverse=True))

    return render(request, 'count.html', {"fulltext": fulltext, 'count':len(word_list), "frequency": freq_dict})
