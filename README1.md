# 🛒 Monitoramento de Preço

Este é um projeto em Python para monitoramento de preços de produtos em uma página da web. O script verifica periodicamente o preço e notifica quando o valor desejado é alcançado, ideal para quem quer aproveitar promoções sem precisar checar manualmente.

---

## 🚀 Funcionalidades

- **Monitoramento Automático**: O script acessa automaticamente a página do produto em intervalos definidos.
- **Comparação de Preços**: Compara o preço atual com um valor desejado, notificando quando o preço cai para o valor definido ou abaixo.
- **Configuração Simples**: Fácil de ajustar para qualquer produto, basta alterar a URL e o valor desejado.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍: Linguagem principal do projeto.
- **Requests** 📡: Para fazer requisições HTTP.
- **BeautifulSoup** 🧽: Para analisar e extrair informações do HTML da página.

---

## 📋 Pré-requisitos

- Python 3.x instalado
- Biblioteca Requests (`pip install requests`)
- Biblioteca BeautifulSoup (`pip install beautifulsoup4`)

---

## 📝 Como Usar

1. **Clone o repositório** para o seu ambiente local:

   ```bash
   git clone https://github.com/Djailson1/monitoramento-preco.git
   cd monitoramento-preco