# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: [Alexia] & [Mariangeles] & [Natalia]
# =====================================================================

from calculadora import estimar_consumo_wh, calcular_huella_co2

def solicitar_numero_positivo(mensaje: str, tipo=float):
    """Solicita un número positivo y controla los errores de entrada."""
    while True:
        try:
            valor = tipo(input(mensaje))

            if valor <= 0:
                print("Error: introduce un número mayor que cero.")
                continue

            return valor

        except ValueError:
            print("Error: introduce un número válido.")


def main():
    """Muestra el menú principal y ejecuta las opciones."""
    while True:
        print("\n========== ECOAUDIT CLI ==========")
        print("1. Realizar auditoría energética")
        print("2. Consultar históricos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n--- AUDITORÍA ENERGÉTICA ---")

            proceso = input("Nombre del equipo/proceso: ").strip()

            if not proceso:
                print("Error: el nombre no puede estar vacío.")
                continue

            potencia = solicitar_numero_positivo("Potencia consumida en Vatios (W): ")

            horas = solicitar_numero_positivo("Horas de uso diario: ")

            iteraciones = solicitar_numero_positivo("Número de iteraciones del proceso: ", int)

            consumo = estimar_consumo_wh(potencia, horas, iteraciones)

            huella = calcular_huella_co2(consumo)

            print(f"\nResultados calculados para '{proceso}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono estimada: {huella:.4f} g CO2")
            
            with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
                archivo.write(f"{proceso},{potencia},{horas},{iteraciones},{consumo:.2f},{huella:.4f}\n")
            print("💾 Registro guardado con éxito en 'auditorias.csv'.")

        elif opcion == "2":
            print("\n================ HISTORIAL DE AUDITORÍAS ================")
            try:
                # Abre el archivo en modo lectura ("r") y muestra su contenido
                with open("auditorias.csv", mode="r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                    print(contenido)
                    
            except FileNotFoundError:
                # Si todavía no existe el archivo, evitamos que el programa falle
                print("ℹ️ Aún no existen registros. Realiza una auditoría primero.")

        elif opcion == "3":
            print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Selecciona 1, 2 o 3.")


if __name__ == "__main__":
    main()