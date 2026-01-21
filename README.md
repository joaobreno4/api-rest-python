# API REST com FastAPI, Docker e SQLite

API REST desenvolvida em **Python** utilizando **FastAPI**, com persistência de dados em **SQLite**, containerização com **Docker** e orquestração com **Docker Compose**.  
Projeto focado em **boas práticas de backend e DevOps**, simulando um ambiente real de desenvolvimento.

---

## 🚀 Tecnologias Utilizadas

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Docker
- Docker Compose
- Swagger / OpenAPI

---

## 📦 Funcionalidades

- ✅ Criar usuários
- ✅ Listar usuários
- ✅ Buscar usuário por ID
- ✅ Deletar usuário
- ✅ Persistência de dados com volume Docker
- ✅ Documentação automática com Swagger

---

## 🏗️ Arquitetura do Projeto

- **FastAPI** como framework web
- **SQLAlchemy ORM** para acesso ao banco
- **SQLite** como banco de dados
- **Docker** para containerização
- **Docker Compose** para orquestração
- **Swagger** para documentação e testes da API

---

## ▶️ Como Executar o Projeto

### Pré-requisitos
- Docker
- Docker Compose

### Subir a aplicação
```bash
docker compose up --build -d
🌐 Acessos
API: http://localhost:8000

Swagger UI: http://localhost:8000/docs

🧪 Exemplo de Requisição
Criar usuário (POST /usuarios)
{
  "id": 1,
  "nome": "João",
  "email": "joao@email.com"
}
📁 Estrutura de Pastas
.
├── main.py
├── database.py
├── models.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .dockerignore
📌 Objetivo do Projeto
Projeto desenvolvido para aprendizado prático de:

APIs REST

Docker e Docker Compose

Persistência de dados

Organização de código backend

Fluxo real de desenvolvimento e deploy

👤 Autor
João Breno
GitHub: https://github.com/joaobreno4