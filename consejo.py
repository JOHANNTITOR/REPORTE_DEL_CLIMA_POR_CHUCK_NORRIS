import random

#mi primera función, parámetro recibido (temperatura)
def obtener_respuesta(temperatura):
    
    if temperatura < 5:
        respuesta = "hoy decidí abrir mi refrigerador, así que abrigate como si fueses al Everest!"

    if temperatura >= 5 < 10:
        respuesta = "hoy miré al sol fijamente y se alejó, así que abrigate bien antes de salir!"

    if temperatura >= 10 < 15:
        respuesta = "hoy decidí que iba a hacer frío, asi que ponte algo de abrigo colega!"

    if temperatura >= 15 < 20:
        respuesta = "hoy decidí que iba a estar fresco, usa ropa normal!"

    if temperatura >= 20 < 25:
        respuesta = "Hoy estoy de buen humor así que decidí un clima cálido y agradable, así que sale con shorts!"

    if temperatura >= 25 < 40:
        respuesta = "Hoy le puse más combustible al sol, así, vete a la playa!"

    
    
    #envía retorno desde función
    return respuesta
