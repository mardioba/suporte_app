from django.urls import path
from chamados.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path('chamados/', ChamadoListView.as_view(), name='chamado-list'),
    path('chamados/<int:pk>/', ChamadoDetailView.as_view(), name='chamado-detail'),
    path('chamados/new/', ChamadoCreateView, name='chamado-create'),
    path('chamados/<int:pk>/update/', ChamadoUpdateView.as_view(), name='chamado-update'),
    path('chamados/<int:pk>/delete/', ChamadoDeleteView.as_view(), name='chamado-delete'),
    path('setores/', SetorListView.as_view(), name='setor-list'),
    path('setores/<int:pk>/', SetorDetailView.as_view(), name='setor-detail'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('setor/new/', cadastrar_setor, name='cadastrar_setor'),
    path('setor/existente/', setor_existente, name='setor_existente'),
    path('setor/editar/<int:setor_id>/', editar_setor, name='editar_setor'),
    path('setor/excluir/<int:setor_id>/', excluir_setor, name='excluir_setor'),
    path('chamado/atualizar/<int:chamado_id>/', atualizar_chamado, name='atualizar_chamado'),
    path('chamados-nao-atendidos/', listar_chamados_nao_atendidos, name='listar_chamados_nao_atendidos'),
]
