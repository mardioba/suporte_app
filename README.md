# 🎧 Sistema de Suporte - Abertura de Chamados ⚠️

Bem-vindo ao Sistema de Suporte para abertura de chamados! Este sistema foi desenvolvido para facilitar o processo de solicitação de suporte técnico, permitindo que os usuários registrem e acompanhem suas solicitações de maneira eficiente.

* ## Recursos Principais:

Abertura de Chamados: Os usuários podem facilmente abrir novos chamados descrevendo seus problemas ou solicitações de suporte.

Acompanhamento em Tempo Real: Uma vez que um chamado é aberto, os usuários podem acompanhar seu progresso em tempo real, desde a criação até a resolução.

Priorização Automática: O sistema prioriza automaticamente os chamados com base na gravidade e urgência do problema relatado.

Comentários e Atualizações: Os usuários e os agentes de suporte podem adicionar comentários e atualizações aos chamados, mantendo todos os envolvidos informados sobre o status e as ações tomadas.

Notificações por E-mail: Os usuários recebem notificações por e-mail sempre que houver uma atualização em seu chamado, garantindo uma comunicação eficaz e transparente.
* ## Instalação
* ### Clonar o sistema
~~~Codigo GIT
  git clone https://github.com/mardioba/suporte_app.git
~~~
* ### Entrando na pasta do sistema
  ~~~
  cd suporte_app
  ~~~
* ### Criar Ambiente Virtual
~~~Python
python -m venv venv
~~~
* ### Ativar Ambiente Virtual
  * #### Linux
 ~~~ Còdigo Python
source venv/bin/activate
~~~
   * #### Windows
     * PowerShell ou Prompt de Comando

~~~Python
venv\bin\Activate.ps1
~~~
~~~CMD
venv\bin\Activate.bat
~~~

* ### Instalação dos requisitos
    ~~~Python
    pip install -r requirements.txt
    ~~~
* ### Criando o usuario inicial
  ~~~
  python manage.py createsuperuser
  ~~~
* ### Iniciar o sistema
  ~~~Python Django
  python manage.py runserver
  ~~~
  
* ## Como Usar:
1. Acesso o sistema pelo seu navegador http://127.0.0.1:8000/
2. Criar um Chamado: Clique no botão "Chamado >> Cadastrar" e preencha o formulário com as informações necessárias, incluindo uma descrição detalhada do problema.

Acompanhar Chamados: Após abrir um chamado, você pode acompanhar seu progresso em chamado >> Listar, onde serão exibidos todos os chamados abertos.

Adicionar Comentários: Para fornecer mais informações ou esclarecimentos sobre o seu chamado, você pode adicionar comentários diretamente na página do chamado.

* ## Contribuindo:

Este projeto está em constante evolução e estamos abertos a contribuições! Se você tiver ideias para melhorias ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença:

Este projeto é licenciado sob a Licença MIT.
