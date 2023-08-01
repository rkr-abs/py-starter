import pandas as pd

dataFrame = pd.read_csv('employee.csv')

print("Data in DataFrame:")
print(dataFrame)

print("\nBasic Statistics:")
print(dataFrame.describe())

print("\nPeople younger than 25:")
young_people = dataFrame[dataFrame['Age'] < 25]
print(young_people)

average_salary = dataFrame['Salary'].mean()
print("\nAverage Salary:", average_salary)

dataFrame['Bonus'] = dataFrame['Salary'] * 0.1
print("\nDataFrame with Bonus column:")
print(dataFrame)
