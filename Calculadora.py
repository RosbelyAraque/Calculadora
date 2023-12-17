print("Bienvenido a la Calculadora")
k='s'
while k=='s' :
    #Solicitar el primer numero
    n1=int(input("Introduzca el primer número (entre 40 y 200): "))
    #validar que este en el rango correcto
    while n1<40 or n1>200 :
        n1=int(input("Número fuera de rango, (entre 40 y 200), intente de nuevo: "))
        #Solicitar el segundo numero
    n2=int(input("Introduzca el segundo número (entre 40 y 200): "))
    while n2<40 or n2>200 :
        n2=int(input("Número fuera de rango, (entre 40 y 200), intente de nuevo: "))
        #Mostrar opciones
    print("¿Qué desea hacer:")
    print("1_Sumar")
    print("2_Restar")
    print("3_Multiplicar")
    print("4_Dividir")
    print("Selecione una opción: ")
    i=int(input())
    while i<1 or i>4 :
        print("Escogió la opción incorrecta, vuelva a intentarlo.")
        i=int (input())
    if i==1 :
        suma=n1+n2
        print("La suma es: ",suma)
    elif i==2 :
        resta=n1-n2
        print("La resta de n1-n2 es: ",resta)
    elif i==3 :
        pro=n1*n2
        print("El producto es: ",pro)
    elif i==4 :
        div=n1/n2
        print("La división de n1/n2 es: ",div)
    print("¿Desea continuar? Sí <s> , No <n>")
    k=input()
          



