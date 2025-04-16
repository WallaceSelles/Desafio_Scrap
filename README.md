
# Projeto Cripto: Coleta de Dados de Criptomoedas

Este projeto coleta dados de cotações de criptomoedas de duas formas:

- **Web Scraping** do site [CoinMarketCap](https://coinmarketcap.com)
- **API Pública** da [CoinGecko](https://www.coingecko.com/en/api)

As informações coletadas são salvas em arquivos CSV padronizados na pasta output/.

---

## 📦 Requisitos

Antes de rodar, instale as bibliotecas necessárias com:

bash
pip install -r requirements.txt


### 🧪 Bibliotecas utilizadas

- `requests` – Requisições HTTP (API + Scraping)
- `pandas` – Manipulação de dados e geração dos CSVs
- `beautifulsoup4` – Parse HTML do site CoinMarketCap (scraping)

---

## ▶️ Como Executar

### ✅ Opção 1: Pelo Terminal do VS Code ou CMD

1. Abra o terminal na **pasta raiz do projeto** (onde estão `scraping/`, `api/`, `start.bat`, etc.).
2. Execute os comandos:

bash
python -m scraping.main
python -m api.main


---

### ✅ Opção 2: Pelo `start.bat` (Windows)

Execute o script automático:

- **Via Explorer:** Dê dois cliques em `start.bat`
- **Via terminal:**

cmd
start.bat


---

### ✅ Opção 3: Pelo Git Bash (Windows)

1. Clique com o botão direito na pasta do projeto > “**Git Bash Here**”
2. Rode:

bash
bash start.sh
```

Se necessário, dê permissão de execução:
bash
chmod +x start.sh
./start.sh


---

## 📂 Saída

Os arquivos CSV gerados ficarão disponíveis em:


output/coins_scraping.csv
output/coins_api.csv


Cada arquivo contém:

| Name | Symbol | Price | Market Cap | 24h Volume | Change (24h) |
|------|--------|-------|------------|-------------|--------------|

---

## 📁 Estrutura do Projeto


Projeto_cripto/
├── api/
│   ├── main.py
│   ├── services/
│   │   └── coingecko_api.py
│   └── data/
│       └── writer.py
├── scraping/
│   ├── main.py
│   ├── services/
│   │   └── scraper.py
│   └── data/
│       └── writer.py
├── output/
│   ├── coins_scraping.csv
│   └── coins_api.csv
├── start.bat
├── start.sh
├── README.md
└── requirements.txt

