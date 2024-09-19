print("Clases V2 Ever Pereyra")
# Zona de clase
class Datos: 
    # El constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso 
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} kg")
    def mi_lista(self):
        albumes=["SKR","aztlan","roncanlover"]
        print(albumes)
        for a in albumes:
            print(a)
    def mi_tupla(self):
        caricaturas = ("Bob_Esponja","Gravity_Falls","Muchalucha")
        print(caricaturas)
        for c in caricaturas:
            print(c)
    def mi_conjunto(self):
        JuegosM = {"GTA","DOOM","Call_of_Duty"}        
        print(JuegosM)
        for j in JuegosM:
            print(j)
    def mi_diccionario(self):
        calificaciones = {
            "Quimica": 9,
            "Inglés": 10,
            "Matematicas": 8  
        }
        print(calificaciones)
        for cal1,cal2 in calificaciones.items():
            print(cal1, cal2)
# Creación de objeto
info=Datos(1.78,110.7)

# Utilizando  el obj.
info.mostrar_datos()
print("Lista de Albumes Ever Pereyra")
info.mi_lista()
print("Tupla de caricaturas Ever Pereyra")
info.mi_tupla()
print("Conjunto de juegos clasificación M Ever Pereyra")
info.mi_conjunto()
print("Diccionario de calificaciones Ever Pereyra")
info.mi_diccionario()

