# Reporte Meteorológico inspirado en el personaje Chuck Norris

Este proyecto consiste en una aplicación interactiva desarrollada en Python y Streamlit, que aunque aún no llegamos a esa parte del curso, se me hizo correcto experimentar
la experiencia de usar los gráficos de este, para representar mi primera incursión en los dashboards interactivos.

Este programa realiza los siguientes pasos de forma más o menos secuencial:

carga e importa librerías externas
carga librería propia consejo.py (usa librería random) selección aleatoria mediante condicional if
define variables globales para debuggear (correción de errores)
decodifica en texto plano las imágenes para poder trabajarlas en *.CSS
define visualizaciones CSS, uso de clases
presenta visualización de transionado de 2 imágenes mediante niveles de transparencia
consulta un *.csv básico para visualizar un chiste elegido al azar
realiza consulta JSON mediante método GET (obtener) envía parámetros de consulta a saber: latitud, longitud y altitud app de Puerto Montt
carga mensaje de estado consulta, espera 5 segundos con timeup, si no hay respuesta favorable, carga un JSON genérico.
convierte el JSON en un arreglo (parsea)
consulta cada arreglos y anidados a saber datos admosféricos actuales: humedad relativa, temperatura, presión relativa del aire, sensación térmica.
muestra gráficos gauges (los que parecen un transportador) segmentos de colores definidos como una escala de colores (verdes, azules y rojos) mediante *.CSS y RGB (rojo, verde y azul)
muestra imagen de Chuck Norris *.webp con el consejo del día desde librería propia consejo.py de forma aleatoria mediante librería random
muestra gráfico tipo radar o eje de coordenadas circular con dirección del viento.
muestra el JSON en un expander, para dar contexto al desarrollador.

¿Por qué es necesario hacer esto?

Para poder asimilar conocimientos nuevos adquiridos de librerías, consultas APIs, estados, manejo de variables.

¿Dónde extraigo los datos?

La aplicación combina datos climáticos obtenidos desde una API meteorológica "https://api.open-meteo.com/v1/forecast".

¿Por qué Chuck Norris?

Sirve como ejemplo de uso divertido y didáctico. Es un personaje muy conocido a nivel mundial. Es la explicación cómica a funciones absurdamente complejas.
