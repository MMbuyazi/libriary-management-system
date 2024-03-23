import pandas as pd
import matplotlib.pyplot as plt


file_path = "C:\Users\cash\DevelopmentProject\Task3\motor_data11-14lats.csv"

insurance_df = pd.read_csv(file_path)


plt.figure(figsize=(8, 6))
plt.scatter(insurance_df['carring_capacity'], insurance_df['effective_yr'], alpha=0.5)
plt.xlabel('Carring Capacity')
plt.ylabel('Effective Year')
plt.title('Carring Capacity vs. Effective Year')
plt.grid(True)
plt.show()
