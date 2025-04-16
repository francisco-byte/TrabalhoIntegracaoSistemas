
# 🧠 Projeto: Sistema Cliente-Servidor para Gestão de Produtos com Múltiplas APIs e Interface Gráfica

Este projeto consiste numa aplicação cliente-servidor desenvolvida em Python que permite gerir uma lista de produtos. A aplicação oferece funcionalidades para **visualizar, adicionar, remover e atualizar produtos**, sendo que cada produto possui um **ID, nome, preço e quantidade em stock**.

O servidor disponibiliza diferentes formas de acesso aos dados através de múltiplas tecnologias: **REST, SOAP, gRPC e GraphQL**. O cliente comunica com o servidor através de uma **interface gráfica desenvolvida em Tkinter**, permitindo ao utilizador escolher o tipo de serviço a utilizar para realizar as operações CRUD (Create, Read, Update, Delete).


---

## 🗂️ Estrutura do Projeto

```
.
├── cliente/                   # Interface gráfica Tkinter
│   ├── cliente.py
│   ├── produtos_pb2_grpc.py   # Define os serviços
│   └── produtos_pb2.py        # Define os produtos
|
├── servidor/                 # Implementação dos serviços
│   ├── app_rest/
│   │   ├── app.py           # API REST (FastAPI)
│   │   ├── Dockerfile.rest   # Dockerfile para serviço REST 
│   │   └── requirements.txt
│   ├── app_soap/
│   │   ├── app.py    # API SOAP
│   │   ├── Dockerfile.soap   # Dockerfile para serviço SOAP
│   │   └── requirements.txt
│   ├── app_grpc/
│   │   ├── app.py    # Servidor gRPC
│   │   ├── produtos.proto    # Definição protobuf
│   │   ├── produtos_pb2_grpc.py   # Define os serviços
│   │   ├── produtos_pb2.py        # Define os produtos
│   │   ├── Dockerfile.grpc   # Dockerfile para serviço gRPC
│   │   └── requirements.txt
│   ├── app_graphql/
│   │   ├── graphql_delete.py # API GraphQL
│   │   ├── Dockerfile.graphql # Dockerfile para serviço GraphQL
│   │   └── requirements.txt
│   └── shared/
│       ├── produtos.json     # JSON onde são guardados os produtos
|       └── schema.json       # Define a estrutura dos produtos
├── documentacao/             # Documentação adicional (descrição dos serviços, exemplos Postman, etc)
│   └── README.md             # Este ficheiro
└── docker-compose.yml        # Orquestração dos serviços

```

---

🚀 Tecnologias Utilizadas
Python 3.10+

FastAPI (REST)

Uvicorn (Servidor ASGI para FastAPI)

Strawberry-GraphQL (GraphQL)

gRPC + Protobuf (RPC)

Tkinter (Interface Gráfica - GUI)

JSON (Persistência de dados)

Docker & Docker Compose (Contéineres e Organização dos serviços)

Flask (Usado em REST)

Spyne (SOAP)

---

## ⚙️ Como Correr o Projeto

### Pré-requisitos

- Docker instalado
- Python (opcionalmente, se quiser executar manualmente)

### Com Docker

```bash
docker-compose up --build
```

### Manualmente

#### 1. Servidor

```bash
cd servidor/app_rest
uvicorn main:app --reload --port 8000

cd servidor/app_soap
python soap_server.py

cd servidor/app_grpc
python server_grpc.py

cd servidor/app_graphql
python graphql_server.py
```

#### 2. Cliente

```bash
cd cliente
python cliente.py
```

---

## 📡 Funcionalidades

| Tecnologia | Tipo de API |    CRUD   |
|------------|-------------|-----------|
| REST       | HTTP (JSON) | Create    |
| SOAP       | XML         | Listar    |
| gRPC       | Protobuf    | Atualizar |
| GraphQL    | Query/Mut.  | Remover   |

O cliente Tkinter permite ao utilizador interagir com todas as APIs disponíveis.

---

## 📚 Documentação dos Endpoints/Serviços

A documentação completa dos serviços e exemplos de chamadas está disponível em:

```
/documentacao/descricoes_servicos.md
/documentacao/exemplos_postman.json
```

- REST: Acesso via `http://localhost:8000/docs` (Swagger)
- SOAP: Exemplos em XML e ficheiro Postman incluídos
- gRPC: Chamadas via script cliente gRPC incluído
- GraphQL: Interface gráfica via `http://localhost:8002/graphql`

---

## 📦 Docker Compose Detalhes

```yaml
services:
  rest:
    build: ./Servidor/REST
    ports:
      - "8001:8001"
    volumes:
      - ./Servidor/shared:/shared  
  soap:
    build: ./Servidor/SOAP
    ports:
      - "8002:8002"
    volumes:
      - ./Servidor/shared:/shared  
  graphql:
    build: ./Servidor/GraphQL
    ports:
      - "8004:8004"
    volumes:
      - ./Servidor/shared:/shared  
  grpc:
    build: ./Servidor/GRPC
    ports:
      - "8003:8003"
    volumes:
      - ./Servidor/shared:/shared  
  shared:
    image: alpine
    volumes:
      - ./Servidor/shared:/shared
    command: tail -f /dev/null

```

---


## 👤 Autor

Projeto desenvolvido por Francisco Carvalho dos Reis, no contexto da disciplina de Integração de Sistemas.
