while True:
    num = int(input("ingrese un numero (0 para salir):"))
    
    if num ==0:
        print("programa terminado")
        break
    elif num % 2 != 0:
        continue
    print("numero par",num)
