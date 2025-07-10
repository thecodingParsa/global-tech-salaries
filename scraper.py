import pandas as pd
import numpy as np
import os

# لیست کشورها و حرفه‌ها
countries = ["USA", "Germany", "India", "Iran", "Japan"]
jobs = ["Software Developer", "Cybersecurity Engineer", "Data Analyst"]

# ساخت داده‌های تصادفی
data = []
for country in countries:
    for job in jobs:
        base_salary = {
            "USA": 90000,
            "Germany": 70000,
            "India": 30000,
            "Iran": 20000,
            "Japan": 80000
        }.get(country, 50000)
        
        # تغییرات تصادفی بر اساس حرفه
        job_factor = {
            "Software Developer": 1.0,
            "Cybersecurity Engineer": 1.2,
            "Data Analyst": 0.9
        }.get(job, 1.0)
        
        avg = int(base_salary * job_factor * np.random.uniform(0.9, 1.1))
        min_salary = int(avg * 0.8)
        max_salary = int(avg * 1.2)
        
        data.append({
            "Job": job,
            "Country": country,
            "Avg Salary (USD)": avg,
            "Min Salary (USD)": min_salary,
            "Max Salary (USD)": max_salary,
            "Source": "Generated"
        })

# ذخیره در CSV
os.makedirs("data", exist_ok=True)
df = pd.DataFrame(data)
df.to_csv("data/salaries.csv", index=False)
print("New data generated in data/salaries.csv")