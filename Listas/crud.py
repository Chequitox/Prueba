

animales=["perro","gato","leon","jirafa"]
opciones=0
running = True

while running:

    print("Mi Zoologico \n")
    print("opciones")
    opciones= int(input("ingresa una opcion: \n1. Agregar\n2.mostar\n3.eliminar por indice\n4.eliminar por nombre\n5.salir\n"))

    if opciones== 1:

        animal= input("ingresa un animal")
        animales.append(animal)

    if opciones == 2:
        print(animales)


    if opciones == 3:
        elimar_index= int(input("ingresa el indice"))
        animales.pop(eliminar_index)

    if opciones == 4:
            eliminar_palabra= input ("ingresa el animal a eliminar: ")
            animales.remove(eliminar_palabra)

    if opciones == 5:
        
        running = False


        print("\n")

