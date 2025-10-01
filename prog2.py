def promedio_ajustado(codigo, nota1, nota2, nota3, nota4, nota5):

    notas = [nota1, nota2, nota3, nota4, nota5]
    notas.remove(min(notas))   
    promedio = sum(notas) / len(notas)
    promedio = round(promedio, 2)
    
    return f"El promedio ajustado del estudiante {codigo} es: {promedio}"

def menu():
    while True:
        print("\n MENU ")
        print("1. Calcular promedio ajustado")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            
            codigo = input("Ingrese el codigo del estudiante: ")
            print("Ingrese las 5 notas de los quices (en escala de 0 a 5):")
            try:
                n1 = int(input("Nota 1: "))
                n2 = int(input("Nota 2: "))
                n3 = int(input("Nota 3: "))
                n4 = int(input("Nota 4: "))
                n5 = int(input("Nota 5: "))
            except ValueError:
                print("Error: Debe ingresar valores numericos enteros")
                continue

            resultado = promedio_ajustado(codigo, n1, n2, n3, n4, n5)
            print(resultado)

        elif opcion == "2":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida, intente de nuevo")

menu()
