#Hacer un funcion que Lea un número entero de cuatro dígitos(+) y que la funcion retorne
#cuántos dígitos pares tiene.

def ContarPares(num :int) -> int :
    r1 = r2 = r3 = c1 = c2 = c3 = 0
    ContP = 0
    if num >= 1000 and num <= 9999 :
        r1 = num % 10
        c1 = num // 10
        r2 = c1 % 10
        c2 = c1 // 10
        r3  = c2 % 10
        c3 = c2 // 10
        if r1 % 2 == 0 : 
            ContP = ContP +  1
        if r2 % 2 == 0 : 
            ContP = ContP +  1
        if r3 % 2 == 0 : 
            ContP = ContP +  1
        if c3 % 2 == 0 : 
            ContP = ContP +  1
    else :
        return "Fuera rango"  

    return(ContP)

num = int(input("Digite numero  "))

print("Cantidad de digitos pares = " ,ContarPares(num))
