import pandas as pd

#creo un dataframe usando pandas del csv
train = pd.read_csv("Ej2/CSV/train.csv")
#uso la funcion dropna() para eliminar los valores nulos
train = train.dropna()
#creo otro csv sin valores nulos
train.to_csv('Ej2/CSV/train_limpio.csv', index=False)