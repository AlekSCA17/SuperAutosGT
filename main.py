class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio_unitario): # init es nuestro constructor que inicializa los atributos de la clase Auto

        self.placa = placa 
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

    def __str__(self): #srt nos va devolver en cadena del objeto Auto, mostrando sus atributos
        return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: Q{self.precio_unitario:.2f}, Descripción: {self.descripcion}"


class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, NIT: {self.nit}"


class Compra:
    contador_id = 0 #Contador estático que nos asignara un ID único para cada compra

    def __init__(self, cliente):
        Compra.contador_id += 1
        self.id = Compra.contador_id
        self.cliente = cliente
        self.lista_productos = []
        self.costo_total = 0.0

    def agregar_auto(self, auto):
        self.lista_productos.append(auto)
        self.costo_total += auto.precio_unitario

    def facturar(self, agregar_seguro):
        if agregar_seguro:
            self.costo_total *= 1.15

    def __str__(self):
        productos = "\n".join([str(auto) for auto in self.lista_productos])
        return f"ID: {self.id}, Cliente: {self.cliente}\nAutos Adquiridos:\n{productos}\nCosto Total: Q{self.costo_total:.2f}"


class SistemaInventario:
    def __init__(self):
        self.autos = []
        self.clientes = []
        self.compras = []

    def registrar_auto(self):
        placa = input("Escribe la placa del auto: ")
        marca = input("Escribe la marca del auto: ")
        modelo = input("Escribe el modelo del auto: ")
        descripcion = input("Escribe la descripción del auto: ")
        precio = float(input("Escribe el precio del auto en quetzales: "))
        auto = Auto(placa, marca, modelo, descripcion, precio)
        self.autos.append(auto)
        print("El auto a sido registrado con exito")

    def registrar_cliente(self):
        nombre = input("Escribe el nombre del cliente: ")
        correo = input("Escribe el correo electrónico del cliente: ")
        nit = input("Escribe el NIT del cliente: ")
        cliente = Cliente(nombre, correo, nit)
        self.clientes.append(cliente)
        print("El cliente a sido registrado con exito")

    def realizar_compra(self):
        nit = input("Escribe el NIT del cliente que esta realizando la compra: ")
        cliente = next((c for c in self.clientes if c.nit == nit), None)
        if not cliente:
            print("El cliente no a sido encontrado.")
            return

        compra = Compra(cliente)

        while True:
            print("------------- Menú Compra -------------")
            print("1. Agregar Auto")
            print("2. Terminar Compra y Facturar")
            print("---------------------------------------")
            opcion = input("Ingresa una opción: ")

            if opcion == "1":
                placa = input("Escribe la placa del auto a comprar: ")
                auto = next((a for a in self.autos if a.placa == placa), None)
                if auto:
                    compra.agregar_auto(auto)
                    print("Tu auto a sido agregado en tu compra.")
                else:
                    print("El auto no a podido ser encontrado.")
            elif opcion == "2":
                agregar_seguro = input("¿Quieres agregar seguro al auto? (si/no): ").strip().lower() == "si"
                compra.facturar(agregar_seguro)
                self.compras.append(compra)
                print("Tu compra se realizo con éxito.")
                break

    def reporte_compras(self):
        print("------------- REPORTE DE COMPRAS -------------")
        total_general = 0.0
        for compra in self.compras:
            print(compra)
            total_general += compra.costo_total
            print("==============================================")
        print(f"Tu total es: Q{total_general:.2f}")
        print("---------------------------------------------")

    def mostrar_datos_estudiante(self):
        print("Nombre: Brayan Alexander Guzman Margos")
        print("Carnet: 202105658")

    def menu_principal(self):
        while True:
            print("------------- Super Autos GT -------------")
            print("1. Registrar Auto")
            print("2. Registrar Cliente")
            print("3. Realizar Compra")
            print("4. Reporte de Compras")
            print("5. Datos del Estudiante")
            print("6. Salir")
            print("------------------------------------------")
            opcion = input("Ingresa una opcion: ")

            if opcion == "1":
                self.registrar_auto()
            elif opcion == "2":
                self.registrar_cliente()
            elif opcion == "3":
                self.realizar_compra()
            elif opcion == "4":
                self.reporte_compras()
            elif opcion == "5":
                self.mostrar_datos_estudiante()
            elif opcion == "6":
                print("Hasta Pronto :D")
                break
            else:
                print("La opcion que ingresas no es valida, vuelve a intentar")


if __name__ == "__main__":
    sistema = SistemaInventario()
    sistema.menu_principal()