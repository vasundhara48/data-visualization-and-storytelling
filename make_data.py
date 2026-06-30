import pandas as pd
import numpy as np

np.random.seed(42)

regions = ["West", "East", "Central", "South"]
states = {
    "West": ["California", "Washington", "Oregon", "Arizona"],
    "East": ["New York", "Pennsylvania", "Massachusetts", "New Jersey"],
    "Central": ["Texas", "Illinois", "Michigan", "Ohio"],
    "South": ["Florida", "Georgia", "North Carolina", "Tennessee"],
}
categories = {
    "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Art"],
    "Technology": ["Phones", "Machines", "Accessories", "Copiers"],
}
segments = ["Consumer", "Corporate", "Home Office"]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]

n = 1500
rows = []
dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")

for i in range(n):
    region = np.random.choice(regions, p=[0.32, 0.28, 0.22, 0.18])
    state = np.random.choice(states[region])
    category = np.random.choice(list(categories.keys()), p=[0.22, 0.45, 0.33])
    sub_category = np.random.choice(categories[category])
    segment = np.random.choice(segments, p=[0.5, 0.3, 0.2])
    ship_mode = np.random.choice(ship_modes, p=[0.6, 0.2, 0.15, 0.05])
    order_date = np.random.choice(dates)

    base_price = {"Furniture": 250, "Office Supplies": 35, "Technology": 400}[category]
    quantity = np.random.randint(1, 8)
    sales = round(base_price * quantity * np.random.uniform(0.6, 1.6), 2)

    discount = round(np.random.choice([0, 0.1, 0.15, 0.2, 0.3, 0.45],
                                       p=[0.35, 0.25, 0.15, 0.13, 0.08, 0.04]), 2)

    margin = np.random.uniform(0.05, 0.35)
    if category == "Furniture" and discount >= 0.3:
        margin = np.random.uniform(-0.25, -0.02)
    elif discount >= 0.4:
        margin = np.random.uniform(-0.15, 0.02)

    profit = round(sales * margin, 2)

    rows.append([
        f"ORD-{1000+i}", order_date.astype("datetime64[D]").astype(str),
        region, state, segment, category, sub_category,
        ship_mode, quantity, sales, discount, profit
    ])

df = pd.DataFrame(rows, columns=[
    "Order_ID", "Order_Date", "Region", "State", "Segment", "Category",
    "Sub_Category", "Ship_Mode", "Quantity", "Sales", "Discount", "Profit"
])

df.to_csv("/home/claude/task2_submission/data/superstore_sample.csv", index=False)
print(df.shape)
print(df.head())
