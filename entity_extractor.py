import pandas as pd

# Load the dataset with low_memory=False to handle large files
df = pd.read_csv('amazon_sales_report.csv', low_memory=False)


# Rename columns: remove spaces and convert to lowercase
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Data Cleaning: Fill or drop null values as appropriate

# Extract Orders
try:
    orders = df[['order_id', 'date', 'status', 'fulfilment', 'sales_channel', 'currency', 'amount', 'promotion-ids']].copy()
    orders = orders.drop_duplicates().reset_index(drop=True)

    # Fill null values for numeric columns with 0 and categorical with a placeholder
    orders['amount'] = orders['amount'].fillna(0)
    orders['promotion-ids'] = orders['promotion-ids'].fillna('no_promotion')

    # Save to CSV
    orders.to_csv('entities/orders.csv', index=False)
except KeyError as e:
    print(f"Error extracting Orders: {e}")

# Extract Products
try:
    products = df[['sku', 'style', 'category', 'size', 'asin']].copy()
    products = products.drop_duplicates().reset_index(drop=True)

    # Handle nulls by filling with a placeholder
    products = products.fillna('unknown')

    # Save to CSV
    products.to_csv('entities/products.csv', index=False)
except KeyError as e:
    print(f"Error extracting Products: {e}")

# Extract Customers
try:
    customers = df[['ship-city', 'ship-state', 'ship-postal-code', 'ship-country']].copy()
    customers = customers.drop_duplicates().reset_index(drop=True)

    # Handle nulls by filling with a placeholder
    customers = customers.fillna({'ship-city': 'unknown', 'ship-state': 'unknown', 'ship-postal-code': 'unknown', 'ship-country': 'unknown'})

    # Save to CSV
    customers.to_csv('entities/customers.csv', index=False)
except KeyError as e:
    print(f"Error extracting Customers: {e}")


# Extract Merchants
try:
    merchants = df[['order_id', 'fulfilled-by']].copy()
    merchants = merchants.drop_duplicates().reset_index(drop=True)

    # Handle nulls by filling with a placeholder
    merchants['fulfilled-by'] = merchants['fulfilled-by'].fillna('unknown')

    # Save to CSV
    merchants.to_csv('entities/merchants.csv', index=False)
except KeyError as e:
    print(f"Error extracting Merchants: {e}")
