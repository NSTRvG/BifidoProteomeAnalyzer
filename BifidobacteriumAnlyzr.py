"""
Este programa analiza un archivo TSV que contiene información sobre proteínas de Bifidobacterium.
Utilizando pandas, seaborn y matplotlib, realiza varias operaciones de análisis y visualización
de datos relacionados con las proteínas y sus características.

Funciones principales:
1. Carga un archivo TSV con columnas relevantes como nombres de entrada, proteínas, genes, longitud,
   masa y palabras clave.
2. Maneja valores nulos en la columna 'Keywords', reemplazándolos con cadenas vacías.
3. Analiza y cuenta las palabras clave separadas por ';', organizándolas en un DataFrame.
4. Genera histogramas para la distribución de longitud y masa de las proteínas.
5. Crea un gráfico de dispersión para visualizar la relación entre longitud y masa.
6. Identifica las 10 proteínas más frecuentes y visualiza su distribución en un gráfico de barras.
7. Visualiza las palabras clave del 5° al 14° lugar en frecuencia mediante gráfico de barras.

Requisitos:
- El archivo TSV debe estar en la ruta especificada en la variable `file_path`.
- Las librerías necesarias incluyen pandas, seaborn y matplotlib.

Salidas:
- Histogramas de la longitud y masa de las proteínas.
- Gráfico de dispersión de la relación entre longitud y masa.
- Gráficos de barras para las proteínas y palabras clave más comunes.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo TSV
file_path = "uniprotkb_Bifidobacterium_2024_12_20.tsv"  # Cambia esto por la ruta de tu archivo
data = pd.read_csv(file_path, sep='\t')  # Lee el archivo TSV y lo almacena en un DataFrame

# Filtrar las columnas necesarias
filtered_data = data[['Entry Name', 'Entry', 'Protein names', 'Gene Names', 'Length', 'Mass', 'Keywords']]

# Manejar valores nulos en la columna 'Keywords' usando loc
filtered_data.loc[:, 'Keywords'] = filtered_data['Keywords'].fillna('')  # Rellena valores nulos con cadenas vacías

# Crear un nuevo DataFrame para contar las ocurrencias de cada palabra clave
keyword_counts = (
    filtered_data['Keywords']
    .str.split(';', expand=True) # Separar las palabras clave por ';'
    .stack()                     # Reorganizar en una serie de palabras clave
    .value_counts()              # Contar la frecuencia de cada palabra clave
    .reset_index()               # Convertir a DataFrame
)
keyword_counts.columns = ['Keyword', 'Count']  # Renombrar columnas
keyword_counts = keyword_counts.sort_values('Count', ascending=False)  # Ordenar las palabras clave por frecuencia

# Histogramas
plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_data, x='Length', kde=True, color='blue', bins=30)  # Histograma de longitud
plt.title("Distribución de la longitud de las proteínas")
plt.xlabel("Longitud (aminoácidos)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_data, x='Mass', kde=True, color='green', bins=30)  # Histograma de masa
plt.title("Distribución de la masa de las proteínas")
plt.xlabel("Masa (Daltons)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# Gráfico de dispersión entre longitud y masa
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_data, x='Length', y='Mass', color='orange')  # Relación longitud vs masa
plt.title("Relación entre la longitud y la masa de las proteínas")
plt.xlabel("Longitud (aminoácidos)")
plt.ylabel("Masa (Daltons)")
plt.tight_layout()
plt.show()

# Contar las proteínas más frecuentes
protein_counts = (
    filtered_data['Protein names']
    .value_counts()
    .head(10)  # Seleccionar las 10 proteínas más frecuentes
    .reset_index()
)
protein_counts.columns = ['Protein Name', 'Count']  # Renombrar columnas

# Gráfico de barras para las proteínas más frecuentes
plt.figure(figsize=(10, 6))
sns.barplot(data=protein_counts, x='Count', y='Protein Name')  # Top 10 proteínas
plt.title("Top 10 Proteínas más frecuentes")
plt.xlabel("Frecuencia")
plt.ylabel("Nombre de la proteína")
plt.tight_layout()
plt.show()

# Seleccionar las keywords entre el 5° y 10° lugar
keywords_3_to_10 = keyword_counts[4:14]  # Filtrar filas de interés

# Crear el gráfico de barras para las keywords seleccionadas
plt.figure(figsize=(10, 6))
sns.barplot(data=keywords_3_to_10, x='Count', y='Keyword')  # Top keywords seleccionadas
plt.title('Palabras Clave del 5° al 14° Lugar')
plt.xlabel('Frecuencia')
plt.ylabel('Palabra Clave')
plt.xticks(rotation=45)  # Rotar etiquetas para mejor visualización
plt.tight_layout()
plt.show()

