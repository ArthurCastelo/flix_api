


# 🎬 Flix API

API RESTful desenvolvida com **Django REST Framework (DRF)** para gerenciamento de filmes, atores, gêneros e avaliações.  
O projeto tem foco em **boas práticas**, segurança com **JWT (Access/Refresh Tokens)** e deploy 100% em nuvem usando **PythonAnywhere**.  

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Django 5+**
- **Django REST Framework**
- **SimpleJWT** para autenticação
- **Flake8** para linting (PEP8)
- **Git + GitHub** para versionamento
- **PythonAnywhere** para deploy em nuvem

---

## 🔑 Funcionalidades

- CRUD completo para:
  - Filmes
  - Atores
  - Gêneros
  - Avaliações
- Autenticação JWT:
  - `access token` e `refresh token`
- Endpoints RESTful seguindo PEP8
- Deploy em nuvem (PythonAnywhere)

---

## 📂 Estrutura dos Endpoints

Base URL da API:  
[https://arthurcastelo.pythonanywhere.com/api/v1/movies/](https://arthurcastelo.pythonanywhere.com/api/v1/]

Endpoints disponíveis (basta trocar o final):

- `/movies/`
- `/actors/`
- `/reviews/`
- `/genres/`

---

## 🔐 Autenticação

### Criar Token
Endpoint:  

POST /api/token/

Exemplo de credenciais já disponíveis para teste:  
- **Usuário:** `teste`  
- **Senha:** `teste@123`

A resposta retorna `access` e `refresh`.  
Use o `access token` no **Authorization Header**:  



Authorization: Bearer <seu_token>


---

## 🛠️ Como Rodar Localmente

```bash
git clone https://github.com/ArthurCastelo/flix_api.git
cd flix_api
python -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🧪 Testando a API

Pode usar Insomnia ou Postman.
Exemplo de fluxo de teste:

Criar token (/api/token/)

Copiar access token

Usar nos endpoints (/movies/, /actors/ etc) com CRUD completo.

📦 Boas Práticas

requirements.txt → dependências do projeto

requirements-dev.txt → dependências extras para dev

.gitignore → evita arquivos desnecessários no repositório

flake8 → validação de estilo e PEP8

🌐 Deploy

Deploy feito com PythonAnywhere, disponível publicamente:
👉 Flix API em Produção

📌 Links

🔗 GitHub: ArthurCastelo/flix_api

🔗 Deploy: arthurcastelo.pythonanywhere.com
