# API de Liturgia Diária

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
* [Contribuição](#contribuição)
* [Licença](#licença)

---

## Visão Geral

Esta API serve como um proxy ou adaptador para a liturgia diária, buscando os dados de uma fonte externa (`https://liturgia.up.railway.app/v2/`) e reformatando-os para uma estrutura de resposta mais simples e consistente. Isso abstrai a complexidade e as possíveis mudanças na API externa, oferecendo um endpoint local estável para suas aplicações.

**A API está atualmente deployada e acessível em:**
**`[API deploy](https://liturgia-api.onrender.com/liturgia)`**

## Funcionalidades

* Obter a liturgia completa para o dia atual.
* Obter a liturgia completa para uma data específica.
* Formatar as leituras (Primeira Leitura, Salmo, Evangelho, etc.) e orações em uma estrutura fácil de usar.

## Tecnologias Utilizadas

* **Python 3.x**
* **Flask:** Micro-framework web para Python.
* **Requests:** Biblioteca HTTP para fazer requisições a APIs externas.
* **Gunicorn:** Servidor WSGI para deploy em produção.

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
    pip install Flask requests gunicorn
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
