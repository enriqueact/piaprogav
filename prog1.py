import datetime

class Empleado:
    def __init__(self, nombre, sueldo, departamento, fecha_ingreso):
        self.nombre = nombre
        self.sueldo = sueldo
        self.departamento = departamento
        self.fecha_ingreso = fecha_ingreso

    def imprimir_ticket(self):
        print("\n")
        print("       TICKET EMPLEADO")
        print("")
        print("Nombre:        ", self.nombre)
        print("Sueldo:        $", self.sueldo)
        print("Departamento:  ", self.departamento)
        print("Fecha ingreso: ", self.fecha_ingreso.strftime("%d/%m/%Y"))
        print("----------------------------")

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")



empleados = []


departamentos = {
    1: "Recursos Humanos",
    2: "Sistemas",
    3: "Contabilidad",
    4: "Ventas",
    5: "Produccion"
}


def registrar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = float(input("Ingrese el sueldo: "))

    print("\nDepartamentos disponibles:")
    for clave, valor in departamentos.items():
        print(clave, ".", valor)
    depto = int(input("Seleccione el numero del departamento: "))
    departamento = departamentos.get(depto, "No asignado")

    
    fecha_ingreso = datetime.datetime.now()

    nuevo_empleado = Empleado(nombre, sueldo, departamento, fecha_ingreso)
    empleados.append(nuevo_empleado)
    print("Empleado registrado con exito\n")


def mostrar_empleados():
    if not empleados:
        print("No hay empleados registrados\n")
    else:
        for emp in empleados:
            emp.imprimir_ticket()


def menu():
    while True:
        print("\nMENU ")
        print("1. Registrar empleado")
        print("2. Mostrar empleados")
        print("3. Revisar impuestos")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            if not empleados:
                print("No hay empleados registrados\n")
            else:
                for emp in empleados:
                    print("Empleado:", emp.nombre, "->", end=" ")
                    emp.paga_impuestos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

menu()
