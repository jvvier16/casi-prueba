import os
import csv
import time

nombre = []
cargo =[]
sueldo_b= []
descu_salu = []
desc_afp = []
sueldo_liquio = []

while True:
    os.system('cls')
    print("""
            1.regristrar trebajador
            2.lista de los trabajadores
            3.imprimir plantilla de sueldo
            4.salir del programa""")
    
    opc = int(input("que opcion desea usar:"))

    if opc >=1 and opc <=4:
        
        if opc == 1:
            nombre1= input("ingrese nombre del trabajador:")
            nombre.append(nombre1)
            pocision = input("ingrese su pocision:")
            cargo.append(pocision)
            sueldob = int(input("ingrese su sueldo bruto porfavor:"))
            if sueldob<=10000 :
                sueldo_b.append(sueldob)
                desc_salu = sueldob*0.07
                descu_salu.append(desc_salu)
                descu_afpc = sueldob*0.12
                desc_afp.append(descu_afpc)
                descu_total = descu_afpc + desc_salu
                sueldo_final = sueldob - descu_total
                sueldo_liquio.append(sueldo_final)
            else:
                print("sueldo debe ser mayor a 10.000 pesos ")

        elif opc ==2:

            print("nombre del trabajador:",nombre)
            print("cargo del trabajador:",cargo)
            print("sueldo bruto del trabajador:",sueldo_b)
            print("descuento de la salud del trabajador es:",descu_salu)
            print("descuento de la afp para el trabajador es:",desc_afp)
            print("su sueldo liquido es:",sueldo_liquio)
            time.sleep(4)

        elif opc ==3:
            pass
        
        else:
            print("gracias por usarnos")
            break
    
    else:
        print("opcion incorrecta vuelve a intentarlo")