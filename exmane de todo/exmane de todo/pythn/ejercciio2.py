#ejercicio 2 infrmacin de una caden de extirnwenfo



def contar_mayu_minus (frase):
    if  isinstance(frase, str):

        minus = 0
        mayus = 0
         
        for c in frase:
           
           if c.isalpha():

            if c.islower():
                minus += 1
            elif c.isupper():
                mayus += 1
                
    return minus, mayus
    raise TypeError
    raise("no")
    
frase = "LOs ojo"
resultado = contar_mayu_minus(frase)

print(f"en la frase hay {resultado[0]} minusculas y {resultado[1]} mayusulas ")

