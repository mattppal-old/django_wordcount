from django.http import HttpResponse
from django.shortcuts import render
from collections import defaultdict
import operator

def home(request):
  return render(request, 'home.html',)

def count(request):
  fulltext = request.GET['fulltext']
  wordlist = fulltext.split()
  count_dict = defaultdict(int)
  for word in wordlist:
    count_dict[word] += 1
  sorted_words = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)

  return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'count_dict':sorted_words})

def about(request):
  return render(request, 'about.html')
