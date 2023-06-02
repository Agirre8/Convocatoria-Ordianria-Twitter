import pandas as pd

#APARTADO 2.B

#creo un dataframe usando pandas del csv
train = pd.read_csv("Ej2/CSV/train.csv")
#uso la funcion dropna() para eliminar los valores nulos
train = train.dropna()
#creo otro csv sin valores nulos
train.to_csv("Ej2/CSV/train_limpio.csv", index=False)



train = pd.read_csv("Ej2/CSV/train_limpio.csv")
test = pd.read_csv("Ej2/CSV/test.csv")
ss = pd.read_csv("Ej2/CSV/sample_submission.csv")