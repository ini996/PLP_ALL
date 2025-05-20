import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

#Load the CSV file
df = pd.read_csv("sales.csv")

#calculate total revenue
total_revenue = df["Revenue ($)"].sum()

#best selling product
best_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()
best_qty = df.groupby("Product")["Quantity Sold"].sum().max()

#Highest sales day
top_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

#Create a summary dataframe
summary_df = pd.DataFrame({"Metric":["Total Revenue", "Best-selling Product", "Units Sold", "Highest Sales Day"],
                            "Value": [f"${total_revenue}", best_product, best_qty, top_day]

                            })


#Save summary to Excel
summary_df.to_excel("sales_summary.xlsx", index= False)

#Bonus Plot sales trend and save it
df.groupby ("Date")["Revenue ($)"].sum().plot(kind="line",marker="o", title="Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.savefig("sales_trend.xlsx")


print ("Libraries")
