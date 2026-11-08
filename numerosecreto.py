numero_secreto = 7
adivinado = False

print("=== Juego de Adivinanza en Python ===")

# Este bucle se encarga de pedir el número y evaluarlo repetidamente
while not adivinado:
    intento = int(input("Introduce tu número (1-10): "))
    
    if intento == numero_secreto:
        print("¡Excelente! Has acertado el número secreto 🎉")
        adivinado = True  # Al cambiar a True, el bucle termina
    elif intento < numero_secreto:
        print("Pista: El número secreto es MAYOR. ¡Inténtalo de nuevo!")
    else:
        print("Pista: El número secreto es MENOR. ¡Inténtalo de nuevo!")

print("¡Gracias por jugar!")

