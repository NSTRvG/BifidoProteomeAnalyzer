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
________________________________________________________________________________________________________________________________________________
Los datos analizados en este programa fueron extraídos de UniProt, una de las bases de datos más completas y confiables para información sobre proteínas. En particular, se seleccionaron datos relacionados con proteínas de diferentes especies del género Bifidobacterium, conocidas por su importancia en la microbiota intestinal y su contribución a la salud humana, especialmente en recién nacidos y bebés. Esta información incluye detalles como los nombres de las proteínas, genes asociados, longitudes en aminoácidos, masas moleculares en Daltons y palabras clave funcionales. El análisis de estos datos busca identificar patrones y características clave que podrían estar vinculadas a la función biológica de estas proteínas en el contexto del entorno intestinal y su posible relación con la nutrición y el metabolismo en etapas tempranas de la vida.
Los datos exeden los 25mb por lo tanto para obtener datos puede realizar los siguientes pasos.
Paso 1: Acceder a UniProt
1.	Ve al sitio web de UniProt: https://www.uniprot.org.

Paso 2: Filtrar por Bifidobacterium

1.	En la barra de búsqueda principal, escribe Bifidobacterium y presiona Enter.
2.	En la página de resultados, utiliza los filtros en el panel izquierdo:
o	Organism: Selecciona "Bifidobacterium" (puede incluir varias especies).
o	Opcional: Aplica otros filtros si deseas datos más específicos, como el tipo de revisión (Reviewed/Unreviewed).
Paso 3: Seleccionar las columnas necesarias

1.	Haz clic en el botón Columns ubicado en la parte superior derecha de la tabla de resultados.
2.	En el menú desplegable, selecciona las columnas relevantes. Asegúrate de incluir:
o	Entry Name (Nombre de entrada)
o	Entry (ID único de entrada)
o	Protein names (Nombres de las proteínas)
o	Gene Names (Nombres de los genes)
o	Length (Longitud de las proteínas en aminoácidos)
o	Mass (Masa molecular en Daltons)
o	Keywords (Palabras clave funcionales)
Paso 4: Descargar el archivo

1.	Una vez configuradas las columnas, haz clic en el botón Download.
2.	Selecciona el formato TSV para la descarga.
3.	Dependiendo de la cantidad de datos, UniProt generará un archivo que puede ser grande. Descarga y guarda el archivo en tu computadora.
