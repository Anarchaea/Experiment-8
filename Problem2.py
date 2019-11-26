import pandas as pd
cars=pd.read_csv('cars.csv')
carsht=cars.head().append(cars.tail())
a=carsht.iloc[:,0:11:2]
b=cars[cars['Model']=='Mazda RX4']
c=cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
d=cars.loc[[1,28,18],['Model','cyl','gear']]
print('A\n')
print(a,'\n')
print('B\n')
print(b,'\n')
print('C\n')
print(c,'\n')
print('D\n')
print(d)