""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya and Daniel Valencia Cordero
    Mayo 3-2021 
    ulitima modificacion: Mayo 18-2021"""

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular dicvisión: (4)")
  print("==================================================")
   
  opcion = int(input())
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=menu_operaciones()

num1 = int(input("Digite el pimer valor a operar:\n"))
num2 = int(input("DIgite el segundo valor a operar: \n"))
if(operacion == 1):
  print("El resultado de al suma de "+str(num1)+" + "+str(num2)+" es = "+str(calc.sumar_numeros(num1,num2)))
elif(operacion == 2):
  print("El resultado de la resta de "+str(num1)+" - "+str(num2)+" es = "+str(calc.restar_numeros(num1,num2)))
elif(operacion == 3):
  print("El resultado de la multiplicacion de "+str(num1)+" x "+str(num2)+" es = "+str(calc.multiplicar_numeros(num1,num2)))
elif(operacion == 4):
  if(num1 == 0 and num2!=0):
    print("El resultado de la division de "+str(num1)+" / "+str(num2)+" es = 0")
  elif(num2 ==0 and num1!=0):
    print("El resultado de la division de "+str(num1)+" / "+str(num2)+" es = ERROR DIV FOR 0")
  else:
    print("El resultado de la division de "+str(num1)+" / "+str(num2)+" es = "+str(calc.multiplicar_numeros(num1,num2)))
elif(operacion >4 or operacion<1):
  print("Opcion no valida")
