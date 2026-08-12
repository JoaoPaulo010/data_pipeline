# Data Pipeline - Projeto Olist

## Visão Geral

Projeto de engenharia de dados focado em ingestão e processamento dos dados públicos da **Olist**, maior plataforma de e-commerce do Brasil. O pipeline é construído para demonstrar conceitos fundamentais de Data Engineering, incluindo extração, transformação e carga de dados (ELT/ETL).

## Objetivos

- Projetar e implementar um pipeline de dados escalável
- Aplicar conceitos de modelagem dimensional (fatos e dimensões)
- Trabalhar com dados reais de e-commerce brasileiro
- Demonstração de boas práticas em engenharia de dados

## Dados Utilizados

O dataset público da Olist contém approximately 100k pedidos realizados entre 2016 e 2018, incluindo:

| Tabela | Descrição |
|--------|-----------|
| `olist_orders_dataset` | Pedidos com status, timestamps de aprovação e entrega |
| `olist_order_items_dataset` | Itens de cada pedido (produtos, vendedores, frete) |
| `olist_order_payments_dataset` | Formas de pagamento parcelado |
| `olist_order_reviews_dataset` | Avaliações dos clientes |
| `olist_products_dataset` | Atributos dos produtos (categoria, dimensões, peso) |
| `olist_sellers_dataset` | Dados dos vendedores |
| `olist_customers_dataset` | Dados dos clientes |
| `olist_geolocation_dataset` | Coordenadas geográficas por CEP |

## Estrutura do Projeto

```
data_pipeline/
├── data/
│   ├── raw/                    # Dados brutos originais
│   ├── staging/                # Dados em staging (pré-transformação)
│   └── warehouse/              # Dados modelados (star schema)
├── scripts/
│   ├── ingestao/               # Scripts de ingestão dos dados
│   ├── transformacao/          # Scripts de transformação (T)
│   ├── qualidade/              # Scripts de qualidade dos dados
│   └── utilitarios/            # Funções auxiliares
├── models/
│   └── dimensoes_fatos.md      # Documentação do modelo dimensional
├── tests/
│   └── data_quality/           # Testes de qualidade
├── docker-compose.yml          # Orquestração dos serviços
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

## Fluxo do Pipeline

```
[Fonte: Olist CSV] 
       ↓
[1. INGESTÃO - Extração dos dados brutos]
       ↓
[2. STAGING - Validação e padronização]
       ↓
[3. TRANSFORMAÇÃO - Limpeza e modelagem]
       ↓
[4. WAREHOUSE - Carga nas tabelas de fatos e dimensões]
       ↓
[5. QUALIDADE - Validação e testes]
```

## Modelo Dimensional (Star Schema)

### Tabelas de Fato

- **fato_pedidos** - Fato granular: cada linha = 1 item de pedido
  - Chave: `sk_pedido_item`
  - Medidas: `preco_item`, `valor_frete`, `preco_total`

### Tabelas de Dimensão

- **dim_cliente** - Dados do comprador
- **dim_vendedor** - Dados do comerciante
- **dim_produto** - Atributos do produto
- **dim_pagamento** - Forma e parcelamento
- **dim_avaliacao** - Nota e comentários
- **dim_data** - Dimensão temporal
- **dim_geolocalizacao** - Localização geográfica

## Tecnologias

- **Python 3.10+** - Linguagem principal
- **Pandas** - Processamento de dados
- **SQL** - Consultas e modelagem
- **Docker** - Containerização
- **Great Expectations** - Qualidade dos dados (opcional)

## Setup

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd data_pipeline

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute o pipeline
python scripts/pipeline_principal.py
```

## Aluno

**João Paulo**  
Disciplina: Data Pipeline

## Licença

Projeto acadêmico para fins de estudo.
