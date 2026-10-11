def SeleccionarTramite():
    print("\n===== TIPO DE TRAMITE =====")
    print("1. Solicitud administrativa")
    print("2. Licencia o autorizacion")
    print("3. Certificado o constancia")
    print("4. Reclamo o queja")
    print("5. Recurso administrativo")
    print("6. Acceso a la informacion publica")
    print("7. Otros")
    
    opcion = input("Seleccione el tipo de tramite: ")
    
    if opcion == "1":
        return "Solicitud administrativa"
    elif opcion == "2":
        return "Licencia o autorizacion"
    elif opcion == "3":
        return "Certificado o constancia"
    elif opcion == "4":
        return "Reclamo o queja"
    elif opcion == "5":
        return "Recurso administrativo"
    elif opcion == "6":
        return "Acceso a la informacion publica"
    else:
        print("Opcion no valida. Se registrara como otros")
        return "Otros"

def RegistrarExpediente(codigos, nombres, documentos, tramites, descripciones, fechas, areas):
    codigo = input("Codigo del expediente: ").strip()
    while codigo == "":
        print("El codigo no puede estar vacio.")
        codigo = input("Codigo del expediente: ").strip()
        
    nombre = input("Nombre del ciudadano: ")
    documento = input("Documento de identidad: ")
    tramite = SeleccionarTramite()
    descripcion = input("Descripcion: ")
    fecha = input("Fecha de recepcion: ")
    area = input("Area responsable: ")
    
    codigos.append(codigo)
    nombres.append(nombre)
    documentos.append(documento)
    tramites.append(tramite)
    descripciones.append(descripcion)
    fechas.append(fecha)
    areas.append(area)
    
    print("Expediente registrado correctamente.")

def ConsultarExpediente(codigos, nombres, documentos, tramites, descripciones, fechas, areas):
    codigo_buscar = input("Ingrese el codigo del expediente: ")
    encontrado = False
    
    for i in range(len(codigos)):
        if codigos[i] == codigo_buscar:
            print("\n===== EXPEDIENTE ENCONTRADO =====")
            print(f"Codigo: {codigos[i]}")
            print(f"Ciudadano: {nombres[i]}")
            print(f"Documento: {documentos[i]}")
            print(f"Tipo de tramite: {tramites[i]}")
            print(f"Descripcion: {descripciones[i]}")
            print(f"Fecha: {fechas[i]}")
            print(f"Area responsable: {areas[i]}")
            encontrado = True
            break
            
    if not encontrado:
        print("No se encontro el expediente.")


#En esta parte usaremos un bubble sort 

def OrdenarExpediente(codigos, nombres, documentos, tramites, descripciones, fechas, areas):
    print("Ordenando los expedientes por codigo...")
    n = len(codigos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if codigos[j] > codigos[j + 1]:
                # Intercambia todos los elementos paralelos
                codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                documentos[j], documentos[j + 1] = documentos[j + 1], documentos[j]
                tramites[j], tramites[j + 1] = tramites[j + 1], tramites[j]
                descripciones[j], descripciones[j + 1] = descripciones[j + 1], descripciones[j]
                fechas[j], fechas[j + 1] = fechas[j + 1], fechas[j]
                areas[j], areas[j + 1] = areas[j + 1], areas[j]
    print("Expedientes ordenados correctamente.")

def GuardarInformacion(codigos, nombres, documentos, tramites, descripciones, fechas, areas):
    print("Guardando informacion...")
    # Abrimos el archivo en modo escritura ('w') y usaremos codificacion utf-8 para evitar problemas con las tildes
    with open("expedientes.txt", "w", encoding="utf-8") as archivo:
        for i in range(len(codigos)):
            linea = f"{codigos[i]}|{nombres[i]}|{documentos[i]}|{tramites[i]}|{descripciones[i]}|{fechas[i]}|{areas[i]}\n"
            # Escribimos la linea construida en el archivo de texto
            archivo.write(linea)
    print("Datos guardados en el archivo 'expedientes.txt'.")