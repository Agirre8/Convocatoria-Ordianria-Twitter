import pandas as pd
import plotly.io as pio
import plotly.graph_objs as go

#APARTADO 1.B
def random_colours(number_of_colors):

    colors = []
    for i in range(number_of_colors):
        colors.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    return colors

#APARTADO 2.A
train = pd.read_csv("Ej2/CSV/train_limpio.csv")
test = pd.read_csv("Ej2/CSV/test.csv")
ss = pd.read_csv("Ej2/CSV/sample_submission.csv")



#APARTADO 3.A


# Explorar la estructura y contenido del conjunto de datos
print(train.head())
print(train.info())


sentiment_counts = train['sentiment'].value_counts()
print(sentiment_counts)

# Crear la figura del gráfico de embudo
fig = go.Figure()

fig.add_trace(go.Funnel(
    y=sentiment_counts.index.tolist(),
    x=sentiment_counts.values.tolist(),
    textposition='inside',
    textinfo='value+percent previous'))

# Guardar la imagen como un archivo PNG
pio.write_image(fig, 'Ej2/Graficas/grafico_embudo.png')


#APARTADO 3.B
# Función para calcular la similitud de Jaccard
def jaccard(str1, str2):
    a = set(str1.lower().split())
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

results_jaccard=[]

for ind,row in train.iterrows():
    sentence1 = row.text
    sentence2 = row.selected_text

    jaccard_score = jaccard(sentence1,sentence2)
    results_jaccard.append([sentence1,sentence2,jaccard_score])

jaccard_df = pd.DataFrame(results_jaccard,columns=["text","selected_text","jaccard_score"])
train = train.merge(jaccard_df,how='outer')


train['Num_words_ST'] = train['selected_text'].apply(lambda x:len(str(x).split())) # Número de palabras en Selected_text
train['Num_words_text'] = train['text'].apply(lambda x:len(str(x).split())) # Número de palabras en texto principal
train['difference_in_words'] = train['Num_words_text'] - train['Num_words_ST'] # Diferencia en número de palabras entre texto y Selected_text

train.head()


#librerias para plotear las graficas
import matplotlib.pyplot as plt
import seaborn as sns

#diferencia en el número de palabras
plt.figure(figsize=(10, 6))
sns.histplot(data=train, x='difference_in_words', hue='sentiment', kde=True)
plt.title("Diferencia en el número de palabras entre Selected_text y texto")
plt.xlabel("Diferencia en el número de palabras")
plt.ylabel("Frecuencia")
plt.savefig('Ej2/Graficas/diferencia_palabras.png')
plt.close()

#similitud de Jaccard
plt.figure(figsize=(10, 6))
sns.histplot(data=train, x='jaccard_score', hue='sentiment', kde=True)
plt.title("Similitud de Jaccard entre texto y Selected_text")
plt.xlabel("Similitud de Jaccard")
plt.ylabel("Frecuencia")
plt.savefig('Ej2/Graficas/similitud_jaccard.png')
plt.close()


#APARTADO 3.C

# Calcular la curtosis de cada sentimiento
kurtosis = train.groupby('sentiment')['difference_in_words'].apply(lambda x: x.kurtosis())

# Visualizar la curtosis
plt.figure(figsize=(10, 6))
sns.barplot(x=kurtosis.index, y=kurtosis.values)
plt.title("Curtosis de la diferencia en el número de palabras por sentimiento")
plt.xlabel("Sentimiento")
plt.ylabel("Curtosis")
plt.savefig('Ej2/Graficas/curtosis.png')
plt.close()

# Calcular la asimetría de cada sentimiento
skewness = train.groupby('sentiment')['difference_in_words'].apply(lambda x: x.skew())

# Visualizar la asimetría
plt.figure(figsize=(10, 6))
sns.barplot(x=skewness.index, y=skewness.values)
plt.title("Asimetría de la diferencia en el número de palabras por sentimiento")
plt.xlabel("Sentimiento")
plt.ylabel("Asimetría")
plt.savefig('Ej2/Graficas/asimetria.png')
plt.close()