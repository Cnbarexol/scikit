import pandas as pd #importamos pandas
import sklearn #biblioteca de aprendizaje automático
import matplotlib.pyplot as plt #Librería especializada en la creación de gráficos
from sklearn.decomposition import PCA #importamos algorimo PCA
from sklearn.decomposition import IncrementalPCA #importamos algorimo PCA
from sklearn.linear_model import LogisticRegression #clasificación y análisis predictivo 
from sklearn.preprocessing import StandardScaler #Normalizar los datos
from sklearn.model_selection import train_test_split #permite hacer una división de un conjunto de datos en dos 
#bloques de entrenamiento y prueba de un modelo
if __name__ == '_main_':
    dt_heart=pd.read_csv('./mineriadataa.csv')
    print(dt_heart.head(5)) #imprimimos los 5 primeros datos
    