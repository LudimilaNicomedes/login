# 🔐 Sistema de Login & Cadastro Full Stack

Este é um sistema completo de autenticação de usuários (Login e Cadastro) desenvolvido com uma arquitetura Full Stack. O projeto integra uma interface moderna e responsiva a uma API robusta conectada a um banco de dados relacional, além de contar com um assistente virtual integrado via webhook.

---

## 🚀 Funcionalidades

*   **Autenticação Completa:** Cadastro de novos usuários e validação de credenciais de login em tempo real.
*   **Segurança e Validação:** Uso de schemas estruturados no back-end para validação de dados de entrada e prevenção de cadastros duplicados.
*   **Carrossel Interativo:** Slider de imagens dinâmico na tela de login criado puramente com JavaScript (DOM e timers).
*   **Integração com Assistente Virtual:** Chat inteligente acoplado diretamente à interface, integrado a fluxos de automação através de Webhook (n8n).
*   **Conexão Segura:** Configuração de políticas de CORS para garantir a comunicação segura entre o front-end e o back-end.

---

## 🛠️ Tecnologias Utilizadas

### **Front-end**
*   **HTML5 & CSS3:** Estruturação semântica e estilização moderna (Flexbox, variáveis e responsividade).
*   **JavaScript (ES6+):** Manipulação dinâmica de elementos (DOM), controle do carrossel e consumo assíncrono da API via `Fetch API`.

### **Back-end**
*   **Python (FastAPI):** Criação de rotas assíncronas de alta performance para a API de autenticação.
*   **Pydantic:** Criação de schemas de validação de dados (`UsuarioSchema` e `LoginSchema`).

### **Banco de Dados**
*   **SQL Server & pyodbc:** Armazenamento seguro de dados cadastrais e execução de queries relacionais.

### **Automação & Integrações**
*   **n8n (Workflow Automation):** Criação e hospedagem de um fluxo de automação via Webhook para processar mensagens e gerenciar o comportamento do assistente virtual em tempo real.
*   
*   👉 [Clique aqui para acessar o projeto no ar](https://sistema-simples-login.netlify.app/)
