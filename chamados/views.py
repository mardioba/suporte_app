from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Setor, Usuario, Chamado
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ChamadoForm, SetorForm, AtualizarChamadoForm, Chamado_Editar_Form
from django.contrib.auth import logout
from datetime import datetime
from django import forms
from datetime import datetime
################# Chamados ################
class ChamadoListView(ListView):
    model = Chamado
    template_name = 'chamado_list.html'

class ChamadoDetailView(DetailView):
    model = Chamado
    template_name = 'chamados/chamado_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chamado = self.get_object()  # Obtém o objeto Chamado
        context['chamado_keys'] = chamado.__dict__.keys()  # Obtém as chaves do objeto
        return context

def ChamadoCreateView(request):
    data = datetime.now().strftime('%Y-%m-%d')
    hora_atual = datetime.now().strftime("%H:%M")
    context = {}
    if request.method == "POST":
        form = ChamadoForm(request.POST)
        form.initial['hora_chamado'] = hora_atual
        form.initial['data'] = datetime.now().strftime('%Y-%m-%d')
        user = request.user
        context = {
            'form': form,
            'user': user,
        }
        if form.is_valid():
            form.save()
            return redirect("chamado-list")
    else:
        form = ChamadoForm()
        form.initial['hora_chamado'] = hora_atual
        form.initial['data'] = datetime.now().strftime('%Y-%m-%d')
        context['form'] = form
        context['data'] = data
    return render(request, "chamados/chamado_form.html", context)
def chamado_edit(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('chamado-list')
    else:
        form = ChamadoForm(instance=chamado)
    return render(request, 'chamados/formularioeditar.html', {'form': form})

class ChamadoDeleteView(DeleteView):
    model = Chamado
    template_name = 'chamados/chamado_confirm_delete.html'
    success_url = reverse_lazy('chamado-list')

def atualizar_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, pk=chamado_id)
    if request.method == 'POST':
        form = AtualizarChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('listar_chamados_nao_atendidos')
    else:
        form = AtualizarChamadoForm(instance=chamado)
        # Se for a primeira vez que o formulário é exibido, defina o valor inicial da hora
        if not request.POST:
            form.initial['hora_atendimento'] = datetime.now().strftime('%H:%M')
            form.initial['data_atendimento'] = datetime.now().strftime('%Y-%m-%d')
    return render(request, 'chamados/atualizar_chamado.html', {'form': form})
def listar_chamados_nao_atendidos(request):
    chamados_nao_atendidos = Chamado.objects.filter(atendido=False)
    existe_chamado_nao_atendido = chamados_nao_atendidos.exists()
    return render(request, 'chamados/listar_chamados_nao_atendidos.html', {'chamados_nao_atendidos': chamados_nao_atendidos, 'existe_chamado_nao_atendido': existe_chamado_nao_atendido})



class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuario/usuario_detail.html'
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
def logout_view(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request, 'outros/home.html')

########## SETOR ############'

class SetorListView(ListView):
    model = Setor
    template_name = 'setor/setor_list.html'

class SetorDetailView(DetailView):
    model = Setor
    template_name = 'setor/setor_detail.html'
def cadastrar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            nome_setor = form.cleaned_data['nome']
            # Verifica se o setor já existe no banco de dados
            if Setor.objects.filter(nome=nome_setor).exists():
                return redirect('setor_existente')
            else:
                form.save()
                return redirect('setor-list')
    else:
        form = SetorForm()
    return render(request, 'setor/cadastrar_setor.html', {'form': form})
def editar_setor(request, setor_id):
    setor = get_object_or_404(Setor, pk=setor_id)
    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            return redirect('setor_editado')
    else:
        form = SetorForm(instance=setor)
    return render(request, 'setor/editar_setor.html', {'form': form})

def excluir_setor(request, setor_id):
    setor = get_object_or_404(Setor, pk=setor_id)
    if request.method == 'POST':
        setor.delete()
        return redirect('setor_excluido')
    return render(request, 'excluir_setor.html', {'setor': setor})

def setor_existente(request):
    return render(request, 'setor/setor_existente.html')

def view_chamado(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == "POST":
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect("chamado-list")
    else:
        form = ChamadoForm(instance=chamado)
    return render(request, "chamados/chamado_form.html", {'form': form})
    chamado = Chamado.objects.get(pk=pk)
    data = chamado.data.strftime('%Y-%m-%d')#YYYY-MM-DD
    form = ChamadoForm(instance=chamado)
    context = {'chamado': chamado, 'data': data}
    context['form'] = form
    return render(request, 'chamados/chamado_edit.html', context)