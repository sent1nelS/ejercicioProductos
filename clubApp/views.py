from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'templatesProductos/index.html')

def clubes(request):
    data={
        "titulo":"Clubes NineNine",
    }
    return render(request, 'templatesClub/indexc.html',data)

def colocolo(request):
    data={
        "titulo":"Clubes NineNine",
    }
    return render(request, 'templatesClub/indexc.html',data)

def cobreloa(request):
    data={
        "titulo":"Clubes NineNine",
    }
    return render(request, 'templatesClub/indexc.html',data)

def ohiggins(request):
    data={
        "titulo":"Clubes NineNine",
    }
    return render(request, 'templatesClub/indexc.html',data)