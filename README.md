Para execultar o projeto e preciso que tenha o python 3.12.3 instalado em sua maquina e rode os seguites comando na orden no seu terminal 
(pode ser no termina interno do VScode, soprecisa estar na pasta do projeto exemplo
c:....\...\...\mercado_CRUD>)

Configuração do Ambiente Virtual
 1. Defina a Política de Execução (Windows):
Set-ExecutionPolicy -Scope Process -Execution Bypass

 2. Crie um Ambiente Virtual (Windows):
python -m venv .venv

 3. Ative o Ambiente Virtual (Windows):
.\.venv\Scripts\activate

Instalação de Dependências
 1. Instale o python-decouple (para extrair dados seguros do arquivo de configuração):
pip install python-decouple

 2. Instale o dj-database-url (para manipulação de strings de conexão de banco de dados):
pip install dj-database-url

 3. Instale o Django:
pip install django

 4. Instale o Crispy-Bootstrap5 (para integração do Django com o Bootstrap 5):
pip install crispy-bootstrap5

Gerenciamento do Banco de Dados
 1. Crie as Migrações de Modelo:
python manage.py makemigrations nesse projeto já está criado(No changes detected)

 2. Execute as Migrações Iniciais:
python manage.py migrate

Execução do Servidor

 1. Inicie o Servidor Django:
python manage.py runserver


estrutura de pasta do projeto
 
 1. migrations: 
Criação e atualização do banco de dados.

 2. templates\mercado:
Onde ficam todos os aquivos django-HTML (frondend).

 3. mercado\views.py:
arquivo em Python onde roda todo o Backend

 4. mercado\models.py:
Arquivo responsável pela criação do banco de dados.

 5. mercado\apps.py:
Arquivo responsável por separar os módulos, exemplo: caso seja necessário, cria um módulo financeiro e preciso criar mais um app, isso possível pelo comando "Python manage.py startapp financeiro".






