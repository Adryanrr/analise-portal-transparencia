# 📊 Análise do Portal da Transparência

Análise de dados extraídos do Portal da Transparência, com foco nos gastos públicos em viagens realizadas em 2023.  
O projeto gera relatórios consolidados e visualizações gráficas para facilitar a interpretação e promover a transparência pública.

## 📁 Estrutura de Pastas

```

analise-portal-transparencia/
├── datasets/
│ └── 2023_Viagem.csv
├── env/ (ambiente virtual)
├── output/
│ ├── Viagens Por cargo público.png
│ ├── tabela_2023.xlsx
│ └── Despesa Média Por cargo público (2023).png
├── app.py
├── requirements.txt
└── README.md

```

## 🛠️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Adryanrr/analise-portal-transparencia.git
cd analise-portal-transparencia
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv env
source env/bin/activate    # Linux/Mac
.\env\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Prepare as pastas

- Certifique-se de que `datasets/2023_Viagem.csv` existe.
- A pasta `output/` será usada para salvar os resultados.

### 5. Execute o script

```bash
python app.py
```

---

## 📊 Resultados Gerados

### 📈 Número de Viagens por Cargo Público (2023)

![Viagens por Cargo Público](./output/Viagens%20Por%20cargo%20p%C3%BAblico.png)

### 💰 Despesa Média por Cargo Público (2023)

![Despesa Média por Cargo Público](<./output/Despesa%20M%C3%A9dia%20Por%20cargo%20p%C3%BAblico%20(2023).png>)

---

## 📦 Tecnologias Utilizadas

[![Python Version](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-blue?logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=matplotlib)](https://matplotlib.org/)
