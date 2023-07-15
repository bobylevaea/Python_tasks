
import pandas as pd 
  
# Загрузка данных из файла 
df = pd.read_csv('/content/sample_data/california_housing_train.csv') 
df.head(2)

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке 
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
 
mean_house_value = round(df[df['population'] < 501]['median_house_value'].mean(), 2) 
print (f'Средняя стоимость дома: {mean_house_value}')

# mean    206799.95 

  
# Задача 42: Узнать какая максимальная households в зоне минимального значения population 

max_households = df[df['population'] == df['population'].min()]['households'].max()
print(f'Максимальная households: {max_households}')

# max    4.0
