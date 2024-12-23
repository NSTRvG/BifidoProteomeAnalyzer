# BifidoProteomeAnalyzer
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
7. Visualiza las palabras clave del 5° al 10° lugar en frecuencia mediante otro gráfico de barras.

Requisitos:
- El archivo TSV debe estar en la ruta especificada en la variable `file_path`.
- Las librerías necesarias incluyen pandas, seaborn y matplotlib.

Salidas:
- Histogramas de la longitud y masa de las proteínas.
- Gráfico de dispersión de la relación entre longitud y masa.
- Gráficos de barras para las proteínas y palabras clave más comunes.
