# Curso FastAPI — Diário de Aprendizagem

Descrição: Repositório com projetos de estudo do curso de FastAPI, contendo exemplos práticos, configurações de banco de dados e anotações do processo de aprendizagem.

## Sumário
- Objetivos de Aprendizagem
- Visão Geral dos Projetos
- Pré-requisitos
- Instalação
- Execução
- Endpoints Principais
- Banco de Dados e Migrações
- Testes
- Diário de Estudos
- Recursos
- Contribuição
- Licença

## Objetivos de Aprendizagem
- Compreender o ciclo de desenvolvimento de APIs com FastAPI (rotas, validação, dependências).
- Autenticação/Autorização básica (JWT/sessions).
- Persistência com SQLAlchemy e migrações com Alembic.
- Testes automatizados com `pytest`.
- Deploy simples (uvicorn/gunicorn e Docker opcional).

## Visão Geral dos Projetos
- [project2-books_complete_restful_api](project2-books_complete_restful_api): API de livros (REST). Consulte o arquivo principal `books.py`.
- [project3-todo_list_database_integrated](project3-todo_list_database_integrated): Aplicação TODO com integração de banco, templates e autenticação (código em `TodoApp`).

## Pré-requisitos
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

## Endpoints Principais
- Consulte os routers em [project3-todo_list_database_integrated/TodoApp/routers](project3-todo_list_database_integrated/TodoApp/routers) (ex.: `todos.py`, `auth.py`, `user.py`).
- Para o projeto Books, veja `books.py` em [project2-books_complete_restful_api](project2-books_complete_restful_api).

## Banco de Dados e Migrações
- Configurações em [project3-todo_list_database_integrated/TodoApp/config.py].
- Rodar migrações (execute a partir de `project3-todo_list_database_integrated/TodoApp`):

```powershell
alembic upgrade head
```

## Testes
- Executar testes com `pytest` a partir da raiz do repositório ou da pasta do projeto correspondente:

```powershell
pytest -q
```

## Diário de Estudos
Mantenha entradas curtas com formato:

- `YYYY-MM-DD — Tema`
  - Resumo: O que foi feito/entendido.
  - Código/links relevantes.
  - Tempo gasto.

Exemplo:

- 2026-05-24 — Autenticação JWT
  - Resumo: Implementei login e verificação de token via dependência.
  - Recursos: FastAPI docs, tutorial X.
  - Tempo: 1h30

## Recursos
- FastAPI docs: https://fastapi.tiangolo.com
- SQLAlchemy: https://www.sqlalchemy.org
- Alembic: https://alembic.sqlalchemy.org

## Contribuição
- Convenção de commits sugerida: `tipo: mensagem curta` (ex.: `feat: adicionar endpoint de login`).

## Licença
- Adicione aqui a licença que deseja usar (ex.: MIT).
<h2 align="left">FastAPI course repo</h2>
<p align="left"><a href="https://www.udemy.com/course/fastapi-the-complete-course/">FastAPI - The Complete Course</a> by 
  <a href="https://github.com/codingwithroby">Eric Roby</a></p>

<h2 align="left">Folder Structure</h2>
<h4 align="left">Project 1: Explicit Status Code Responde</h4>
