#Punto 1 

letra =input("Escribe una letra: ")

'''if letra.lower() == "a"  or  letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() =="u":
    print("Es una vocal")
else:
    print("No es una vocal")'''

#-------------------------------------

if letra.lower() in "aeiou":
    print("es una vocal")
else:
    print("No es una vocal")

#Punto 2

num = int(input("Escribe un numero: "))

if num >= 0:
    print("El valor absoluto de {} es {}".format(num,num))
else:
    print("El valor absoluto de {} es {}".format(num, abs(num)))