from django.urls import path
from .apps import ProcessoSeletivoConfig
# from .views import dashboard, contacts, term_of_use


app_name = ProcessoSeletivoConfig.name


urlpatterns = [
    # path('contacts/', contacts, name="contacts"),
    # path('term_of_use/', term_of_use, name="term_of_use"),
    # path('', dashboard, name="dashboard"),
]
