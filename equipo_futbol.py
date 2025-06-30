import funciones_externas as fun;

jugadores = {};

while True:
    print("***** MENU *****");
    print("1) Registrar Jugador");
    print("2) Buscar jugador");
    print("3) Mostrar estado nutricional");
    print("4) Listar equipo completo");
    print("5) Contar jugadores por posición");
    print("6) Salir del sistema");

    try:
        opc = int(input("Ingrese una opción del menu: "));
    except ValueError:
        print("La opcion debe ser un valor numerico de 1 a 6.");

    if(opc == 1):
        rut = input("Ingrese su numero de rut (12345678-k): ");

        if(rut in jugadores):
            print("El jugador ya se encuentra registrado!");
        else:
            nombre = input("Ingrese el nombre del jugador: ");

            try:
                peso = float(input("Ingrese el peso del jugador en kilos: "));
                if(peso <= 0):
                    raise ValueError;

                altura = float(input("Ingrese el altura del jugador en metros: "));
                if(altura <= 0):
                    raise ValueError;                

            except ValueError:
                print("El peso y la altura deben ser valores numericos positivos.");
                continue

            try:
                posicion = int(input("Posición dentro del equipo: (1.Arquero - 2.Defensa - 3.Medio Campo - 4.Delantero): ")); 

                if(posicion not in [1,2,3,4]):
                    raise ValueError;

            except ValueError:
                print("La posición del jugador solo puede ser un valor numerico del 1 al 4.");
                continue

            # agregar jugador al diccionario
            jugadores[rut] = {
                "nombre": nombre,
                "peso": peso,
                "altura": altura,
                "posicion": posicion
            };

            print("Jugador ingresado exitosamente!");

    elif(opc == 2):
        rut = input("Ingrese el rut del jugador a buscar: ");
        fun.buscar_jugador(rut, jugadores);

    elif(opc == 3):
        rut = input("Ingrese el rut del jugador a buscar: ");
        fun.estado_nutricional(rut, jugadores);

    elif(opc == 4):
        for clave, valor in jugadores.items():
            print(f"Rut: {clave} - Nombre: {valor["nombre"]}, Peso: {valor["peso"]}, Altura: {valor["altura"]}, posicion: {fun.validar_posicion(valor["posicion"])}")
        

    elif(opc == 5):
        conteo = {1: 0, 2: 0, 3: 0, 4: 0};

        for valor in jugadores.values():
            posicion = valor["posicion"];

            if(posicion in conteo):
                if(posicion == 1):
                    conteo[posicion] += 1;
                elif(posicion == 2):
                    conteo[posicion] += 1;
                elif(posicion == 3):
                    conteo[posicion] += 1;
                elif(posicion == 4):
                    conteo[posicion] += 1;

        for posicion in conteo:
            print(f"Posicion: {fun.validar_posicion(posicion)} = {conteo[posicion]}");

    elif(opc == 6):
        break

    else:
        print("Opcion invalida!");



        
