from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required
# def dashboard(request):
#     # campus = Campus.objects.filter(homepage=True)
#     categorias = [
#         {"titulo": "Todos", "url": "#todos", "current": True},
#         {"titulo": "Meus cursos", "url": "#Meus_cursos", "current": False},
#         {"titulo": "Destaques", "url": "#Destaques", "current": False},
#         {"titulo": "Gestão", "url": "#Gestão", "current": False},
#         {"titulo": "Administração", "url": "#Administração", "current": False},
#         {"titulo": "Qualidade de vida", "url": "#qualidade", "current": False}
#     ]
#     # return render(request, 'processoseletivo/index.html', context={'categorias': categorias})
#     return render(request, "processoseletivo/dashboard.html", context={'page_title': 'Dashboard v1'})

# @login_required
# def contacts(request: HttpRequest) -> HttpResponse:
#     return render(request, "processoseletivo/contacts.html")

# def term_of_use(request: HttpRequest) -> HttpResponse:
#     return render(request, "processoseletivo/term_of_use.html")
