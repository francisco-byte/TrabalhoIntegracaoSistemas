
# 🧠 Projeto: Sistema Cliente-Servidor com Múltiplas APIs e Interface Gráfica

Este projeto consiste numa aplicação cliente-servidor desenvolvida em Python que utiliza diversas tecnologias para comunicação entre o cliente e o servidor, incluindo REST, SOAP, gRPC e GraphQL. O cliente oferece uma interface gráfica desenvolvida com Tkinter.

---

## 🗂️ Estrutura do Projeto

```
.
├── cliente/                   # Interface gráfica Tkinter
│   ├── cliente.py
│   └── ...
├── servidor/                 # Implementação dos serviços
│   ├── app_rest/
│   │   └── main.py           # API REST (FastAPI)
│   ├── app_soap/
│   │   └── soap_server.py    # API SOAP
│   ├── app_grpc/
│   │   ├── server_grpc.py    # Servidor gRPC
│   │   └── mensagens.proto   # Definição protobuf
│   ├── app_graphql/
│   │   └── graphql_server.py # API GraphQL
│   └── db/
│       └── database.py       # Simulação de base de dados
├── documentacao/             # Documentação adicional (descrição dos serviços, exemplos Postman, etc)
│   ├── exemplos_postman.json
│   ├── descricoes_servicos.md
│   └── ...
├── docker-compose.yml        # Orquestração dos serviços
├── Dockerfile.rest           # Dockerfile para serviço REST
├── Dockerfile.soap           # Dockerfile para serviço SOAP
├── Dockerfile.grpc           # Dockerfile para serviço gRPC
├── Dockerfile.graphql        # Dockerfile para serviço GraphQL
└── README.md                 # Este ficheiro
```

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- FastAPI (REST)
- Zeep / Spyne (SOAP)
- gRPC + Protobuf
- Graphene / Ariadne (GraphQL)
- Tkinter (GUI)
- SQLite / JSON (dados persistentes)
- Docker & Docker Compose

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

| Tecnologia | Tipo de API | CRUD |
|------------|-------------|------|
| REST       | HTTP (JSON) | Sim |
| SOAP       | XML         | Sim |
| gRPC       | Protobuf    | Sim |
| GraphQL    | Query/Mut.  | Sim |

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
    build:
      context: .
      dockerfile: Dockerfile.rest
    ports:
      - "8000:8000"
  soap:
    build:
      context: .
      dockerfile: Dockerfile.soap
    ports:
      - "8001:8001"
  grpc:
    build:
      context: .
      dockerfile: Dockerfile.grpc
    ports:
      - "50051:50051"
  graphql:
    build:
      context: .
      dockerfile: Dockerfile.graphql
    ports:
      - "8002:8002"
```

---

## 📝 Entrega

### Repositório GitHub com:

- [x] Código fonte do servidor e cliente (bem estruturado e documentado)
- [x] Dockerfiles e docker-compose.yml
- [x] Documentação completa:
  - [x] Descrição detalhada dos endpoints/serviços
  - [x] README.md com instruções claras de execução
  - [x] Exemplos de chamadas Postman
  - [x] Esquemas de validação (nos ficheiros da pasta /documentacao)
  - [ ] Vídeo de demonstração (até 8 minutos)

### Estrutura sugerida:

```
/servidor
/cliente
/documentacao
docker-compose.yml
```

### Acesso ao Repositório GitHub:

- Adicionar o professor como colaborador com permissões de leitura.
- Realizar commits frequentes com mensagens claras.

---

## 👤 Autor

Projeto desenvolvido por [Teu Nome Aqui], no contexto da disciplina de Integração de Sistemas.
