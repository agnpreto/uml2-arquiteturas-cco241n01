# Trabalho de Análise e Projeto de Sistemas: Arquiteturas de Software

**Disciplina:** Análise e Projeto de Sistemas — Ciência da Computação  
**Equipe:** Os Mugiwaras  
**Modelo escolhido:** 1 — Delivery de Comida  
**Prazo:** 18/11/2026

## Equipe

| Nome | Usuário do GitHub |
|---|---|
| Daniela Yasmin | [@danielapicanco](https://github.com/danielapicanco) |
| David Castro | [@Davi-Astro](https://github.com/Davi-Astro) |
| Elisabete Marques | [@ElizabethFernandes30](https://github.com/ElizabethFernandes30) |
| Guilherme Castro | [@BatataSayajin](https://github.com/BatataSayajin) |
| Isaque Queiroz | [@isaacaqueiroz](https://github.com/isaacaqueiroz) |
| Luiz Ricardo | [@xXBR4BOXx](https://github.com/xXBR4BOXx) |
| Paulo Vieira | [@paulo-cco](https://github.com/paulo-cco) |

---

## 1. Sobre o projeto

O projeto consiste no desenvolvimento de um sistema de delivery de comida utilizando a arquitetura de **microsserviços**.

O sistema permite cadastrar e consultar clientes, consultar restaurantes, realizar pedidos e registrar pagamentos.

A solução foi desenvolvida com serviços independentes, que se comunicam por meio de APIs REST. Para centralizar o acesso às funcionalidades, foi implementado um API Gateway.

## 2. Arquitetura do sistema

A arquitetura é composta por quatro microsserviços e um API Gateway.

### Microsserviços

| Serviço | Tecnologia | Porta | Responsabilidade |
|---|---|---:|---|
| Restaurantes | Java + Spring Boot | 8080 | Cadastro e consulta de restaurantes |
| Clientes | Java + Spring Boot | 8081 | Cadastro e consulta de clientes |
| Pedidos | Java + Spring Boot | 8082 | Criação e consulta de pedidos |
| Pagamentos | Java + Spring Boot | 8083 | Registro e consulta de pagamentos |
| API Gateway | C# + ASP.NET Core + YARP | 5000 | Centralização e encaminhamento das requisições |

### Comunicação entre os serviços

- O API Gateway recebe as requisições e encaminha para o microsserviço correspondente.
- O serviço de Pedidos consulta Clientes e Restaurantes para validar os dados antes de registrar um pedido.
- O serviço de Pagamentos consulta Pedidos para verificar se o pedido informado existe.
- Os microsserviços se comunicam por meio de APIs REST.

### Banco de dados

Foi utilizado o padrão **Database per Service**, no qual cada microsserviço possui seu próprio banco de dados independente.

| Microsserviço | Banco de dados |
|---|---|
| Restaurantes | `db_restaurantes` |
| Clientes | `db_clientes` |
| Pedidos | `db_pedidos` |
| Pagamentos | `db_pagamentos` |

Os serviços não acessam diretamente os bancos de dados uns dos outros. A comunicação acontece exclusivamente por meio das APIs.

## 3. Tecnologias utilizadas

- Java
- Spring Boot
- Spring Web
- Spring Data JPA
- C#
- ASP.NET Core
- YARP Reverse Proxy
- MySQL
- Maven
- Postman
- Git e GitHub

## 4. Estrutura do projeto

```text
Delivery-de-comida-cco241n01/
│
├── docs/
│   └── requisitos.md
│
├── servicos/
│   ├── restaurantes/
│   ├── clientes/
│   ├── pedidos/
│   └── pagamentos/
│
├── Gateway/
│
├── EQUIPES.md
├── LOGS.md
└── README.md
```

## 5. Como executar o projeto

### Pré-requisitos

- Java instalado
- .NET SDK instalado
- MySQL instalado e em execução
- Git instalado
- Postman para testar as APIs

### 5.1. Configuração dos bancos de dados

Antes de executar os serviços, é necessário criar os seguintes bancos no MySQL:

- `db_restaurantes`
- `db_clientes`
- `db_pedidos`
- `db_pagamentos`

Também devem ser configurados os usuários e as permissões individuais de cada banco.

### 5.2. Configuração das variáveis de ambiente

As senhas dos bancos são recebidas por variáveis de ambiente:

| Serviço | Variável |
|---|---|
| Restaurantes | `DB_PASSWORD` |
| Clientes | `DB_PASSWORD_CLIENTES` |
| Pedidos | `DB_PASSWORD_PEDIDOS` |
| Pagamentos | `DB_PASSWORD_PAGAMENTOS` |

Exemplo de configuração no Git Bash:

```bash
export DB_PASSWORD="sua_senha"
export DB_PASSWORD_CLIENTES="sua_senha"
export DB_PASSWORD_PEDIDOS="sua_senha"
export DB_PASSWORD_PAGAMENTOS="sua_senha"
```

Substitua os valores pelas senhas configuradas no seu ambiente. Não compartilhe senhas nem as envie para o GitHub.

### 5.3. Inicialização dos microsserviços

Abra um terminal para cada microsserviço, acesse sua respectiva pasta e execute:

```bash
./mvnw spring-boot:run
```

Os serviços devem ser iniciados nas seguintes portas:

- Restaurantes: `8080`
- Clientes: `8081`
- Pedidos: `8082`
- Pagamentos: `8083`

### 5.4. Inicialização do API Gateway

Em outro terminal, acesse a pasta `Gateway`:

```bash
cd Gateway
dotnet run
```

O Gateway ficará disponível em:

```text
http://localhost:5000
```

## 6. Testes da aplicação

Os testes das APIs foram realizados utilizando o Postman, com as requisições encaminhadas pelo API Gateway.

### Exemplos de endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/clientes` | Listar clientes |
| POST | `/clientes` | Cadastrar cliente |
| GET | `/restaurantes` | Listar restaurantes |
| POST | `/restaurantes` | Cadastrar restaurante |
| GET | `/pedidos` | Listar pedidos |
| POST | `/pedidos` | Criar pedido |
| GET | `/pagamentos` | Listar pagamentos |
| POST | `/pagamentos` | Registrar pagamento |

Todos os endpoints podem ser acessados pelo endereço:

```text
http://localhost:5000
```

### Exemplo de criação de pedido

```http
POST http://localhost:5000/pedidos
```

Corpo da requisição:

```json
{
  "clienteId": 2,
  "restauranteId": 2,
  "dataPedido": "2026-11-25T19:00:00",
  "status": "PENDENTE",
  "valorTotal": 65.90
}
```

O serviço de Pedidos consulta os serviços de Clientes e Restaurantes para validar as informações antes de salvar o pedido.

### Exemplo de registro de pagamento

```http
POST http://localhost:5000/pagamentos
```

Corpo da requisição:

```json
{
  "pedidoId": 5,
  "valor": 65.90,
  "dataPagamento": "2026-11-25T19:05:00",
  "status": "APROVADO",
  "metodoPagamento": "PIX"
}
```

O serviço de Pagamentos consulta o serviço de Pedidos para validar a existência do pedido informado.

**Observação:** o projeto realiza o registro de pagamentos e a simulação de seus status. Não há integração com uma plataforma financeira real.

## 7. Validações implementadas

O sistema possui validações entre os microsserviços:

- Não permite registrar pedidos com clientes inexistentes.
- Não permite registrar pedidos com restaurantes inexistentes.
- Não permite registrar pagamentos vinculados a pedidos inexistentes.
- Retorna respostas HTTP adequadas para operações inválidas.

## 8. Objetivos alcançados

- Implementação de quatro microsserviços independentes.
- Desenvolvimento de APIs REST com Spring Boot.
- Integração entre os serviços por meio de requisições HTTP.
- Utilização de bancos de dados independentes.
- Implementação de API Gateway com ASP.NET Core e YARP.
- Testes das operações utilizando Postman.

## 9. Considerações finais

O projeto demonstra a aplicação prática da arquitetura de microsserviços, destacando a independência dos serviços, a comunicação por APIs REST, a separação dos bancos de dados e a utilização de um API Gateway para centralizar o acesso à aplicação.

A implementação permite compreender como diferentes componentes podem trabalhar de forma integrada, mantendo suas próprias responsabilidades e estruturas independentes.

---

**Equipe Os Mugiwaras — Modelo 1: Delivery de Comida.**
