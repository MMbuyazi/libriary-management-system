import pandas as pd
import matplotlib.pyplot as plt


file_path =pd.read_csv ("C:\\Users\\cash\\libriary-management-system\\DevelopmentProject\\motor_data11-14lats.csv")
print(file_path.head(10))
print(file_path[file_path['SEATS_NUM']>40][['MAKE','USAGE']])

file_path['EFFECTIVE_YR'] = pd.to_numeric(file_path['EFFECTIVE_YR'], errors='coerce')


plt.plot(file_path['CARRYING_CAPACITY'], file_path['EFFECTIVE_YR'])
plt.xlabel('CARRYING CAPACITY')
plt.ylabel('EFFECTIVE YEAR')
plt.title('Carring Capacity vs Effective Year')
plt.show()

