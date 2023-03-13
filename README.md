Shark-attack-project
Data wrangling - Data Visualization

Realizado por Ubaldo Hervás y Laura Martín / Diciembre-22

1. Introducción

¿Qué oportunidades hay en el mundo de los seguros para ataques de tiburón? ¿Se pueden crear seguros específicos en función de edad, países, género o actividad? ¿Qué perfiles son más proclives a sufrir un ataque de tiburón? ¿Cómo podemos usar Data Wrangling y Data Visualization para responder a estas preguntas?
Para este caso se ha utilizado un archivo CSV que recoge más de 25.000 casos de ataque de tiburón registrados desde mediados del siglo XIX y en el que se puede extraer información de valor como, por ejemplo, si el ataque ha sido fatal o no, el tipo de actividad que se realiza durante el ataque, si era provocado o no, país donde sucedió el ataque, entre otros.
Para poner foco en el proceso de limpieza y visualización de datos, se decide simular un caso ficticio, en el que una agencia de viajes quiere ofrecer seguros específicos a aquellos clientes que quieran realizar actividades con riesgo de recibir un ataque de tiburón. Para ello, contrata a una consultora de data analytics para hallar oportunidades en este nicho.

2. Objetivo y pasos del proyectos
El objetivo principal es extraer insights y oportunidades para el desarrollo de servicios de seguros de viajes para nuestro cliente. Para ello se inicia un proceso de data wrangling y data visualization.

2.1. Definir preguntas de investigación

¿Qué países tienen más ataques?
¿Qué regiones tienen más ataques?
Los individuos que han sufrido ataques, ¿qué características demográficas tenían?
¿Qué actividad estaban realizando aquellos que han sufrido un ataque de tiburón?
¿Qué meses del año son las más proclives a tener ataques de tiburón?
Tipos de daños causados por ataque de tiburón

2.2 Data Wrangling

En este proceso se seleccionaron las columnas con las que trabajar y se eliminaron las que no contribuían a cumplir nuestro objetivo objetivo principal, además de seguir todo el proceso estándar de Data Wrangling: Tratamiento de nulos, outliers, registros duplicados, formateo, agrupación y organización de los datos. Notebook: shark_attack_project.ipynb.
También se realizaron funciones para trabajar de forma más eficiente algunos procesos repetitivos de limpieza de datos (shark_attack_functions.py)

2.3. Data Visualization

Una vez se finaliza el proceso de data wrangling se procede al proceso de visualización de datos para obtener insights y oportunidades. Para esto, hemos utilizado la librería seaborn.

3. Tecnología utilizada

Lenguaje de programación
- Python

Librerías
- Numpy
- Pandas
- Seaborn
- Matplotlib
