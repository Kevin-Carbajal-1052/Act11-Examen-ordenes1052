class ordenes1052:
    id_ordenes07=0
    id_clientes07=0
    fecha_de_orden07=""
    total07=0
    estado07=""
    fecha_de_envio07=""
    direccion_envio07=""

    #Zona de funciones

    def mostrardatos(self):
        print("---Mostrando datos---")
        print(f"El id de la orden es: {self.id_ordenes07}")
        print(f"El id del cliente es: {self.id_clientes07}")
        print(f"La fecha de la orden es: {self.fecha_de_orden07}")
        print(f"El total es: {self.total07}")
        print(f"El estado de los productos es: {self.estado07}")
        print(f"La fecha de envio es: {self.fecha_de_envio07}")
        print(f"La direccion de envio es: {self.direccion_envio07}\n")

    def listar_ordenes(self):
        print("---Lista de ordenes---")
        listaordenes=["Manga de kny", "Traje de nezuko","espada de zenitsu","Funko pop","Figura de accion\n"]
        for x in listaordenes:
            print(x)
    
    def tupla_ordenes(self):
        print("---Tupla de ordenes---")
        tuplaordenes=("Manga de kny", "Traje de nezuko","espada de zenitsu","Funko pop","Figura de accion\n")
        for x in tuplaordenes:
            print(x)

    def diccionario_ordenes(self):
        print("---Diccionario de ordenes---")
        dicordenes={"Manga de kny":"Tomo 21",
                    "Traje de nezuko":"Talla L",
                    "espada de zenitsu":"Acero inoxidable",
                    "Funko pop":"Tengen Uzui",
                    "Figura de accion":"Kanroji Mitsuri\n"}
        for x,y in dicordenes.items():
            print(x,y)
    
    def altas(self):
        print("---ALTAS---")
        print("La orden a sido pedida con exito\n")
    
    def bajas(self):
        print("---BAJAS---")
        print("La orden no se pudo completar\n")
    
#Zona creacion de objetos
obj=ordenes1052()
obj.id_ordenes07=7
obj.id_clientes07=1045
obj.fecha_de_orden07="23/Sep/2024"
obj.total07=10000
obj.estado07="Nuevo"
obj.fecha_de_envio07="26/Sep/2024"
obj.direccion_envio07="Henequen #9534-3"

#Llamada a las funciones
obj.mostrardatos()
obj.listar_ordenes()
obj.tupla_ordenes()
obj.diccionario_ordenes()
obj.altas()
obj.bajas()