from django.shortcuts import render
from . import api

def index(request):
    ip = api.get_ip()
    info = api.get_info(ip)
    print(info)
    
    return render(request, "index.html", info)
    