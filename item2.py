from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad, pais):
    """Obtiene coordenadas de una ciudad."""
    geolocator = Nominatim(user_agent="distancia_ciudades")
    try:
        ubicacion = geolocator.geocode(f"{ciudad}, {pais}", timeout=10)
        if ubicacion:
            return (ubicacion.latitude, ubicacion.longitude)
    except Exception as e:
        print(f"Error al obtener coordenadas: {e}")
    return None

def calcular_distancia(coord1, coord2):
    """Calcula la distancia en kilómetros entre dos coordenadas."""
    return geodesic(coord1, coord2).kilometers

def obtener_duracion(distancia_km, medio):
    """Calcula duración del viaje según medio de transporte."""
    velocidades = {
        "auto": 80,
        "bus": 60,
        "bicicleta": 20,
        "caminando": 5,
        "avion": 700
    }
    velocidad = velocidades.get(medio.lower())
    if velocidad:
        horas = distancia_km / velocidad
        return int(horas), int((horas - int(horas)) * 60)
    else:
        return None, None

def narrativa_viaje(ciudad_origen, ciudad_destino, medio, distancia_km, horas, minutos):
    """Genera una narrativa descriptiva del viaje."""
    return (f"\nViajando desde {ciudad_origen} en Chile hasta {ciudad_destino} en Argentina "
            f"en {medio}, recorrerás aproximadamente {distancia_km:.2f} km. "
            f"El trayecto tomará unas {horas} horas y {minutos} minutos, "
            f"dependiendo de las condiciones del clima y tráfico. ¡Buen viaje!\n")

def mostrar_medios():
    print("\nMedios disponibles:")
    print(" - auto")
    print(" - bus")
    print(" - bicicleta")
    print(" - caminando")
    print(" - avion\n")

def main():
    while True:
        print("\n--- Cálculo de distancia entre ciudades ---")
        ciudad_origen = input("Ingrese la ciudad de origen en Chile (o 's' para salir): ").strip()
        if ciudad_origen.lower() == 's':
            print("Saliendo del programa.")
            break

        ciudad_destino = input("Ingrese la ciudad de destino en Argentina (o 's' para salir): ").strip()
        if ciudad_destino.lower() == 's':
            print("Saliendo del programa.")
            break

        origen = obtener_coordenadas(ciudad_origen, "Chile")
        destino = obtener_coordenadas(ciudad_destino, "Argentina")

        if origen is None:
            print(f"No se encontró la ciudad de origen: {ciudad_origen}")
            continue
        if destino is None:
            print(f"No se encontró la ciudad de destino: {ciudad_destino}")
            continue

        distancia_km = calcular_distancia(origen, destino)
        distancia_millas = distancia_km * 0.621371

        mostrar_medios()
        medio = input("Seleccione el medio de transporte: ").strip().lower()
        horas, minutos = obtener_duracion(distancia_km, medio)

        if horas is None:
            print("Medio de transporte no válido. Intente nuevamente.")
            continue

        print(f"\nDistancia entre {ciudad_origen} y {ciudad_destino}:")
        print(f"- {distancia_km:.2f} kilómetros")
        print(f"- {distancia_millas:.2f} millas")
        print(f"- Duración estimada del viaje en {medio}: {horas} h y {minutos} min")

        print(narrativa_viaje(ciudad_origen, ciudad_destino, medio, distancia_km, horas, minutos))

if __name__ == "__main__":
    main()