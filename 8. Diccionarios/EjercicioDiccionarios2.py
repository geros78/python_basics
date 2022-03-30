diccionario = {1: "Casillas", 15: "Ramos", 3: "Pique", 5: "Puyol", 
11: "Capdevila", 14: "Xabi Alonso", 16: "Busquets", 8: "Xavi Hernandez",
18: "Pedrito", 6: "Inista", 7: "Villa"}

numero = int(input("Numero del jugador: "))

if numero in diccionario:
     print("Nombre del jugador:",diccionario.get(numero))
else:
     print("No es un numero dentro del diccionario")