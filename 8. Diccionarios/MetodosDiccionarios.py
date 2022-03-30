diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5, 6 : 7}
print(diccionario)

'''diccionario.pop(3) #Elimina una clave dada
print(diccionario)

diccionario.clear() #Elimina todo el diccionario
print(diccionario)'''

print(diccionario.get(2))

diccionario.setdefault(4 , 5)
print(diccionario)

diccionario.update(diccionario2)
print(diccionario)

diccionario.copy()
print(diccionario)