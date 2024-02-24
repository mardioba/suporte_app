from django.urls import path
from . import views
from chamados.views import add_chamado, home

urlpatterns = [
    path('chamados/', views.ChamadoListView.as_view(), name='chamado_list'),
    # path('chamados/criar/', cadastrar_chamado, name='chamado_create'),
    path('home', home, name='pagina_sucesso_cadastro_chamado'),
    path('cadastrar_chamado/', add_chamado, name='cadastrar_chamado'),

]
