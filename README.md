#🌦️ Reporte Meteorológico inspirado en Chuck Norris

Aplicación interactiva desarrollada en Python y Streamlit que consulta datos meteorológicos en tiempo real y los presenta mediante dashboards visuales. Como elemento distintivo, incorpora frases humorísticas inspiradas en el personaje Chuck Norris para entregar consejos y observaciones climáticas de forma entretenida.

Este proyecto representa una primera aproximación al desarrollo de dashboards interactivos y al consumo de APIs externas desde Python.

---

🚀 Características principales

- Consulta datos meteorológicos en tiempo real mediante API.
- Visualización interactiva utilizando Streamlit.
- Indicadores tipo Gauge para variables atmosféricas.
- Gráfico radar para dirección del viento.
- Integración de imágenes mediante CSS y Base64.
- Sistema de consejos aleatorios inspirado en Chuck Norris.
- Mecanismo de respaldo ante fallos de conexión.
- Herramientas de depuración para desarrollo.
- Visualización del JSON recibido para análisis y aprendizaje.

---

#⚙️ Funcionamiento general

La aplicación realiza los siguientes procesos:

1. Inicialización

- Importación de librerías externas.
- Carga de módulos propios.
- Definición de variables globales de depuración.

2. Recursos visuales

- Conversión de imágenes a Base64.
- Aplicación de estilos CSS personalizados.
- Efectos de transición entre imágenes mediante niveles de transparencia.

3. Contenido dinámico

- Lectura de un archivo CSV con chistes aleatorios.
- Selección aleatoria de consejos mediante la librería "random".

4. Consulta meteorológica

Se realiza una petición HTTP GET a una API meteorológica enviando parámetros como:

- Latitud
- Longitud
- Altitud

correspondientes a la ciudad de Puerto Montt.

5. Manejo de errores

- Se muestra un mensaje de estado durante la consulta.
- Se establece un tiempo máximo de espera.
- Si la consulta falla, se carga un JSON genérico como respaldo.

6. Procesamiento de datos

- Conversión del JSON recibido a estructuras de Python.

- Extracción de datos meteorológicos actuales:
  
  - Temperatura
  - Humedad relativa
  - Presión atmosférica
  - Sensación térmica

7. Visualización

La información se presenta mediante:

- Indicadores Gauge.
- Escalas de colores RGB.
- Gráficos radar para dirección del viento.
- Imagen de Chuck Norris acompañada por un consejo aleatorio.

8. Información para desarrolladores

El JSON completo recibido desde la API puede visualizarse dentro de un componente expandible para facilitar el análisis y la depuración.

---

#🎯 Objetivo del proyecto

Este proyecto fue desarrollado con fines educativos para practicar:

- Consumo de APIs.
- Manipulación de datos JSON.
- Creación de dashboards interactivos.
- Uso de librerías externas.
- Personalización visual mediante CSS.
- Manejo de errores y estados de aplicación.

---

🌎 Fuente de datos

Los datos meteorológicos son obtenidos desde la API de Open-Meteo:

https://api.open-meteo.com/v1/forecast

---

😎 ¿Por qué Chuck Norris?

Chuck Norris se utiliza como elemento humorístico para acompañar la información meteorológica.

Además de aportar personalidad a la aplicación, sirve como ejemplo práctico de generación de contenido dinámico y aleatorio dentro de una interfaz interactiva.

---

📂 Archivo principal

reporte.py

---

▶️ Ejecución

Desde la carpeta principal del proyecto ejecutar:

python -m streamlit run reporte.py

---

📦 Dependencias

import streamlit as st
import plotly.graph_objects as go
import requests
import base64
import random
import json

Descripción de librerías

Librería| Función
Streamlit| Desarrollo de aplicaciones web interactivas
Plotly| Creación de gráficos y dashboards
Requests| Consulta de APIs mediante HTTP
Base64| Conversión de imágenes binarias a texto
Random| Generación de elementos aleatorios
JSON| Manipulación de estructuras JSON

---

📚 Tecnologías utilizadas

- Python
- Streamlit
- Plotly
- CSS
- JSON
- REST API
- Open-Meteo

---
