secreto =7 
while True:
    numero = int(input("aduvina el numero:"))
    if numero == secreto:
        print("acertaste al numero,!FELICIDADES¡")
        break
    elif numero < secreto:
        print("num muy bajo")
    else:
        print("numero muy alto")    
