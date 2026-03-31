#Ejercicio 1 
nombre = input("Cliente:").strip()     #Pedimos el nombre al cliente.

while nombre == "" or not nombre.isalpha():    #Validamos el nombre con .isalpha para que solo pueda ingresar un dato que sea alfabético y con strip eliminando los espacios delante y detrás del texto.
    print("Error, ingrese un nombre solo con caracteres alfabéticos")
    nombre = input("Cliente: ").strip()

cantidad_string = input("Ingresa la cantidad de productos: ").strip()

while not cantidad_string.isdigit() or int(cantidad_string) == 0 :   #Validamos con .isdgit que la cantidad sea un número entero positivo.
    print("Error, ingresa un número válido")
    cantidad_string = input("Ingresa la cantidad de productos: ").strip()

cantidad_int = int(cantidad_string)              #Una vez hechas las validaciones puedo convertir a la variable cantidad a entero.

total_sindesc = 0         #Creamos las variables que contabilizarán los valores totales.
total_condesc = 0

for producto in range(1,cantidad_int+1):      #El bucle for contabiliza cantidad desde 1 y suma 1 cada vez que el cliente ingrese un producto.
    precio_string = input(f"Producto {producto} - Precio: ").strip()    #Le pedimos el precio al cliente

    while not precio_string.isdigit() or int(precio_string) == 0:   #Validamos con .isdgit que la cantidad sea un número entero positivo.
        print("Error, ingrese un precio válido.")
        precio_string = input(f"Producto{producto} - Precio: ").strip()
    
    precio_int = int(precio_string)
    desc = input("Descuento S/N: ").strip().lower()   #Creamos la variable de descuento, strip valida la información ingresada eliminando los espacios delante y detrás del texto, luego con lower lo convierte a minúsculas.

    while desc != "s" and desc !="n":   #Validamos que el cliente solo ingrese s o n para descuento si o no.
        print("Error, ingrese S(Si) o N(No) para continuar")
        desc = input("Descuento S/N: ").strip().lower()
    
    total_sindesc += precio_int   #Sumamos los precios sin descuento.

    if desc == "s":   #Si hay descuento se multiplica por el 90%, descontando el 10% de descuento.
        precio_final = precio_int * 0.9   
    else:
        precio_final = precio_int  #En otro caso, si no hay descuento, el precio final sera el original.
    total_condesc += precio_final   #Sumamos el total de los precios con descuento.

ahorro = total_sindesc - total_condesc
promedio = total_condesc / cantidad_int

print()
print(f"Total sin descuento: {total_sindesc:.2f}")  #Imprime todos los resultados formateados a .2f (dos decimales)
print(f"Total con descuento: {total_condesc:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio: ${promedio:.2f}") 


#Ejercicio 2 
usuario_correcto = "alumno"   #Definimos las variables correctas de usuario y contraseña.
clave_correcta = "python123"

acceso = False      #Definimos el acceso, solo si es True podrá continuar.

for intento in range(3):  #Mediante el bucle for contabilizamos los 3 intentos posibles del usuario.
    usuario = input("Ingrese su usuario: ")  #Pedimos usuario y clave al usuario.
    clave = input("Ingrese su contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        break    #Finalizamos el bucle si usuario y clave son correctos.
    else: 
        print("Usuario o clave incorrectos.") 

if acceso:   
    while True:   #Si el acceso es correcto ingresa al menú.
        print("MENU")
        print("")
        print("1.Ver estado de inscripción.")
        print("2.Cambiar clave")
        print("3.Mostrar mensaje motivacional")
        print("4.Salir")
        print("")
        opcion = input("Elegí una opción:")
        if not opcion.isdigit():   #Valida que la opción sea un número 
            print("Ingresá una opción válida")
            continue
        
        opcion = int(opcion)  #Valida la opción a emtero.
        if opcion <1 or opcion > 4: #Valida que la opción sea un número entre 1 y 4
            print("Ingresa una opción válida") 
            continue
        if opcion == 1:
            print("Estado: Inscripto")
        elif opcion == 2: 
            nueva_clave = input("Ingresa una nueva clave.")
            nueva_clave_confirmación = input("Ingresa la clave nuevamente.")
            if nueva_clave != nueva_clave_confirmación:
                print("Las claves no coinciden.")
            elif len(nueva_clave) < 6:  #Verifica que la clave contenga mínimo de 6 caractéres.
                print("La clave debe tener un mínimo de 6 caractéres.")
            else: 
                clave_correcta = nueva_clave
                print("Clave actualizada correctamente.")

        elif opcion == 3:
            print("Cada día es una nueva oportunidad, ponete a estudiar estructuras repetitivas.")

        elif opcion == 4: 
            print ("Saliendo.")
            break
else:
    print("Cuenta bloqueada, excedió el límite de 3 intentos.")


#Ejercicio 3
#Lunes 4 turnos ; Martes 3 turnos

nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():   #Valida que el nombre solo contenga letras, mientras sea False continuará pidiendo el nombre.
    print("Error, ingrese un nombre solo con letras: ")
    nombre = input("Ingrese su nombre: ")

#Definimos las variables de los turnos disponibles.

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""


martes1 = ""
martes2 = ""
martes3 = ""

while True:   #Si el nombre es válido (True) ingresa al menú.
    
    print("MENU")
    print("")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Elegí una opción: ")   #Validamos las opciones con .isdigit.
    if not opcion.isdigit():
        print("Ingresa una opción válida: ")
        continue
    opcion = int(opcion)    #Convertimos la opción ingresada (string) a entero. 

    if opcion < 1 or opcion > 5:
        print("Elegí una opción válida (1-5): ")   #Validamos las opciones para que sea un valor entre 1 y 5 
        continue

    if opcion == 1:
        print("Reservar")
    elif opcion == 2:
        print("Cancelar")
    elif opcion == 3:
        print("Ver agenda")
    elif opcion == 4:
        print("Resúmen general")
    elif opcion == 5:
        print("Cerrando sistema.")
    
    if opcion == 1:
        dia = input("Elegí el día (1: Lunes, 2: Martes): ")
        if not dia.isdigit():      #Validamos que el número del día sea válido
            print("Ingresá un número válido.")
        elif dia != "1" and dia != "2":      #Validamos que el número del día sea válido (1 y o 2)
            print("El día debe ser 1(Lunes) o 2(Martes).")
        else: 
            dia = int(dia)    #Convertimos la opción ingresada (string) a entero.
            paciente = input("Ingrese el nombre del paciente: ")

            while not paciente.isalpha():  #Validamos las opciones con .isalpha.
                print("Error, ingrese un nombre válido solo con letras: ")
                paciente = input("Ingrese el nombre del paciente: ")
            
            
            if dia == 1: 
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:  #Validamos que si el paciente ya tiene turno asignado no pueda generar otro.
                    print("El paciente ya tiene turno ese día.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado correctamente para {paciente} en Lunes.")
                elif lunes2 == "":
                    lunes2 = paciente
                    print(f"Turno reservado para {paciente} en Lunes.")
                elif lunes3 == "":
                    lunes3 = paciente
                    print(f"Turno reservado para {paciente} en Lunes.")
                elif lunes4 == "":
                    lunes4 = paciente
                    print(f"Turno reservado para {paciente} en Lunes.")
                else:
                    print("No hay turnos disponibles en Lunes, intente en Martes.")
            
            
            elif dia == 2:
                if paciente == martes1 or paciente == martes2 or paciente == martes3: #Validamos que si el paciente ya tiene turno asignado no pueda generar otro.
                    print("El paciente ya tiene turno ese día.")
                elif martes1 == "":
                    martes1 = paciente
                    print(f"Turno reservado para {paciente} en Martes.")
                elif martes2 == "":
                    martes2 = paciente
                    print(f"Turno reservado para {paciente} en Martes.")
                elif martes3 == "":
                    martes3 = paciente
                    print(f"Turno reservado para {paciente} en Martes.")
                else:
                    print("No hay turnos disponibles en Martes.")
    elif opcion == 2: 
        dia = input("Elegí el día (1: Lunes, 2: Martes): ")
        if not dia.isdigit():
            print("Ingresá un número válido.")
        elif dia != "1" and dia != "2": 
            print("El día debe ser 1(Lunes) o 2(Martes).")
        else: 
            dia = int(dia)
            paciente = input("Ingrese el nombre del paciente a cancelar: ")

            while not paciente.isalpha():
                print("Error, ingrese un nombre válido solo con letras: ")
                paciente = input("Ingrese el nombre del paciente a cancelar: ")
            if dia == 1:
                if paciente == lunes1:
                    lunes1 = ""
                    print(f"Turno de {paciente} cancelado en Lunes.")
                elif paciente == lunes2:
                    lunes2 = ""
                    print(f"Turno de {paciente} cancelado en Lunes.")
                elif paciente == lunes3:
                    lunes3 = ""
                    print(f"Turno de {paciente} cancelado en Lunes.")
                elif paciente == lunes4:
                    lunes4 = ""
                    print(f"Turno de {paciente} cancelado en Lunes.")
                else:
                    print(f"{paciente} no tiene turno en Lunes.")

            elif dia == 2:
                if paciente == martes1:
                    martes1 = ""
                    print(f"Turno de {paciente} cancelado en Martes.")
                elif paciente == martes2:
                    martes2 = ""
                    print(f"Turno de {paciente} cancelado en Martes.")
                elif paciente == martes3:
                    martes3 = ""
                    print(f"Turno de {paciente} cancelado en Martes.")
                else:
                    print(f"{paciente} no tiene turno en Martes.")  
    elif opcion == 3: 
        dia = input("Elegí el día (1: Lunes, 2: Martes): ")
        if not dia.isdigit():
            print("Ingresá un número válido.")
        elif dia != "1" and dia != "2": 
            print("El día debe ser 1(Lunes) o 2(Martes).")
        else: 
            dia = int(dia)

            if dia == 1:
                print("Agenda Lunes")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")

            if dia == 2:  
                print("Agenda Martes")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")
            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")
            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Día inválido")
    elif opcion == 4:
        print("Resumen general: ") 

        ocupados_dia1 = 0
        if lunes1 != "":
            ocupados_dia1 += 1 
        if lunes2 != "":
            ocupados_dia1 += 1
        if lunes3 != "":
            ocupados_dia1 += 1
        if lunes4 != "":
            ocupados_dia1 += 1
        
        ocupados_dia2 = 0
        if martes1 != "":
            ocupados_dia2 += 1
        if martes2 != "":
            ocupados_dia2 += 1
        if martes3 != "":
            ocupados_dia2 += 1
        
        print(f"Lunes  - Ocupados: {ocupados_dia1} / Disponibles: {4 - ocupados_dia1}")
        print(f"Martes - Ocupados: {ocupados_dia2} / Disponibles: {3 - ocupados_dia2}")
        
        if ocupados_dia1 > ocupados_dia2:
            print("Día con más turnos: Lunes")
        elif ocupados_dia2  > ocupados_dia1:
            print("Día con más turnos: Martes")
        else:
            print("Empate entre Lunes y Martes")

    elif opcion == 5: 
        print("")
        break


#Ejercicio 4

#Definimos todas las variables.

energia = 100    
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
veces_forzadas_seguidas = 0       

nombre_agente = input("Ingrese el nombre del agente: ")

while not nombre_agente.isalpha():     #Validamos el nombre del agente
    print("Error, ingrese un nombre solo con letras: ")
    nombre_agente = input("Ingrese nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:  #El bucle que anidará todo lo demás, mientras todas estas condiciones se cumplan el juego seguirá.
    if alarma == True and tiempo <=3:
        print("Sistema bloqueado por alarma.")
        break
    print(f"\nEnergia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")

    print("\nMENU")
    print()
    print("1. Forzar cerradura (costo: - 20 energia, -2 de tiempo)")
    print("2. Hackear panel (costo: -10 energía, -3 de tiempo)")
    print("3. Descansar (costo: +15 de energía (max 100), -1 de tiempo, si alarma ON -10 de energía extra)")
    print()
    opcion = input("Ingrese una opción: ")

    while not opcion.isdigit():
        print("Ingrese una opción: ")
        continue
    opcion = int(opcion)

    if opcion < 1 or opcion > 3: 
        print("Error, ingrese una opción válida (1-3)")
                            #continue?

    if opcion == 1:  
        print("Forzar cerradura")
        energia -= 20 
        tiempo -= 2
        veces_forzadas_seguidas += 1

        if veces_forzadas_seguidas == 3:     #Validación 
            alarma = True
            print("Se trabó la cerradura! alarma activada.")
        elif energia < 40:
            print("Energía baja! riesgo de alarma.")
            numero = input("Ingresá un número del 1 al 3: ")
            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                print("Ingresá un número válido entre 1 y 3.")
                numero = input("Ingresá un número del 1 al 3: ")
            numero = int(numero)
            if numero == 3:
                alarma = True
                print("¡Alarma activada!")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura abierta. Llevás {cerraduras_abiertas}/3.")
        else:                                  
            cerraduras_abiertas += 1
            print(f"Cerradura forzada. Llevás {cerraduras_abiertas}/3.")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        veces_forzadas_seguidas = 0

        print("Hackeando panel")
        
        for paso in range (1,5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Codigo parcial:{codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"Cerradura abierta. Llevás {cerraduras_abiertas}/3.")
        
    elif opcion == 3:
        tiempo -= 1
        veces_forzadas_seguidas = 0  # cortamos la racha de forzar

        if alarma == True:
            energia -= 10
            print("Alarma activa!")
        else:
            energia += 15
            if energia > 100:
                energia = 100
            print(f"Energía actual: {energia}")

if cerraduras_abiertas == 3:
        print(f"\nVICTORIA! {nombre_agente} abrió la bóveda.")
elif alarma == True and tiempo <= 3:
        print(f"\nDERROTA. Sistema bloqueado por alarma.")
else:
    if energia <= 0:
            print(f"\nDERROTA. {nombre_agente} se quedó sin energía.")
    elif tiempo <= 0:
            print(f"\nDERROTA. {nombre_agente} se quedó sin tiempo.")

        

#Ejercicio 5
#String para el nombre del jugador
#Int para los puntos de vida (HP) y cantidad de pocions
#Float para el cálculo del daño


#Inicializamos todas las variables iniciales
vida_gladiador = 100 
vida_enemigo = 100 
pociones = 3 
daño_base = 15
daño_base_enemigo = 15
turno_gladiador = True

nombre = input("Ingrese el nombre de su Gladiador: ")
while not nombre.isalpha:
    print("Ingrese un nombre solo con letras.")
    nombre = input("Ingrese el nombre de su Gladiador: ")

while vida_gladiador > 0 and vida_enemigo > 0:
    print("\n--- NUEVO TURNO ---")
    print(f"{nombre} ( Vida Gladiador {vida_gladiador}/100 ) | ( Vida Enemigo {vida_enemigo}/100 ) | ( Pociones {pociones}/3)")

    print("\n --- MENU --- ")
    print("1. Ataque pesado")
    print("2. Ráfaga veloz")
    print("3. Curar")

    opcion = input("\nIngrese una opción: ")
    while not opcion.isdigit():
        print("Error, ingrese un número válido")
        opcion = input("Ingrese una opción: ")
    
    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error, ingrese una opción entre 1 y 3")
        opcion = input("Opción: ")
        while not opcion.isdigit():
            print("Error, ingrese un número válido")
            opcion = input("Opción: ")
        opcion = int(opcion)
    
    if opcion == 1: 
        print("1. Ataque pesado")
        if vida_enemigo > 20: 
            daño_final = daño_base * 1.5 
            print(f"GOLPE CRÍTICO!!! Atacaste al enemigo por {daño_final} puntos de daño!")
        else: 
            daño_final = daño_base
            print(f"Atacaste al enemigo por {daño_base} puntos de daño!")

        vida_enemigo -= daño_final

    elif opcion == 2:
        print("2. Ráfaga veloz")
        for daño in range (3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño!")
        print(f"\nVida del enémigo: {vida_enemigo}")
    
    elif opcion == 3:
        print("3. Curar") 
        if pociones > 0:
            vida_gladiador += 30 
            pociones -= 1
            if vida_gladiador > 100:
                vida_gladiador = 100
            print(f"Te curaste, vida actual: {vida_gladiador}/100 | Pociones restantes: {pociones}/3")
        else:
            print("No quedan pociones restantes")

    vida_gladiador -= daño_base_enemigo
    print(f"\nEl enemigo contraataca por {daño_base_enemigo} puntos!")

if vida_gladiador > 0:
    print("\nVICTORIA!!")

else:
    print("\nDERROTA, HAS CAÍDO!")