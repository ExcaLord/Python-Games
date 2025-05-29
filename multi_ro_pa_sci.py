import random
from typing import Dict, List

# --------------------------------
# Configuración de Variantes del Juego
# --------------------------------
# Diccionario que almacena todas las variantes del juego con sus reglas y opciones específicas.
# Cada variante contiene:
# - nombre: Nombre para mostrar de la variante.
# - opciones: Lista de jugadas válidas.
# - reglas: Diccionario que define qué jugadas vencen a otras jugadas.

VARIANTES_JUEGO = {
    "1": {
        "nombre": "Juego Clásico",
        "opciones": ["piedra", "papel", "tijeras"],
        "reglas": {"piedra": ["tijeras"], "papel": ["piedra"], "tijeras": ["papel"]},
    },
    "2": {
        "nombre": "Big Bang Theory",
        "opciones": ["piedra", "papel", "tijeras", "lagarto", "spock"],
        "reglas": {
            "piedra": ["tijeras", "lagarto"],
            "papel": ["piedra", "spock"],
            "tijeras": ["papel", "lagarto"],
            "lagarto": ["papel", "spock"],
            "spock": ["piedra", "tijeras"],
        },
    },
    "3": {
        "nombre": "Europeo",
        "opciones": ["piedra", "papel", "tijeras", "pozo"],
        "reglas": {
            "piedra": ["tijeras"],
            "papel": ["piedra", "pozo"],
            "tijeras": ["papel"],
            "pozo": ["piedra", "tijeras"],
        },
    },
    "4": {
        "nombre": "Héroe del Escudo",
        "opciones": ["piedra", "papel", "tijeras", "dinamita", "escudo"],
        "reglas": {
            "piedra": ["tijeras", "dinamita"],
            "papel": ["piedra", "escudo"],
            "tijeras": ["papel", "escudo"],
            "dinamita": ["piedra", "tijeras"],
            "escudo": ["dinamita", "piedra"],
        },
    },
    "5": {
        "nombre": "Rayo",
        "opciones": ["piedra", "papel", "tijeras", "árbol", "rayo"],
        "reglas": {
            "piedra": ["tijeras", "rayo"],
            "papel": ["piedra", "árbol"],
            "tijeras": ["papel", "árbol"],
            "árbol": ["rayo", "piedra"],
            "rayo": ["papel", "árbol"],
        },
    },
}


# --------------------------------
# Funciones del Juego
# --------------------------------


def imprimir_tutorial(variante: Dict) -> None:
    """Imprime el tutorial para una variante específica del juego."""
    print(f"\nTutorial para {variante['nombre']}:")
    print(f"Opciones disponibles: {', '.join(variante['opciones'])}")
    print("\nReglas:")
    for opcion, vence_a_lista in variante["reglas"].items():
        for vencido in vence_a_lista:
            print(f"-> {opcion} vence a {vencido}")


def obtener_eleccion_usuario(opciones: List[str]) -> str:
    """
    Obtiene y valida la elección de jugada del usuario.

    Args:
        opciones (List[str]): Lista de jugadas válidas entre las que el usuario puede elegir.

    Returns:
        str: La elección validada del usuario de entre las jugadas disponibles.

    Nota:
        - Muestra opciones numeradas para la selección del usuario.
        - Valida que la entrada sea un número válido dentro del rango.
        - Sigue preguntando hasta recibir una entrada válida.
    """
    while True:
        print("\nElige tu jugada:")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}: {opcion}")

        entrada_usuario = input("\nIngresa tu elección (número): ")
        if entrada_usuario.isdigit() and 1 <= int(entrada_usuario) <= len(opciones):
            return opciones[int(entrada_usuario) - 1]
        print("¡Elección inválida! Por favor, ingresa un número válido.")


def determinar_ganador(
    eleccion_jugador: str, eleccion_computadora: str, reglas: Dict
) -> str:
    """
    Determina el ganador del juego basándose en las elecciones y las reglas del juego.

    Args:
        eleccion_jugador (str): La jugada elegida por el jugador.
        eleccion_computadora (str): La jugada elegida por la computadora.
        reglas (Dict): Diccionario que contiene las reglas del juego, definiendo qué jugadas vencen a otras.

    Returns:
        str: Un mensaje indicando el resultado (ganar/perder/empatar).

    Lógica:
        - Si ambas elecciones son iguales -> Empate.
        - Si la elección de la computadora está en la lista de jugadas que la elección del jugador vence -> El jugador gana.
        - De lo contrario -> La computadora gana.
    """
    if eleccion_jugador == eleccion_computadora:
        return "¡Es un empate!"
    elif eleccion_computadora in reglas[eleccion_jugador]:
        return "¡Ganaste! 🎉"
    else:
        return "¡Perdiste! 😢"


def principal():
    """
    Función principal del juego que controla el flujo del mismo.

    Flujo:
        1. Muestra mensaje de bienvenida.
        2. Muestra las variantes de juego disponibles.
        3. Obtiene la elección de variante de juego del usuario.
        4. Ofrece un tutorial opcional.
        5. Inicia el bucle principal del juego:
           - Obtiene la jugada del jugador.
           - Genera la jugada de la computadora.
           - Determina el ganador.
           - Pregunta si desea jugar de nuevo.
        6. Muestra mensaje de despedida cuando el jugador termina.

    Nota:
        - El juego está completamente en español.
        - Cada variante tiene su propio conjunto de reglas y jugadas.
        - La elección de la computadora se selecciona aleatoriamente.
    """
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    print("\nVersiones disponibles:")
    for clave, variante_info in VARIANTES_JUEGO.items():
        print(f"{clave}: {variante_info['nombre']}")

    # Obtener versión del juego
    while True:
        version_juego_elegida = input("\nElige una versión (1-5): ")
        if version_juego_elegida in VARIANTES_JUEGO:
            break
        print("¡Versión inválida! Por favor, elige un número entre 1 y 5.")

    variante_actual = VARIANTES_JUEGO[version_juego_elegida]

    # Mostrar tutorial si se solicita
    ver_tutorial = input("\n¿Quieres ver el tutorial? (sí/no): ").lower()
    if ver_tutorial.startswith("s"):  # 's' para "sí"
        imprimir_tutorial(variante_actual)

    # Bucle principal del juego
    while True:
        # Obtener elecciones
        eleccion_jugador = obtener_eleccion_usuario(variante_actual["opciones"])
        eleccion_computadora = random.choice(variante_actual["opciones"])

        # Mostrar elecciones
        print(f"\nTu elección: {eleccion_jugador}")
        print(f"Elección de la computadora: {eleccion_computadora}")

        # Determinar y mostrar ganador
        resultado = determinar_ganador(
            eleccion_jugador, eleccion_computadora, variante_actual["reglas"]
        )
        print(f"\n{resultado}")

        # ¿Jugar de nuevo?
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (sí/no): ").lower()
        if not jugar_de_nuevo.startswith("s"):  # 's' para "sí"
            break

    print("\n¡Gracias por jugar!")


if __name__ == "__main__":
    principal()

