import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.rcParams.update({
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

df = pd.read_csv("/home/claude/task2_submission/data/superstore_sample.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M").dt.to_timestamp()

OUT = "/home/claude/task2_submission/charts/"

# 1. Sales trend over time (line chart)
monthly = df.groupby("Month")["Sales"].sum()
fig, ax = plt.subplots(figsize=(9, 4.2))
ax.plot(monthly.index, monthly.values, color="#2A6F97", linewidth=2, marker="o", markersize=3)
ax.set_title("Monthly Sales Trend (2023-2024)")
ax.set_ylabel("Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
ax.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
fig.savefig(OUT + "01_sales_trend.png", dpi=150)
plt.close(fig)

# 2. Sales by category (bar chart)
cat_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.barh(cat_sales.index, cat_sales.values, color="#2A6F97")
ax.set_title("Total Sales by Category")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for b in bars:
    ax.text(b.get_width() + 5000, b.get_y() + b.get_height()/2,
            f"${b.get_width():,.0f}", va="center", fontsize=9)
fig.tight_layout()
fig.savefig(OUT + "02_sales_by_category.png", dpi=150)
plt.close(fig)

# 3. Profit by sub-category (diverging bar)
sub = df.groupby("Sub_Category")["Profit"].sum().sort_values()
colors = ["#C1121F" if v < 0 else "#2A9D8F" for v in sub.values]
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(sub.index, sub.values, color=colors)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_title("Profit by Sub-Category (Red = Loss-Making)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
fig.tight_layout()
fig.savefig(OUT + "03_profit_by_subcategory.png", dpi=150)
plt.close(fig)

# 4. Sales by region (bar)
reg_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(reg_sales.index, reg_sales.values, color="#3D5A80")
ax.set_title("Sales by Region")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for b in bars:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 5000,
            f"${b.get_height():,.0f}", ha="center", fontsize=9)
fig.tight_layout()
fig.savefig(OUT + "04_sales_by_region.png", dpi=150)
plt.close(fig)

# 5. Segment share (pie chart)
seg_sales = df.groupby("Segment")["Sales"].sum()
fig, ax = plt.subplots(figsize=(6, 5))
ax.pie(seg_sales.values, labels=seg_sales.index, autopct="%1.0f%%",
       colors=["#2A6F97", "#61A0AF", "#A9D6E5"], startangle=90,
       wedgeprops={"edgecolor": "white", "linewidth": 1})
ax.set_title("Share of Sales by Customer Segment")
fig.tight_layout()
fig.savefig(OUT + "05_segment_share.png", dpi=150)
plt.close(fig)

# 6. Discount vs Profit scatter
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.scatter(df["Discount"], df["Profit"], alpha=0.35, s=18, color="#2A6F97")
ax.axhline(0, color="#C1121F", linewidth=1, linestyle="--")
ax.set_title("Discount vs Profit (Higher Discounts Erode Margin)")
ax.set_xlabel("Discount Rate")
ax.set_ylabel("Profit ($)")
fig.tight_layout()
fig.savefig(OUT + "06_discount_vs_profit.png", dpi=150)
plt.close(fig)

print("charts done")
