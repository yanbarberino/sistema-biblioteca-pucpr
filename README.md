# 🤖 Sistema de Gerenciamento de Biblioteca Digital (PUCPR)

**Projeto da disciplina de Programação para Ciência de Dados.**

Este projeto é um sistema de linha de comando (CLI) desenvolvido em Python para auxiliar bibliotecários na gestão de documentos digitais, conforme solicitado na Hora da Prática 2.

---

## 🚀 Funcionalidades Implementadas

O sistema, executado através do arquivo `gerenciador.py`, permite as seguintes operações:

* **1. Listar Documentos:** Varre a pasta `biblioteca/` e exibe todos os arquivos existentes, organizados por suas respectivas pastas (Tipo e Ano).
* **2. Adicionar Documento:** Solicita ao usuário o caminho de um arquivo (ex: um PDF nos Downloads), o tipo (ex: PDF) e o ano (ex: 2023). O sistema então copia o arquivo para a pasta correta, criando a estrutura `biblioteca/TIPO/ANO/` automaticamente.
* **3. Renomear Documento:** Permite renomear um arquivo que já está dentro da biblioteca.
* **4. Remover Documento:** Permite apagar um arquivo da biblioteca, com uma etapa de confirmação para segurança.
* **5. Sair:** Encerra o programa.

---

## 🛠️ Como Usar

### Pré-requisitos

* Python 3.x instalado.

### Execução

1.  Clone este repositório para sua máquina local:
    ```bash
    git clone [https://github.com/yanbarberino/sistema-biblioteca-pucpr.git](https://github.com/yanbarberino/sistema-biblioteca-pucpr.git)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd sistema-biblioteca-pucpr
    ```
3.  Execute o script principal:
    ```bash
    python gerenciador.py
    ```
4.  O menu principal aparecerá, permitindo que você escolha a operação desejada.

---

## 📁 Estrutura de Diretórios

O sistema organiza os arquivos automaticamente na seguinte estrutura:

biblioteca/ │ ├── PDF/ │ ├── 2023/ │ │ └── artigo_ia.pdf │ └── 2022/ │ └── tese_computacao.pdf │ └── ePUB/ └── 2023/ └── livro_python.epub

## 🧑‍💻 Autor

* **Yan Barberino**
* [GitHub](https://github.com/yanbarberino)