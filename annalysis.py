import os
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/salaries.csv")


os.makedirs("plots", exist_ok=True)


avg_salaries = df.pivot_table(values="Avg Salary (USD)", index="Country", columns="Job")


avg_salaries.plot(kind="bar", figsize=(12, 6), colormap="viridis")
plt.title("Average Salaries by Job and Country (USD)", fontsize=14)
plt.ylabel("Salary (USD)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig("plots/salary_comparison.png")
plt.show()
