import pandas as pd

# Carregar datasets
customers = pd.read_csv('dataset/olist_customers_dataset.csv')
orders = pd.read_csv('dataset/olist_orders_dataset.csv')
items = pd.read_csv('dataset/olist_order_items_dataset.csv')
products = pd.read_csv('dataset/olist_products_dataset.csv')
payments = pd.read_csv('dataset/olist_order_payments_dataset.csv')
reviews = pd.read_csv('dataset/olist_order_reviews_dataset.csv')
sellers = pd.read_csv('dataset/olist_sellers_dataset.csv')

print("=" * 60)
print("ANÁLISE EXPLORATÓRIA - DADOS OLIST")
print("=" * 60)

print("\n1. TOTAL DE REGISTROS POR TABELA:")
print(f"   Clientes: {len(customers):,}")
print(f"   Pedidos: {len(orders):,}")
print(f"   Itens: {len(items):,}")
print(f"   Produtos: {len(products):,}")
print(f"   Pagamentos: {len(payments):,}")
print(f"   Avaliações: {len(reviews):,}")
print(f"   Vendedores: {len(sellers):,}")

print("\n2. STATUS DOS PEDIDOS:")
print(orders['order_status'].value_counts().to_string())

print("\n3. TOP 10 CIDADES POR NÚMERO DE CLIENTES:")
print(customers['customer_city'].value_counts().head(10).to_string())

print("\n4. FORMAS DE PAGAMENTO:")
print(payments['payment_type'].value_counts().to_string())

print("\n5. ESTATÍSTICAS DE PREÇO (ITENS):")
print(f"   Média: R$ {items['price'].mean():.2f}")
print(f"   Mediana: R$ {items['price'].median():.2f}")
print(f"   Máximo: R$ {items['price'].max():.2f}")
print(f"   Mínimo: R$ {items['price'].min():.2f}")

print("\n6. AVALIAÇÕES - DISTRIBUIÇÃO:")
print(reviews['review_score'].value_counts().sort_index().to_string())

print("\n7. TOP 10 ESTADOS POR CLIENTES:")
uf_count = customers['customer_state'].value_counts().head(10)
print(uf_count.to_string())

print("\n" + "=" * 60)
print("DADOS CARREGADOS COM SUCESSO!")
print("=" * 60)
