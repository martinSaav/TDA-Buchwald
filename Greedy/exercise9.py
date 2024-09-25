def minimizar_latencia(L_deadline, T_tareas):
    tareas = list(zip(T_tareas, L_deadline))

    tareas.sort(key=lambda tarea: tarea[1])

    tiempo_transcurrido = 0
    orden = []
    for tiempo_tarea, deadline in tareas:
        tiempo_transcurrido += tiempo_tarea
        orden.append((tiempo_tarea, max(0, tiempo_transcurrido - deadline)))

    return orden

# Se trata de un algoritmo greedy porque siempre se realiza la tarea que tiene menor deadline (regla sencilla esperando acumular menor latencia (optimo local). 
# Esto se realiza para cada tarea disponible, llegando a la latencia mínima total (optimo general)