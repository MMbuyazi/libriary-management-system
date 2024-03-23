import pandas as pd


file_path = "C:\Users\cash\DevelopmentProject\Task3\motor_data11-14lats.csv"

insurance_df = pd.read_csv(file_path)

print("Column Names:")
print(insurance_df.columns)
print("\nFirst 10 Records:")
print(insurance_df.head(10))

filtered_records = insurance_df[(insurance_df['sets_num'] > 40)]
print("\nRecords for make and usage with sets_num > 40:")
print(filtered_records[['make', 'usage']])





