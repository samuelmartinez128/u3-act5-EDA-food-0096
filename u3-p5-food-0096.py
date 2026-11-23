import pandas as pd
import matplotlib.pyplot as plt
## Samuel Martinez NC 0096
# 4. Leer el archivo CSV
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV, comida india 0096 ---")
print(df_food_india)
print("\n--- Mostrar Nombre comida + ingredientes, comida india 0096 ---")
recipes = df_food_india[['name', 'ingredients']]
print(recipes)
print("\n--- Tiempo de cocinado mostrandr 10 registros con head, comida india 0096 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)