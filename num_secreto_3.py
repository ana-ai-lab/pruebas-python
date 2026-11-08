numerosecreto = 7
intentos = 3
adivinado = False
print("¡Bienvenido al juego del número secreto!(limite de intentos: 3)")
# El bucle while se ejecutará mientras el número de intentos sea mayor que 0 y el número no haya sido adivinado
while not adivinado and intentos > 0:
    # Se solicita al usuario que ingrese un número
    numero = int(input("Ingresa un número entre 1 y 10: "))
    # Se verifica si el número ingresado es igual al número secreto
    if numero == numerosecreto:
        adivinado = True
        print("¡Felicidades! Has adivinado el número secreto.")
    elif numero < numerosecreto:
        print("¡Casi! El número secreto es mayor.")
        intentos -=1    #restamos un intento por fallar
    else:
        print("¡Casi! El número secreto es menor.")
        intentos -= 1   #restamos un intento por fallar
        print(f"¡Incorrecto! Te quedan {intentos} intentos.")
# Mensaje final si se agotaron los intentos sin acertar
if not adivinado:
    print(f"\n¡Se agotaron los intentos! El número secreto era {numerosecreto}. ❌")

print("¡Gracias por jugar!")


