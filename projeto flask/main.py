import os


#mvc


p = input("Projeto: ")

for d in ["controllers", "services", "repositories", "models"]:
    os.makedirs(f"{p}/app/{d}", exist_ok=True)
    open(f"{p}/app/{d}/__init__.py", "w").close()

open(f"{p}/app/__init__.py", "w").close()


# -----------------------------------------

import os

p = input("Nome do projeto: ")

estrutura = [
    'app/controllers',
    "app/services",
    'app/repositories',
    "app/models",
    "templates"
]

arquivos = [
    'app/__init__.py',
    'app/controllers/user_controller.py',
    "app/services/user_service.py",
    "app/repositories/user_repository.py",
    "app/models/user_model.py",
    "templates/index.html",
    "run.py",
    "config.py"
]

for pasta in estrutura:
    os.makedirs(f"{p}/{pasta}", exist_ok=True)

for arquivo in arquivos:
    open(f"{p}/{arquivo}", "w").close()

print("Estrutura criada.")

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRUD</title>
  <style>
    /* Configuração global para centralizar o conteúdo e garantir fundo branco */
    body {
      background-color: #ffffff;
      font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      margin: 0;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      color: #333;
    }

    /* Container principal para abraçar os elementos de forma organizada */
    .container {
      width: 100%;
      max-width: 600px;
      text-align: center;
    }

    .title {
      background-color: aqua;
      padding: 20px; 
      margin-bottom: 30px;
      border-radius: 8px;
    }

    /* Estilização da tabela */
    table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 15px;
      background-color: #fff;
      box-shadow: 0 2px 5px rgba(0,0,0,0.05);
      border: 1px solid #eee;
    }

    th, td {
      padding: 12px;
      border: 1px solid #ddd;
      text-align: center;
    }

    th {
      background-color: #f8f9fa;
    }

    /* Botões de ação (links) */
    .link {
      text-decoration: none;
      margin: 0 5px;
      padding: 6px 12px;
      background-color: beige;
      color: #333;
      border: 1px solid #ccc;
      border-radius: 4px;
      display: inline-block;
      transition: background-color 0.2s;
    }

    .link:hover {
      background-color: #e6e6d8;
    }

    /* Formulário de cadastro */
    form {
      margin-top: 30px;
      padding: 20px;
      border: 1px solid #eee;
      border-radius: 8px;
      background-color: #fefefe;
      display: flex;
      justify-content: center;
      gap: 10px;
    }

    input {
      padding: 8px 12px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }

    button {
      padding: 8px 16px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
    }

    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>

<div class="container">

  <h1 class="title">Usuários</h1>

  {% for u in users %}
  <table>
    <tr>
      <th>ID</th>
      <th>NOME</th>
      <th>AÇÕES</th>
    </tr>
    <tr>
      <td>{{u["id"]}}</td>   
      <td>{{u["name"]}}</td>
      <td>
        <a class="link" href="/delete/{{u['id']}}">Excluir</a>
        <a class="link" href="/edit/{{u['id']}}">Editar</a>
      </td>
    </tr>
  </table>
  {% endfor %}     

  <form method="POST" action="/add">
    <input name="name" placeholder="Nome" required>
    <button type="submit">Adicionar</button>
  </form>

</div>

</body>
</html>
]
# 1. Importa a função que cria o Flask (ajustado para o padrão comum de pacotes)
try:
    from app import create_app
except ModuleNotFoundError:
    # Caso seu arquivo se chame app.py na raiz, usamos o import direto
    from app.app import create_app 


# 2. Importa a inicialização do banco de dados que criamos
from app.repositories.user_repository import init_db


# 3. Inicializa a variável 'app' chamando a função de fábrica (Application Factory)
app = create_app()


if __name__ == "__main__":
    init_db()        # Garante que a tabela 'users' exista no SQLite antes de ligar o servidor
    app.run(debug=True)