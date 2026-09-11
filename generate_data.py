import os
import numpy as np
import pandas as pd

np.random.seed(42)

os.makedirs("data", exist_ok=True)

# ---------------------------------------------------------
# PRODUCTS
# ---------------------------------------------------------

products = [
    ["P001", "Laptop", "Electronics"],
    ["P002", "Smartphone", "Electronics"],
    ["P003", "Headphones", "Electronics"],
    ["P004", "Monitor", "Electronics"],
    ["P005", "Keyboard", "Electronics"],
    ["P006", "T-Shirt", "Apparel"],
    ["P007", "Jeans", "Apparel"],
    ["P008", "Jacket", "Apparel"],
    ["P009", "Sofa", "Home & Living"],
    ["P010", "Dining Table", "Home & Living"],
    ["P011", "Car Seat", "Automotive"],
    ["P012", "Engine Oil", "Automotive"],
    ["P013", "Face Cream", "Health & Beauty"],
    ["P014", "Shampoo", "Health & Beauty"],
    ["P015", "Other Product", "Others"],
]

products_df = pd.DataFrame(
    products,
    columns=["Product_ID", "Product", "Category"]
)

products_df.to_csv("data/products.csv", index=False)

# ---------------------------------------------------------
# SUPPLIERS
# ---------------------------------------------------------

supplier_names = [
    "GlobalTech Solutions",
    "BrightMart Supplies",
    "SupplyMax Inc.",
    "NextGen Traders",
    "Prime Logistics",
    "Alpha Wholesale",
    "Metro Supply Co.",
    "United Distributors",
]

suppliers = []

for i, name in enumerate(supplier_names, 1):
    suppliers.append([
        f"SUP{i:03d}",
        name,
        np.random.randint(350, 1300),
        np.random.randint(450000, 2000000)
    ])

suppliers_df = pd.DataFrame(
    suppliers,
    columns=[
        "Supplier_ID",
        "Supplier_Name",
        "Orders",
        "Total_Value"
    ]
)

suppliers_df.to_csv("data/suppliers.csv", index=False)

# ---------------------------------------------------------
# INVENTORY
# ---------------------------------------------------------

months = pd.date_range("2025-01-01", "2025-12-01", freq="MS")

inventory_rows = []

base_inventory = 5_000_000

for i, month in enumerate(months):

    total_inventory = base_inventory + i * 300000 + np.random.randint(
        -180000, 180000
    )

    raw_materials = total_inventory * 0.48
    finished_goods = total_inventory * 0.36

    inventory_rows.append([
        month,
        total_inventory,
        raw_materials,
        finished_goods
    ])

inventory_df = pd.DataFrame(
    inventory_rows,
    columns=[
        "Month",
        "Total_Inventory",
        "Raw_Materials",
        "Finished_Goods"
    ]
)

inventory_df.to_csv("data/inventory.csv", index=False)

# ---------------------------------------------------------
# ORDERS
# ---------------------------------------------------------

regions = ["North", "South", "East", "West"]

orders = []

for i in range(4892):

    order_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=np.random.randint(0, 365)
    )

    region = np.random.choice(regions, p=[0.29, 0.26, 0.20, 0.25])

    product = products_df.sample(1).iloc[0]

    orders.append([
        f"ORD{i+778000}",
        order_date,
        region,
        product["Product_ID"],
        product["Product"],
        product["Category"],
        np.random.randint(100, 2500),
        np.random.randint(1, 10)
    ])

orders_df = pd.DataFrame(
    orders,
    columns=[
        "Order_ID",
        "Order_Date",
        "Region",
        "Product_ID",
        "Product",
        "Category",
        "Order_Value",
        "Quantity"
    ]
)

orders_df.to_csv("data/orders.csv", index=False)

# ---------------------------------------------------------
# SHIPMENTS
# ---------------------------------------------------------

shipment_rows = []

for i in range(4721):

    ship_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=np.random.randint(0, 365)
    )

    delivery_days = np.random.choice(
        [2, 3, 4, 5, 6, 7, 8],
        p=[0.12, 0.20, 0.25, 0.20, 0.10, 0.08, 0.05]
    )

    delivery_date = ship_date + pd.Timedelta(days=int(delivery_days))

    status = np.random.choice(
        ["Delivered", "In Transit", "Delayed"],
        p=[0.90, 0.06, 0.04]
    )

    region = np.random.choice(regions)

    product = products_df.sample(1).iloc[0]

    shipment_rows.append([
        f"SHP{120000+i}",
        f"ORD{778000+i}",
        product["Product"],
        region,
        status,
        ship_date,
        delivery_date
    ])

shipments_df = pd.DataFrame(
    shipment_rows,
    columns=[
        "Shipment_ID",
        "Order_ID",
        "Product",
        "Destination",
        "Status",
        "Ship_Date",
        "Delivery_Date"
    ]
)

shipments_df.to_csv("data/shipments.csv", index=False)

# ---------------------------------------------------------
# CUSTOMERS
# ---------------------------------------------------------

customers = []

for i in range(1000):

    customers.append([
        f"CUS{i+1:04d}",
        f"Customer {i+1}",
        np.random.choice(regions),
        np.random.choice(["Retail", "Wholesale", "Enterprise"])
    ])

customers_df = pd.DataFrame(
    customers,
    columns=[
        "Customer_ID",
        "Customer_Name",
        "Region",
        "Customer_Type"
    ]
)

customers_df.to_csv("data/customers.csv", index=False)

print("====================================")
print("Supply Chain 365 data created!")
print("====================================")
print("Files created inside data/")
print("inventory.csv")
print("orders.csv")
print("shipments.csv")
print("suppliers.csv")
print("products.csv")
print("customers.csv")