import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from random import choice, randint
from faker import Faker
from chamados.models import Setor, Usuario, Chamado

fake = Faker()

def create_setores():
    nomes_setores = ["TI", "Recursos Humanos", "Financeiro", "Atendimento ao Cliente", "Logística"]
    for nome in nomes_setores:
        Setor.objects.create(nome=nome)

def create_usuarios(num_usuarios=10):
    setores = Setor.objects.all()
    for _ in range(num_usuarios):
        nome = fake.name()
        username = fake.user_name()
        email = fake.email()
        password = make_password("senha123")  # Senha padrão
        setor = choice(setores)
        Usuario.objects.create(username=username, email=email, password=password, setor=setor)

def create_chamados(num_chamados=10):
    usuarios = Usuario.objects.all()
    setores = Setor.objects.all()
    for _ in range(num_chamados):
        titulo = fake.sentence(nb_words=3)
        descricao = fake.text()
        usuario = choice(usuarios)
        setor = choice(setores)
        data = fake.date_time_this_year()
        # hora_chamado = fake.time()
        hora_chamado = data.time()  # Use a hora da data gerada
        Chamado.objects.create(
            titulo=titulo,
            descricao=descricao,
            usuario=usuario,
            setor=setor,
            data=data.date(),
            hora_chamado=hora_chamado,  # Use a hora da data gerada
            data_cadastro=timezone.now(),
            atendido=fake.boolean(),
            data_atendimento=fake.date_time_this_year().date(),
            hora_atendimento=fake.time()
        )

def populate_database():
    create_setores()
    create_usuarios()
    create_chamados()

if __name__ == "__main__":
    populate_database()
    print("Banco de dados populado com sucesso!")
