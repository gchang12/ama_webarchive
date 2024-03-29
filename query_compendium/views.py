from django.shortcuts import render
from django.http import HttpResponse

from .models import ContentCreator, RedditQuery

# Create your views here.

def content_creator_index(request):
    context = {
        "cc_list": ContentCreator.objects.all(),
    }
    return render(request, "query_compendium/content_creator_index.html", context)

def qa_listing(request, cc_name):
    context = {
        "query_list": RedditQuery.objects.filter(content_creator__url_name=cc_name),
    }
    return render(request, "query_compendium/qa_listing.html", context)

