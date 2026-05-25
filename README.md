# Curso de FastAPI - ericroby

<p>Repositório com projetos de estudo do curso de FastAPI, ministrado em inglês pelo professor ericroby, contendo exemplos práticos, configurações de banco de dados e anotações do processo de aprendizagem.</p>

### Tecnologias utilizadas
<table>
  <tr>
    <td>
        <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a>
    </td>
    <td>
        Framework Python para desenvolvimento dos endpoints do backend de maneira assícrona por padrão.
    </td>
  </tr>
  <tr>
    <td>
        <a href="https://www.sqlalchemy.org/">SQLAlchemy</a>
    </td>
    <td>
      Framework Python ideal para manipulação do banco de dados. O SQLAlchemy é a ORM mais utilizada em linguagem Python.
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://alembic.sqlalchemy.org/en/latest/">Alembic</a>
    </td>
    <td>
      Framework ideal para versionamento do banco de dados.
    </td>
  </tr>
  <tr>
    <td>
      Pytest
    </td>
    <td>
      Framework Python utilizado para testagem básica dos endpoints das aplicações que foram construídas durante o curso.
    </td>
  </tr>
</table>

### Conteúdo programático
- Ciclo de desenvolvimento de APIs com FastAPI (rotas, validação, dependências).
- Autenticação/Autorização básica (JWT/sessions).
- Persistência com SQLAlchemy e migrações com Alembic.
- Testes automatizados com `pytest`.
- Deploy simples (uvicorn/gunicorn e Docker opcional).

### Pré-requisitos
- Python 3.10+ recomendado
- `pip` e ambiente virtual (`venv` ou similar)

## Instalação
1. Criar e ativar um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Instalar dependências (se houver `requirements.txt`):

```powershell
pip install -r requirements.txt
```

3. Copie ou crie um arquivo `.env` conforme necessário (não comitar `.env`).

## Execução

- Projeto TODO (executar dentro de `project3-todo_list_database_integrated/TodoApp`):

```powershell
cd project3-todo_list_database_integrated\TodoApp
uvicorn main:app --reload --port 8000
```

- Projeto Books (exemplo):

```powershell
cd project2-books_complete_restful_api
uvicorn books:app --reload --port 8001
```

### As principais rotas das aplicações desenvolvidas durante o curso
- Consulte os routers em [project3-todo_list_database_integrated/TodoApp/routers](project3-todo_list_database_integrated/TodoApp/routers) (ex.: `todos.py`, `auth.py`, `user.py`).
- Para o projeto Books, veja `books.py` em [project2-books_complete_restful_api](project2-books_complete_restful_api).

### Banco de Dados e Migrações
- Configurações em [project3-todo_list_database_integrated/TodoApp/config.py].
- Rodar migrações (execute a partir de `project3-todo_list_database_integrated/TodoApp`):

```powershell
alembic upgrade head
```

### Link do curso
<h2 align="left">FastAPI course repo</h2>
<p align="left"><a href="https://www.udemy.com/course/fastapi-the-complete-course/">FastAPI - The Complete Course</a> by 
  <a href="https://github.com/codingwithroby">Eric Roby</a></p>
