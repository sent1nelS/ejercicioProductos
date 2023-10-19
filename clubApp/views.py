from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'templatesProductos/index.html')

def clubes(request):
    data={
        "titulo":"Clubes",
        
    }
    return render(request, 'templatesClub/indexc.html',data)