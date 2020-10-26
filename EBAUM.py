n1= float(input("Nota Bach I\n "))
n2= float(input("Nota Bach II\n "))
n3= float(input("Nota Fase General\n "))
n4= float (input("Nota Fase Especifica\n "))
Nota1=(((n1+n2)/2)*0.6)+(n3*0.4)+(n4*0.2)
Nota2=(((n1+n2)/2)*0.6)+(n3*0.4)
aprobado=5
if n4 >= aprobado:
    print(str(Nota1))
else:
    print(str(Nota2))

        

