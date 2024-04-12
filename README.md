Para execultar o projeto e preciso que tenha o python 3.12.3 instalado em sua maquina e rode os seguites comando na orden no seu terminal 
(pode ser no termina interno do VScode, soprecisa estar na pasta do projeto exemplo
c:....\...\...\mercado_CRUD>)
** Configuração do Ambiente Virtual

1. Defina a Política de Execução (Windows):
Set-ExecutionPolicy -Scope Process -Execution Bypass

2 Crie um Ambiente Virtual (Windows):
python -m venv .venv

3 Ative o Ambiente Virtual (Windows):
.\.venv\Scripts\activate

** Instalação de Dependências

1 Instale o python-decouple (para extrair dados seguros do arquivo de configuração):
pip install python-decouple

2 Instale o dj-database-url (para manipulação de strings de conexão de banco de dados):
pip install dj-database-url

3 Instale o Django:
pip install django

4 Instale o Crispy-Bootstrap5 (para integração do Django com o Bootstrap 5):
pip install crispy-bootstrap5

** Gerenciamento do Banco de Dados

1 Crie as Migrações de Modelo:
python manage.py makemigrations

2 Execute as Migrações Iniciais:
python manage.py migrate

** Execução do Servidor

1 Inicie o Servidor Django:
python manage.py runserver







