## Django-Crud - Projeto Lista de Tarefas

# Deploy at: https://jorgeenrique.pythonanywhere.com/

No que consite este projeto:
- Criar uma lista de tarefas com o dia que foi listada
- Poder editar, atualizar, finalizar e até deletar a tarefa
- Login ainda a ser implementado, layout pronto

## Configurando o ambiente para executar a aplicação web.
Faça o download deste repositorio:

```
$ git clone https://github.com/jorgevendramini/Django-Crud.git
```

Crie um maquina virtual e instale as bibliotecas disponiveis no 
arquivo requirements.txt:

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd projeto_clinica
$ python3 -m venv venv
```
Depois voce deve ativa-lo com o seguinte comando:

```
$ source ./venv/bin/activate
```
Apos ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requirements.txt
```
Para poder ter o primeiro acesso e pode configurar o aplicação vamos executar o comando 
'migrate' para gerar o banco de dados padrão do Django(SQLite). E depois criar o superusuario:
```
(venv)$ ./manage.py migrate
(venv)$ ./manage.py createsuperuser
Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```

Para iniciar o servidor depois deste passo você deve:
```
(venv)$ ./manage.py runserver
```


Para visualizar se tudo esta executando como esperado vamos acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)

