# Evaluación Final del Módulo 3 📊

## Análisis de la Actividad de Vuelo, Nivel de Educación y Grupos de Fidelización del Cliente en una Aerolínea Canadiense ✈️

## Introducción 📖

Este proyecto se divide en tres fases principales, cada una de las cuales aborda diferentes aspectos del análisis de datos y pruebas estadísticas. Aquí están los enlaces a cada fase:

- [Fase 1: Exploración Inicial y Limpieza de Datos](https://github.com/Adalab/bda-modulo-3-evaluacion-final-MaPitelli/blob/main/jupyters/phase_1.ipynb)
- [Fase 2: Visualización de Datos](https://github.com/Adalab/bda-modulo-3-evaluacion-final-MaPitelli/blob/main/jupyters/phase_2.ipynb)
- [Fase 3: A/B Testing](https://github.com/Adalab/bda-modulo-3-evaluacion-final-MaPitelli/blob/main/jupyters/phase_3.ipynb)


## Objetivo 🎯

El objetivo de esta evaluación es comprobar la comprensión y habilidades en análisis de datos mediante la realización de un A/B Testing y pruebas estadísticas. Utilizaremos un conjunto de datos de clientes con diferentes niveles educativos y sus reservas de vuelos para determinar si existen diferencias significativas en el número de vuelos reservados entre los diferentes niveles educativos. Además, se evaluará la capacidad para realizar una exploración y limpieza de datos, visualización de datos y el uso de procesos ETL y Pipelines en el contexto de análisis de datos.

---

## Estructura 🏗️

La evaluación consta de tres fases:

1. **Exploración y Limpieza**:
    - Exploración inicial de los datos para identificar posibles problemas como valores nulos o atípicos.
    - Limpieza de datos para asegurar consistencia y corrección, incluyendo eliminación o tratamiento de valores nulos y ajustes de tipos de datos.

2. **Visualización**:
    - Creación de gráficas para analizar la distribución de vuelos reservados por mes, relación entre distancia de vuelos y puntos acumulados, distribución de clientes por provincia o estado, comparación de salario promedio entre niveles educativos, proporción de clientes con diferentes tarjetas de fidelidad, y distribución de clientes por estado civil y género.

3. **Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo**:
    - Preparación de datos filtrando las columnas relevantes.
    - Análisis descriptivo agrupando datos por nivel educativo y calculando estadísticas básicas.
    - Realización de un A/B Testing para determinar si existen diferencias significativas en el número de vuelos reservados entre los diferentes niveles educativos.

---

### Tecnologías Utilizadas 🛠️

En esta evaluación se utilizaron diversas tecnologías y librerías para el análisis y visualización de datos, así como para la ejecución de pruebas estadísticas. A continuación, se detallan las principales tecnologías utilizadas:

#### <img src="images/vsc_logo.png" alt="VS Code Logo" width="30"/>     Visual Studio Code     

[Visual Studio Code](https://code.visualstudio.com/) Editor de código utilizado para escribir y depurar el código en Python.

#### <img src="images/jupyter_logo.png" alt="Jupyter Logo" width="30"/>     Jupyter Notebooks      

[Jupyter Notebooks](https://jupyter.org/) En esta evaluación, se utilizaron archivos Jupyter Notebooks (extensión .ipynb) para la exploración interactiva de datos y la creación de gráficos.


### Librerías de Python 📖

- **Pandas**: Biblioteca de análisis de datos en Python.
- **NumPy**: Biblioteca para computación científica en Python.
- **SciPy**: Biblioteca para matemáticas, ciencias e ingeniería en Python.
- **Seaborn**: Biblioteca de visualización de datos basada en Matplotlib.
- **Matplotlib**: Biblioteca de gráficos en 2D para Python.
- **Scikit-learn**: Biblioteca de aprendizaje automático en Python.
- **itertools**: [itertools](https://docs.python.org/3/library/itertools.html) es un módulo de la biblioteca estándar de Python que ofrece funciones que crean iteradores eficientes. En este proyecto, se utilizó para generar combinaciones.

##### Importación de Módulos Propios 👩🏻‍💻

Durante esta evaluación, también se trabajó con módulos Python personalizados, lo cual facilitó la organización y reutilización del código. Estos módulos se importaron y utilizaron para diversas funciones y análisis específicos. Puedes ver el módulo propio [aquí](https://github.com/Adalab/bda-modulo-3-evaluacion-final-MaPitelli/blob/main/jupyters/src/support.py).


---

## Temas Aprendidos 📚

Durante esta evaluación, se cubrieron varios temas clave relacionados con la manipulación, análisis y visualización de datos, así como la aplicación de pruebas estadísticas. A continuación, se detallan los principales temas aprendidos:

### 1. Exploración y Limpieza de Datos

#### Exploración Inicial

- **Inspección de Datos**: Utilización de funciones de Pandas para obtener información sobre la estructura de los datos, la presencia de valores nulos y estadísticas básicas de las columnas involucradas.
- **Identificación de Problemas**: Detección de valores nulos, atípicos o datos faltantes en las columnas relevantes.

#### Limpieza de Datos

- **Tratamiento de Valores Nulos**: Eliminación o tratamiento de valores nulos en las columnas clave para asegurar que los datos estén completos.
- **Consistencia de Datos**: Verificación de la consistencia y corrección de los datos para garantizar su coherencia.
- **Ajuste de Tipos de Datos**: Realización de ajustes o conversiones necesarias en las columnas (por ejemplo, cambiar tipos de datos) para asegurar la adecuación de los datos para el análisis estadístico.

- **Pandas**:
  - `pd.read_csv()`: Lectura de archivos CSV.
  - `df.dropna()`: Eliminación de valores nulos.
  - `df.groupby()`: Agrupación de datos.
  - `df.describe()`: Cálculo de estadísticas descriptivas.
  - `df.apply(lambda x: ...)`: Aplicación de funciones lambda para transformar datos.

### 2. Visualización de Datos

Se utilizaron diversas técnicas de visualización para responder preguntas específicas y explorar las relaciones entre las variables. 

- **Seaborn**:
  - `sns.histplot()`: Creación de histogramas.
  - `sns.scatterplot()`: Creación de gráficos de dispersión.

- **Matplotlib**:
  - `plt.plot()`: Creación de gráficos de línea.
  - `plt.bar()`: Creación de gráficos de barras.

- **Análisis de Gráficos**: Interpretación de las gráficas para extraer conclusiones y responder preguntas específicas del análisis.

A continuación, se presentan dos ejemplos de gráficos generados durante la evaluación:

#### Distribución de la cantidad de vuelos reservados por mes

![Distribución de la cantidad de vuelos reservados por mes](images/flights_booked_month.png)

#### Relación entre la distancia de los vuelos y los puntos acumulados por segmento de cliente

![Relación entre la distancia de los vuelos y los puntos acumulados por segmento de cliente](images/distance_points.png)

### 3. Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo

#### Preparación de Datos

- **Filtrado de Datos**: Filtrado del conjunto de datos para incluir únicamente las columnas relevantes ('Flights Booked' y 'Education').

#### Análisis Descriptivo

- **Agrupación por Nivel Educativo**: Agrupación de los datos por nivel educativo utilizando la función `groupby` y cálculo de estadísticas descriptivas básicas (como el promedio, la desviación estándar y los percentiles) del número de vuelos reservados para cada grupo.

- **Uso de `apply` y Funciones Lambda**: Utilización de la función `apply` junto con funciones lambda para transformar datos y aplicar funciones personalizadas a los DataFrames. Esto permitió realizar operaciones complejas de manera concisa y eficiente.

### Ejemplo de Transformación de Datos con Funciones Lambda

```python
# Aplicación de una función lambda para categorizar niveles educativos
df_filtered_ab['test_group'] = df_filtered_ab['education'].apply(lambda x: sp.categorize(x, group_a, group_b))
```

#### Pruebas Estadísticas

- **SciPy**:
  - `stats.shapiro()`: Prueba de normalidad de Shapiro-Wilk.
  - `stats.kstest()`: Prueba de Kolmogorov-Smirnov.
  - `stats.mannwhitneyu()`: Prueba de Mann-Whitney U.

- **Prueba de Normalidad**: Realización de pruebas de normalidad utilizando los métodos de Shapiro-Wilk y Kolmogorov-Smirnov para evaluar la distribución de los datos.
- **Prueba de Mann-Whitney U**: Aplicación de la prueba de Mann-Whitney U para comparar las medianas de las métricas entre dos grupos y determinar si existe una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos.


---

Estos temas demuestran un enfoque integral para el análisis de datos, abarcando desde la exploración y limpieza hasta la visualización y análisis estadístico. Esta metodología permite obtener una comprensión detallada de los datos y tomar decisiones basadas en resultados sólidos y bien fundamentados. Para ver más ejemplos de este tipo de análisis y explorar en detalle mi trabajo, te invito a visitar el repositorio del proyecto: ➡️ [Enlace al repositorio](https://github.com/Adalab/bda-modulo-3-evaluacion-final-MaPitelli/tree/main/jupyters)


## Información de Contacto 📞

Para cualquier consulta, no dudes en contactarme:

- **Nombre**: [Maíra Pitelli]
- **Email**: [mairapitelli@hotmail.com]
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/mairapitelli/)

¡Gracias por revisar mi proyecto! 😊