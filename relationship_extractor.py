import pandas as pd

# Load the dataset with low_memory=False to handle large files
df = pd.read_csv('amazon_sales_report.csv', low_memory=False)

# Rename columns: remove spaces and convert to lowercase
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Relationship 1: places.csv - Customer PLACES Order
try:
    places = df[['ship-postal-code', 'order_id']].copy()
    places = places.drop_duplicates().reset_index(drop=True)

    # Save to CSV
    places.to_csv('relationships/places.csv', index=False)
except KeyError as e:
    print(f"Error extracting places relationship: {e}")

# Relationship 2: contains.csv - Order CONTAINS Product
try:
    contains = df[['order_id', 'sku']].copy()
    contains = contains.drop_duplicates().reset_index(drop=True)

    # Save to CSV
    contains.to_csv('relationships/contains.csv', index=False)
except KeyError as e:
    print(f"Error extracting contains relationship: {e}")


# Relationship 3: fulfills.csv - Merchant FULFILLS Order
try:
    fulfills = df[['fulfilled-by', 'order_id']].copy()
    fulfills = fulfills.drop_duplicates().reset_index(drop=True)

    # Save to CSV
    fulfills.to_csv('relationships/fulfills.csv', index=False)
except KeyError as e:
    print(f"Error extracting fulfills relationship: {e}")
