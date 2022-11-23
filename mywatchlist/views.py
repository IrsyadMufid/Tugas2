from email import message
from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers
import datetime


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = MyWatchlist.objects.all()
    not_watched = 0
    watched = 0
    message = ""
    for film in item_mywatchlist:
        if (film.watched):
            watched += 1
        else:
            not_watched += 1
    print(watched)
    if(not_watched >= watched):
        message =  "Wah, kamu masih sedikit menonton!"
    else:
        message = "Selamat, kamu sudah banyak menonton!"
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Irsyad Mufid',
        'message': message

    }
    return render(request, 'mywatchlist.html', context)


def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MyWatchlist.objects.all()
    not_watched = 0
    watched = 0
    message = ""
    for film in data:
        if (film.watched):
            watched += 1
        else:
            not_watched += 1
    print(watched)
    if(not_watched >= watched):
        message =  "Wah, kamu masih sedikit menonton!"
    else:
        message = "Selamat, kamu sudah banyak menonton!"
    context = {
        'item_mywatchlist': data,
        'nama' : 'Irsyad Mufid',
        'message': message
        
    
    }
    return render(request, 'mywatchlist.html', context)
