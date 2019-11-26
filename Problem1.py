import pandas as pd
cars=pd.read_csv('cars.csv')
carspd=cars.head().append(cars.tail())

print(carspd)