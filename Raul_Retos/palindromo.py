def es_palindromo(palabra):
   
    palabra = palabra.replace(" ", "").lower()
    
    if palabra == palabra[::-1]:
        return True
    else:
        return False
        
palabra_usuario = input("Por favor, ingresa una palabra: ")

if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' es un palíndromo.")
else:
    print(f"'{palabra_usuario}' no es un palíndromo.")
