#Punto1

diccionario ={"Guatemala" : "Ciudad de Guatemala", "El Salvador" : "San Salvador",
"Honduras": "Honduras", "Nicaragua": "Managua", "Costa Rica": "San Jose",
"Panama" : "Panama", "Argentina" : "Buenos aires", "Colombia": "Bogota",
"Venezuela" : "Caracas", "España": "Madrid"}

pais = input("Nombre del pais: ")



if pais in diccionario:
    print("Capital del Pais: ",diccionario.get(pais))
else:
    print("No se encuentra el pais")
