Este projeto implementa uma API RESTful em Python usando o framework Flask para fornecer a liturgia diária. A API consome uma API externa para obter os dados litúrgicos e os apresenta em um formato padronizado.

## Índice

* [Visão Geral](#visão-geral)
* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Pré-requisitos](#pré-requisitos)
* [Configuração e Instalação](#configuração-e-instalação)
* [Como Executar](#como-executar)
* [Endpoints da API](#endpoints-da-api)
* [Estrutura da Resposta](#estrutura-da-resposta)
* [Limitações do Plano Gratuito e Alternativas](#limitações-do-plano-gratuito-e-alternativas)
* [Contribuição](#contribuição)
* [Licença](#licença)

---

## Visão Geral

Esta API serve como um proxy ou adaptador para a liturgia diária, buscando os dados de uma fonte externa (`https://liturgia.up.railway.app/v2/`) e reformatando-os para uma estrutura de resposta mais simples e consistente. Isso abstrai a complexidade e as possíveis mudanças na API externa, oferecendo um endpoint local estável para suas aplicações.

**A API está atualmente deployada e acessível em:**
👉 **`https://liturgia-api.onrender.com`** 👈

## Funcionalidades

* Obter a liturgia completa para o dia atual.
* Obter a liturgia completa para uma data específica.
* Formatar as leituras (Primeira Leitura, Salmo, Evangelho, etc.) e orações em uma estrutura fácil de usar.

## Tecnologias Utilizadas

* **Python 3.x**
* **Flask:** Micro-framework web para Python.
* **Requests:** Biblioteca HTTP para fazer requisições a APIs externas.
* **Flask-Cors:** Extensão para lidar com requisições Cross-Origin Resource Sharing (CORS) no frontend.
* **Gunicorn:** Servidor WSGI (Web Server Gateway Interface) para deploy em produção.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina.

## Configuração e Instalação

Siga os passos abaixo para configurar e instalar o projeto:

1.  **Clone o repositório** (se estiver em um repositório Git) ou **crie a pasta do projeto**:
    ```bash
    mkdir api_liturgia
    cd api_liturgia
    ```

2.  **Crie e ative um ambiente virtual** (recomendado para isolar as dependências):
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    (Se `python3` não funcionar, tente apenas `python`).

3.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias:
    ```bash
    pip install Flask requests Flask-Cors gunicorn
    ```

4.  **Crie o arquivo `app.py`:**
    Dentro da pasta `api_liturgia`, crie um arquivo chamado `app.py` e cole o código da sua API nele.

5.  **Crie o arquivo `Procfile`:**
    Na raiz do seu projeto (`api_liturgia`), crie um arquivo chamado `Procfile` (sem extensão) com o seguinte conteúdo:
    ```
    web: gunicorn app:app
    ```

## Como Executar

Para executar a API localmente:

Com o ambiente virtual ativado e todas as dependências instaladas, você pode iniciar o servidor Flask:

```bash
python app.py
O servidor será iniciado e estará acessível em http://127.0.0.1:5000 (ou http://localhost:5000). Você verá mensagens de log no seu terminal.
```

###Endpoints da API
A API oferece os seguintes endpoints:

1. Obter Liturgia do Dia Atual
URL: /liturgia
Método: GET
Descrição: Retorna a liturgia completa para o dia em que a requisição é feita.
Exemplo de Uso (local):
[http://127.0.0.1:5000/liturgia](http://127.0.0.1:5000/liturgia)
Exemplo de Uso (em produção):
[https://liturgia-api.onrender.com/liturgia](https://liturgia-api.onrender.com/liturgia)
2. Obter Liturgia para uma Data Específica
URL: /liturgia/<data>
Método: GET
Parâmetros de URL:
<data>: A data desejada no formato DD-MM-AAAA (Dia-Mês-Ano).
Descrição: Retorna a liturgia completa para a data especificada.
Exemplo de Uso (local):
[http://127.0.0.1:5000/liturgia/06-06-2025](http://127.0.0.1:5000/liturgia/06-06-2025)
Exemplo de Uso (em produção):
[https://liturgia-api.onrender.com/liturgia/06-06-2025](https://liturgia-api.onrender.com/liturgia/06-06-2025)
Estrutura da Resposta
Em caso de sucesso (código 200 OK), a API retornará um objeto JSON com a seguinte estrutura:


```
JSON

{
  "cor_liturgica": "Branco",
  "data": "06 de junho de 2025",
  "dia_da_semana": "sexta-feira",
  "leituras": [
    {
      "referencia": "At 25, 13b-21",
      "texto": "Naqueles dias, ... (texto da Primeira Leitura)",
      "tipo": "Primeira Leitura"
    },
    {
      "referencia": "Sl 102",
      "texto": "Refrão: O Senhor pôs o seu trono lá nos céus.\n... (texto do Salmo)",
      "tipo": "Salmo Responsorial"
    },
    {
      "referencia": "Jo 21, 15-19",
      "texto": "Jesus manifestou-se aos seus discípulos ... (texto do Evangelho)",
      "tipo": "Evangelho"
    },
    {
      "referencia": "Não aplicável",
      "texto": "Ó Deus, pela glorificação ... (texto da Oração da Coleta)",
      "tipo": "Oração da Coleta"
    },
    {
      "referencia": "Não aplicável",
      "texto": "Senhor, olhai compassivo ... (texto da Oração das Oferendas)",
      "tipo": "Oração das Oferendas"
    },
    {
      "referencia": "Não aplicável",
      "texto": "Ó Deus, que nos purificais ... (texto da Oração da Comunhão)",
      "tipo": "Oração da Comunhão"
    }
  ],
  "reflexao": "Reflexão não disponível",
  "titulo": "6ª feira da 7ª Semana da Páscoa"
}
```

Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes (se você criar um).
