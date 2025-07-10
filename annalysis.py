import os
import pandas as pd
import matplotlib.pyplot as plt

# خواندن داده‌ها
df = pd.read_csv("data/salaries.csv")

# ایجاد پوشه plots اگر وجود نداشته باشد
os.makedirs("plots", exist_ok=True)

# محاسبه میانگین حقوق
avg_salaries = df.pivot_table(values="Avg Salary (USD)", index="Country", columns="Job")

# نمودار مقایسه حقوق
avg_salaries.plot(kind="bar", figsize=(12, 6), colormap="viridis")
plt.title("Average Salaries by Job and Country (USD)", fontsize=14)
plt.ylabel("Salary (USD)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# ذخیره نمودار
plt.savefig("plots/salary_comparison.png")
plt.show()