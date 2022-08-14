from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    date = datetime.today()
    #return render(request, "DocBlog/index.html", context={'prenom':'Pierre','date':date})
    return HttpResponse("coucou")