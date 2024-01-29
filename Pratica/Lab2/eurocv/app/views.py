import json
from django.shortcuts import render

def eurocv(request):

    with open("./eurocv.json") as f:
        data = json.load(f)

    tparams = {
        "data": data
    }

    return render(request, 'eurocv.html', tparams)
