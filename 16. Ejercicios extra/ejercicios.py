

def longitud(array):
    cont =0
    for i in array:
        cont += 1
    return cont

def vocal(letra):
    letras = ['a','e','i','o','u']
    if letra in letras:
        return True
    return False

def sum(nums):
    suma =0
    for i in nums:
        suma += i
    return suma

def mul(nums):
    mul =1
    for i in nums:
        mul = mul * i
    return mul

def inversa(str):
    return str[::-1]

def palindromo(str):
    if str == str[::-1]:
        return True
    return False

def leap_year(year):
    if year%4 ==0 and (year%100!=0  or year%400==0):
        return True 
    return False

def superpos(nums1, nums2):
    for i in nums1:
        for j in nums2:
            if i == j:
                return True
    return False

def generar_n_caracteres(n,str):
    return str*n

def procedimiento(array):
    for i in array:
        print (i * '*')


print(procedimiento([1, 2, 3, 4]))



