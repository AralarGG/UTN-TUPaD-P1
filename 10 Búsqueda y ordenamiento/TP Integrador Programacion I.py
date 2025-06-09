import time
import random
import sys

# Ajustar el límite de recursión por si acaso (necesario para la búsqueda recursiva en listas grandes).
# Por defecto, Python tiene un límite de recursión de alrededor de 1000. Para listas muy grandes,
# la búsqueda recursiva podría excederlo. Aumentarlo previene errores de "RecursionError".
sys.setrecursionlimit(20000)

print("--- Caso Práctico: Comparación de Eficiencia de Búsqueda ---")
print("--- Simulando búsqueda en una base de datos simple ---")

# --- 1. Definición de Algoritmos de Búsqueda ---

def busqueda_lineal(lista, objetivo):
    """
    Busca un objetivo en una lista de forma lineal.
    Este algoritmo recorre cada elemento de la lista uno por uno.
    Es simple pero ineficiente para grandes volúmenes de datos.

    Args:
        lista (list): La lista de elementos donde se realizará la búsqueda.
        objetivo: El elemento que se desea encontrar en la lista.

    Returns:
        int: El índice del elemento si lo encuentra, o -1 si el objetivo no está en la lista.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna el índice tan pronto como encuentra el objetivo
    return -1  # Retorna -1 si el bucle termina sin encontrar el objetivo

def busqueda_binaria_iterativa(lista, objetivo):
    """
    Busca un objetivo en una lista ORDENADA de forma binaria (iterativa).
    Este método divide repetidamente la lista a la mitad para reducir el espacio de búsqueda.
    Requiere que la lista esté previamente ordenada para funcionar correctamente.

    Args:
        lista (list): La lista de elementos ordenada donde se realizará la búsqueda.
        objetivo: El elemento que se desea encontrar en la lista.

    Returns:
        int: El índice del elemento si lo encuentra, o -1 si el objetivo no está en la lista.
    """
    izquierda, derecha = 0, len(lista) - 1
    
    # El bucle continúa mientras el rango de búsqueda sea válido
    while izquierda <= derecha:
        # Calcula el índice del elemento central. Se usa esta fórmula para evitar
        # un posible desbordamiento de enteros (overflow) en listas extremadamente grandes.
        medio = izquierda + (derecha - izquierda) // 2 
        
        # Compara el elemento central con el objetivo
        if lista[medio] == objetivo:
            return medio  # Elemento encontrado, retorna su índice.
        elif lista[medio] < objetivo:
            # Si el elemento central es menor que el objetivo, significa que el objetivo
            # (si existe) debe estar en la mitad derecha de la lista. Se ajusta el límite izquierdo.
            izquierda = medio + 1
        else:
            # Si el elemento central es mayor que el objetivo, el objetivo (si existe)
            # debe estar en la mitad izquierda. Se ajusta el límite derecho.
            derecha = medio - 1
            
    return -1  # El objetivo no fue encontrado después de agotar el espacio de búsqueda.

def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
    """
    Busca un objetivo en una lista ORDENADA de forma binaria (recursiva).
    Esta implementación usa la recursión para dividir el problema en subproblemas más pequeños.
    Requiere que la lista esté previamente ordenada.

    Args:
        lista (list): La lista de elementos ordenada donde se realizará la búsqueda.
        objetivo: El elemento que se desea encontrar en la lista.
        izquierda (int): El índice de inicio del subrango de búsqueda actual (por defecto 0).
        derecha (int): El índice de fin del subrango de búsqueda actual (por defecto el último índice).

    Returns:
        int: El índice del elemento si lo encuentra, o -1 si el objetivo no está en la lista.
    """
    # Inicializa el puntero derecho si es la primera llamada a la función (derecha es None).
    if derecha is None:
        derecha = len(lista) - 1
    
    # Caso base de la recursión: si el rango de búsqueda es inválido, el elemento no está presente.
    if izquierda > derecha:
        return -1
    
    # Calcula el índice del elemento central del subrango actual.
    medio = izquierda + (derecha - izquierda) // 2
    
    # Compara el elemento central con el objetivo.
    if lista[medio] == objetivo:
        return medio  # Caso base: el elemento ha sido encontrado.
    elif lista[medio] < objetivo:
        # Si el elemento central es menor que el objetivo, se realiza una llamada recursiva
        # para buscar en la mitad derecha del subrango.
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        # Si el elemento central es mayor que el objetivo, se realiza una llamada recursiva
        # para buscar en la mitad izquierda del subrango.
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


# --- 2. Función para Generar Datos de Prueba ---

def generar_lista_aleatoria(tamano):
    """
    Genera una lista de números enteros aleatorios y únicos de un tamaño dado.
    Esta función simula los datos de una 'base de datos' para las pruebas.

    Args:
        tamano (int): El número de elementos que tendrá la lista.

    Returns:
        list: Una lista de números enteros aleatorios y únicos.
    """
    # Genera una lista de números aleatorios y únicos. El rango es 10 veces el tamaño
    # para asegurar que haya suficientes números únicos disponibles para seleccionar.
    return random.sample(range(1, tamano * 10 + 1), tamano)

# --- 3. Ejecución y Medición de Eficiencia ---

# Definir los tamaños de las listas a probar para la simulación.
# Se eligen varios tamaños para observar cómo la eficiencia de los algoritmos
# varía con el volumen de datos, permitiendo una comparación clara de la complejidad temporal.
tamano_listas = [10, 100, 1000, 10000, 100000, 1000000]

# Listas para almacenar los resultados de tiempo de cada algoritmo y tamaño de lista
resultados_busqueda_lineal = []
resultados_busqueda_binaria_iterativa = []
resultados_busqueda_binaria_recursiva = []

# Bucle principal para iterar sobre los diferentes tamaños de lista
for tamano in tamano_listas:
    print(f"\n--- Probando con una lista de {tamano} elementos ---")
    
    # Generar una nueva lista aleatoria para cada tamaño de prueba
    lista_original = generar_lista_aleatoria(tamano)
    
    # Seleccionar un objetivo existente (garantizado en la lista) para medir el caso promedio/mejor
    objetivo_existente = random.choice(lista_original)
    # Seleccionar un objetivo que NO exista en la lista (para simular el peor caso)
    objetivo_no_existente = tamano * 10 + 2 # Se elige un número fuera del rango de generación
    
    # --- A. Búsqueda Lineal ---
    print(f"  Realizando Búsqueda Lineal para objetivo {objetivo_existente} (existente)...")
    inicio_lineal = time.perf_counter() # Marca el tiempo de inicio de la operación
    resultado_lineal_existente = busqueda_lineal(lista_original, objetivo_existente)
    fin_lineal = time.perf_counter()   # Marca el tiempo de fin de la operación
    tiempo_lineal_existente = (fin_lineal - inicio_lineal) * 1000 # Convierte a milisegundos
    
    print(f"    - Búsqueda Lineal (existente): Índice {resultado_lineal_existente}, Tiempo: {tiempo_lineal_existente:.4f} ms")

    print(f"  Realizando Búsqueda Lineal para objetivo {objetivo_no_existente} (no existente/peor caso)...")
    inicio_lineal_no_existente = time.perf_counter()
    resultado_lineal_no_existente = busqueda_lineal(lista_original, objetivo_no_existente)
    fin_lineal_no_existente = time.perf_counter()
    tiempo_lineal_no_existente = (fin_lineal_no_existente - inicio_lineal_no_existente) * 1000
    
    print(f"    - Búsqueda Lineal (no existente/peor caso): Tiempo: {tiempo_lineal_no_existente:.4f} ms")
    # Almacena los resultados para la tabla resumen
    resultados_busqueda_lineal.append((tamano, tiempo_lineal_existente, tiempo_lineal_no_existente))

    # --- B. Preparación para Búsquedas Binarias (Ordenamiento de la Lista) ---
    # La búsqueda binaria REQUIERE que la lista esté ordenada. El tiempo de este
    # paso de ordenamiento es crucial para un análisis completo de la eficiencia total.
    print(f"  Ordenando la lista para Búsquedas Binarias...")
    inicio_ordenamiento = time.perf_counter()
    # sorted() en Python usa Timsort, que es un algoritmo de ordenamiento híbrido
    # con una complejidad de O(N log N) en promedio y peor caso.
    lista_ordenada = sorted(lista_original) 
    fin_ordenamiento = time.perf_counter()
    tiempo_ordenamiento = (fin_ordenamiento - inicio_ordenamiento) * 1000
    print(f"    - Tiempo de ordenamiento: {tiempo_ordenamiento:.4f} ms")

    # --- C. Búsqueda Binaria Iterativa ---
    print(f"  Realizando Búsqueda Binaria Iterativa para objetivo {objetivo_existente} (existente)...")
    inicio_binaria_iterativa = time.perf_counter()
    resultado_binaria_iterativa_existente = busqueda_binaria_iterativa(lista_ordenada, objetivo_existente)
    fin_binaria_iterativa = time.perf_counter()
    tiempo_binaria_iterativa_existente = (fin_binaria_iterativa - inicio_binaria_iterativa) * 1000
    
    print(f"    - Búsqueda Binaria Iterativa (existente): Índice {resultado_binaria_iterativa_existente}, Tiempo: {tiempo_binaria_iterativa_existente:.4f} ms")

    print(f"  Realizando Búsqueda Binaria Iterativa para objetivo {objetivo_no_existente} (no existente/peor caso)...")
    inicio_binaria_iterativa_no_existente = time.perf_counter()
    resultado_binaria_iterativa_no_existente = busqueda_binaria_iterativa(lista_ordenada, objetivo_no_existente)
    fin_binaria_iterativa_no_existente = time.perf_counter()
    tiempo_binaria_iterativa_no_existente = (fin_binaria_iterativa_no_existente - inicio_binaria_iterativa_no_existente) * 1000
    
    print(f"    - Búsqueda Binaria Iterativa (no existente/peor caso): Tiempo: {tiempo_binaria_iterativa_no_existente:.4f} ms")
    resultados_busqueda_binaria_iterativa.append((tamano, tiempo_binaria_iterativa_existente, tiempo_binaria_iterativa_no_existente, tiempo_ordenamiento))

    # --- D. Búsqueda Binaria Recursiva ---
    # Se clona la lista ordenada para asegurar que no haya efectos secundarios entre las pruebas
    # (aunque en este caso no sería un problema, es buena práctica si las funciones modificaran la lista).
    lista_ordenada_recursiva = list(lista_ordenada) 

    print(f"  Realizando Búsqueda Binaria Recursiva para objetivo {objetivo_existente} (existente)...")
    inicio_binaria_recursiva = time.perf_counter()
    # Para la primera llamada recursiva, se pasan los límites iniciales del rango de búsqueda.
    resultado_binaria_recursiva_existente = busqueda_binaria_recursiva(lista_ordenada_recursiva, objetivo_existente) 
    fin_binaria_recursiva = time.perf_counter()
    tiempo_binaria_recursiva_existente = (fin_binaria_recursiva - inicio_binaria_recursiva) * 1000
    
    print(f"    - Búsqueda Binaria Recursiva (existente): Índice {resultado_binaria_recursiva_existente}, Tiempo: {tiempo_binaria_recursiva_existente:.4f} ms")

    print(f"  Realizando Búsqueda Binaria Recursiva para objetivo {objetivo_no_existente} (no existente/peor caso)...")
    inicio_binaria_recursiva_no_existente = time.perf_counter()
    resultado_binaria_recursiva_no_existente = busqueda_binaria_recursiva(lista_ordenada_recursiva, objetivo_no_existente)
    fin_binaria_recursiva_no_existente = time.perf_counter()
    tiempo_binaria_recursiva_no_existente = (fin_binaria_recursiva_no_existente - inicio_binaria_recursiva_no_existente) * 1000
    
    print(f"    - Búsqueda Binaria Recursiva (no existente/peor caso): Tiempo: {tiempo_binaria_recursiva_no_existente:.4f} ms")
    resultados_busqueda_binaria_recursiva.append((tamano, tiempo_binaria_recursiva_existente, tiempo_binaria_recursiva_no_existente, tiempo_ordenamiento))


# --- 4. Resumen de Tiempos de Ejecución (Tablas de Resultados para Análisis) ---

print("\n--- Resumen de Tiempos de Ejecución ---")

print("\nBúsqueda Lineal:")
print("| Tamaño de Lista | Tiempo (ms) - Existente | Tiempo (ms) - No Existente (Peor Caso) |")
print("|-----------------|-------------------------|----------------------------------------|")
for tamano, t_existente, t_no_existente in resultados_busqueda_lineal:
    print(f"| {tamano:<15} | {t_existente:<23.4f} | {t_no_existente:<38.4f} |")

print("\nBúsqueda Binaria Iterativa (Incluye tiempo de ordenamiento):")
print("| Tamaño de Lista | Tiempo Ordenamiento (ms) | Tiempo Búsqueda (ms) - Existente | Tiempo Búsqueda (ms) - No Existente (Peor Caso) |")
print("|-----------------|--------------------------|----------------------------------|-------------------------------------------------|")
for tamano, t_bin_iter_existente, t_bin_iter_no_existente, t_ordenamiento in resultados_busqueda_binaria_iterativa:
    print(f"| {tamano:<15} | {t_ordenamiento:<24.4f} | {t_bin_iter_existente:<32.4f} | {t_bin_iter_no_existente:<47.4f} |")

print("\nBúsqueda Binaria Recursiva (Incluye tiempo de ordenamiento):")
print("| Tamaño de Lista | Tiempo Ordenamiento (ms) | Tiempo Búsqueda (ms) - Existente | Tiempo Búsqueda (ms) - No Existente (Peor Caso) |")
print("|-----------------|--------------------------|----------------------------------|-------------------------------------------------|")
for tamano, t_bin_recur_existente, t_bin_recur_no_existente, t_ordenamiento in resultados_busqueda_binaria_recursiva:
    print(f"| {tamano:<15} | {t_ordenamiento:<24.4f} | {t_bin_recur_existente:<32.4f} | {t_bin_recur_no_existente:<47.4f} |")

print("\nAnálisis Adicional (Para la sección de Resultados Obtenidos y Conclusiones):")
print("Para una evaluación completa de la Búsqueda Binaria en datos no ordenados inicialmente,")
print("se debe considerar el tiempo total de 'Ordenamiento + Búsqueda'.")
print("Comparando el 'Tiempo (ms) - No Existente (Peor Caso)' de la búsqueda Lineal con la suma")
print("de 'Tiempo Ordenamiento (ms)' y 'Tiempo Búsqueda (ms) - No Existente (Peor Caso)' de la Binaria (iterativa o recursiva),")
print("podrán ver en qué punto la Búsqueda Binaria se vuelve más eficiente, incluso con el costo de ordenamiento.")
