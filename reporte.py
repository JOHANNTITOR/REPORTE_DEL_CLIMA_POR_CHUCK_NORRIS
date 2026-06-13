#importaciones de librerías: 

# Streamlit (visalización en navegador, webs nativas rápidas, actualiza código y recarga), 

import streamlit as st #carga código py al navegador, webs interactivas, prototipado rápido
import plotly.graph_objects as go #crea gráficos, gauges, visualización, gráficos, dashboards, de todo
import requests #para consultas APIs, consultas en general
import base64 #para incrustar imágenes en CSS, transforma binarios en texto plano
import random #aleatorización
import json

#librería local
from consejo import obtener_respuesta

#globales
primera_vez = True; #Tira un chiste al recargar la página o sea Shift + Ctrl + R. Funciona bien con True
debbugear = False; #True para solo para debbugear. carga estructura JSON por omisión - solo para pruebas sin consultar a la API

#funcion - decode imagenes
def img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

#aquí ocurre la magia
img_sol = img_base64("soleado.jpg")
img_lluvia = img_base64("lluvia.jpg")

#nombre de pestaña, anchor
st.set_page_config(
    page_title="Dashboard Meteorológico",
    layout="wide"
)

if debbugear == True:
    with open("respaldo_clima.json", "r", encoding="utf-8") as archivo:
        weather = json.load(archivo)

#estructura de consulta JSON API open Mateo (libre) consulta de acuerdo a altitud, longitud y latitud de puerto montt
url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-41.47"
    "&longitude=-72.94"
    "&current=temperature_2m,"
    "relative_humidity_2m,"
    "apparent_temperature,"
    "precipitation,"
    "cloud_cover,"
    "pressure_msl,"
    "wind_speed_10m,"
    "wind_direction_10m"
)

#condicional para hacer la consulta API o no hacerla, solo para debuggear.
if debbugear == False:
    #intenta consulta
    try:
        #mensaje de espera de consulta API
        with st.spinner("🌦️ Consultando condiciones meteorológicas..."):
            respuesta = requests.get(url, timeout=5)
            respuesta.raise_for_status()

            weather = respuesta.json()

    #si la consulta no es satisfactoria
    except Exception:

        st.warning("⚠️ No se pudo conectar a la API. Usando datos locales.")

        with open("respaldo_clima.json", "r", encoding="utf-8") as archivo:
            weather = json.load(archivo)

#recibe JSON con respuestas, algunas anidadas (poner atención en current)

#presenta título
st.title("🌤️ Reporte del Clima por Chuck Norris - INACAP Puerto Montt")

st.divider()

#reparte dos columnas de forma equitativa
col1, col2 = st.columns([2,1])

with col1:

    #el CSS no se lleva bien con los saltos de linea en st.markdown, ojo
    st.markdown(
        f"""
            <style>
                .texto {{
                    z-index: 10;
                    color: white;
                    text-shadow:
                    -1px -1px 0 black,
                    1px -1px 0 black,
                    -1px  1px 0 black,
                    1px  1px 0 black;
                    padding: 20px;
                }}
                /* Contenedor principal del banner */
                .banner-clima {{
                    width: 100%;
                    height: 200px;
                    border-radius: 12px;
                    overflow: hidden;
                    position: relative;
                    background-image: url("data:image/jpeg;base64,{img_sol}");
                    background-size: cover;
                    background-position: center;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    z-index: 1;
                }}
                /* Capa superior (lluvia) que se desvanece */
                .banner-clima::before {{
                    content: "";
                    position: absolute;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background-image: url("data:image/jpeg;base64,{img_lluvia}");
                    background-size: cover;
                    background-position: center;
                    z-index: 1;
                    /* AQUÍ SE DEFINE LA ANIMACIÓN DE 5 SEGUNDOS */
                    animation: transicionClima 5s ease-in-out infinite alternate;
                }}
                /* Efecto de transición suave (opacidad) */
                @keyframes transicionClima {{
                    0% {{ opacity: 1; }}    /* 100% Lluvia */
                    30% {{ opacity: 1; }}   /* Mantiene la lluvia un momento */
                    70% {{ opacity: 0; }}   /* Mantiene el sol un momento */
                    100% {{ opacity: 0; }}  /* 100% Sol (se ve la imagen de fondo) */
                }}
            </style>
            <div class="banner-clima">
                <div class = "texto">
                <h1>{weather['current']['temperature_2m']} °C</h1>
                <h3>Sensación térmica: {weather['current']['apparent_temperature']} °C</h3>
                </div>
            </div>
        """,
        unsafe_allow_html=True
    )

#columna de porcentaje de precipitaciones
with col2:
    st.metric(
        "🌧️ Precipitación",
        f"{weather['current']['precipitation']} mm"
    )

st.divider()

#chistes de chuck norris
with open("chistes.csv", "r", encoding="utf-8") as archivo:
    chistes = [linea.strip() for linea in archivo]

if st.button("😎 Chiste del día...") or primera_vez == True:
    st.success(random.choice(chistes))
    primera_vez = False;

st.divider()

#define 3 columnas muestra métricas
c1, c2, c3 = st.columns(3)

humedad = weather['current']['relative_humidity_2m']

with c1:

    c1.metric("💧 Humedad", f"{weather['current']['relative_humidity_2m']} %")
    st.progress(humedad)
    st.write(f"{humedad}%")

st.divider()

#consulta presión actual
presion = weather['current']['pressure_msl']
presion = (presion - 800) / 1000 #división para mostrar en la barra horizontal

#límite
if 0 > presion > 1:
    presion = 1

with c2:
    c2.metric("💨 Presión Relativa del Aire", f"{weather['current']['pressure_msl']} hPa")
    st.progress(presion)
    st.write(f"{presion}%")

#consulta velocidad del viento actual
velocidad_viento = weather['current']['wind_speed_10m'] / 50

#límite
if 0 > velocidad_viento > 1:
    velocidad_viento = 1

with c3:
    c3.metric("💨 Viento", f"{weather['current']['wind_speed_10m']} m/s")
    st.progress(velocidad_viento)
    st.write(f"{velocidad_viento}%")

#define columnas - reparte equitativamente espaciado
columna_1, columna_2, columna_3 = st.columns(3)

with columna_1:

    humedad = weather['current']['relative_humidity_2m']

    #dibuja gauge de humedad relativa
    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=humedad,
    number={"suffix": "%"},
    title={"text": "Humedad Relativa"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "#0D4715"},
        "steps": [
        {"range": [0, 20], "color": "#E8F5E9"},
        {"range": [20, 40], "color": "#C8E6C9"},
        {"range": [40, 60], "color": "#81C784"},
        {"range": [60, 80], "color": "#4CAF50"},
        {"range": [80, 100], "color": "#1B5E20"}
        ]
    }
    ))

    st.plotly_chart(fig, use_container_width=True)

with columna_2:

    #dibuja gauge de nubosidad
    nubosidad = weather['current']['cloud_cover']

    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=nubosidad,
    number={"suffix": "%"},
    title={"text": "☁️ Nubosidad"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "#003366"},  # Aguja/barra azul marino
        "steps": [
        {"range": [0, 25], "color": "#D6EAF8"},
        {"range": [25, 50], "color": "#85C1E9"},
        {"range": [50, 75], "color": "#3498DB"},
        {"range": [75, 100], "color": "#1B4F72"}
        ]
    }
    ))

    st.plotly_chart(fig, use_container_width=True)

with columna_3:

    temperatura = weather['current']['temperature_2m']

    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=temperatura,
    number={"suffix": "°"},
    title={"text": "Temperatura"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "#7F0000"},  # Rojo oscuro para la barra
        "steps": [
        {"range": [0, 25], "color": "#FDEDEC"},
        {"range": [25, 50], "color": "#F5B7B1"},
        {"range": [50, 75], "color": "#EC7063"},
        {"range": [75, 100], "color": "#922B21"}
        ]
    }
    ))

    st.plotly_chart(fig, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

#fila consejos del día y dirección del viento
with col1:

    #llamar a función obtener_respuesta (parámetros enviados)
    respuesta = obtener_respuesta(temperatura)

    #consejo de chuck norris
    #st.image("chuck_norris.webp", width=500, caption="💪 Chuck Norris dice...")

    with open("chuck_norris.webp", "rb") as img:
        data = base64.b64encode(img.read()).decode()

        st.markdown(f"""
        <style>
        .targeta {{
            box-shadow:0px 5px 15px rgba(0,0,0,0.3);
            text-align:center;
            display:flex;
            justify-content:center;
            padding: 20px;
        }}
        .zoom img {{
            border-radius: 10px;
            transition: transform 0.3s;
        }}
        .zoom img:hover {{
            transform: scale(1.10);
        }}
        </style>
        <div class="targeta">
            <div class="zoom">
                <img src="data:image/webp;base64,{data}" width="500">
                <h3>Consejo del día:</h3>
                <h4>{respuesta}</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
#dirección del viento
with col2:

    fig = go.Figure()

    #eje de coordenadas circular tipo radar
    fig.add_trace(go.Scatterpolar(
        r=[1],
        theta=[weather['current']["wind_direction_10m"]], #define el ángulo theta
        mode="markers",
        marker_size=20
    ))

    fig.update_layout(
        polar=dict(
        radialaxis=dict(
            visible=False,
            range=[0,1]
        ),
        angularaxis=dict(
            tickmode='array',
            tickvals=[0,45,90,135,180,225,270,315], #ángulos de divisiones del scatterpolar
            ticktext=['Norte','Noreste','Este','Sureste','Sur','Suroeste','Oeste','Norte'] #textos de ángulos
        )
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    velocidad = 20

st.divider()

#presentar json en pantalla, lo usé para debuggear ya no lo uso
#st.write('Consulta API en JSON:')
#st.write(weather)

with st.expander("Ver JSON completo"):
    st.json(weather)


