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



#APARTADO 3


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


