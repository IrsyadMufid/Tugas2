from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = MyWatchlist.objects.all()
    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Irsyad Mufid',
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
    context = {
        'item_mywatchlist': data,
        'nama' : 'Irsyad Mufid',
    }
    return render(request, 'mywatchlist.html', context)
