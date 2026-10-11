from modulos import RegistrarExpediente, ConsultarExpediente , OrdenarExpediente , GuardarInformacion
def MostrarMenu():
    print("\n==== SISTEMA DE EXPEDIENTES ====")
    print("1. Registrar expediente")
    print("2. Consultar expediente")
    print("3. Ordenar expedientes")
    print("4. Guardar informacion")
    print("5. Salir")

def main():
    # Listas paralelas para almacenar los datos 
    codigos = []
    nombres = []
    documentos = []
    tramites = []
    descripciones = []
    fechas = []
    areas = []

    opcion = 0
    while opcion != 5:
        MostrarMenu()
        #Intentamos convertir lo que escribe el usuario a un numero entero
        # Si el usuario ingresa una letra u otro simbolo que no es numerico le saldra ValueError.
        try:
            opcion = int(input("Seleccione una opcion:"))
        except ValueError:
            print("Por favor, ingrese un numero valido.")
            continue

        if opcion == 1:
            RegistrarExpediente(codigos,nombres,documentos,tramites,descripciones,fechas,areas)
        elif opcion == 2:
            ConsultarExpediente(codigos, nombres, documentos, tramites, descripciones, fechas, areas)
        elif opcion == 3:
            OrdenarExpediente(codigos, nombres, documentos, tramites, descripciones, fechas, areas)
        elif opcion == 4:
            GuardarInformacion(codigos, nombres, documentos, tramites, descripciones, fechas, areas)
        elif opcion == 5:
            print("Saliendo del sistema...")
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()



