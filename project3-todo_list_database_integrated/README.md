# project3 — TODO List (Database Integrated)

Breve: Aplicação de lista de tarefas com Integração a banco de dados, autenticação e templates.

Como rodar:

```powershell
cd project3-todo_list_database_integrated\TodoApp
uvicorn main:app --reload --port 8000
```

Migrações (Alembic):

```powershell
cd project3-todo_list_database_integrated\TodoApp
alembic upgrade head
```

Arquivos chave:
- `TodoApp/main.py` — entrada da aplicação.
- `TodoApp/routers/` — rotas (`todos.py`, `auth.py`, `user.py`).
- `TodoApp/models.py` — modelos SQLAlchemy.

Testes:
- Execute `pytest` a partir da raiz ou da pasta `TodoApp`.
