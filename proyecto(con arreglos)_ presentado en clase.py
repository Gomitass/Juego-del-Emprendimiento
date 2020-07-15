pregunta1=input("¿Crees tener lo necesario para emprender?, si/no: ")
if pregunta1=="si":
  pass
else:
  print("No te preocupes, lo puedes hacer")
print()
pregunta2=input("¿Sabes cómo emprender?, si/no: ")
if pregunta2=="si":
  pass
else:
  print("No pasa nada, aquí podemos aprender")

print()
print("Aquí te daremos algunos tips para ser un emprendedor.")
print()                                  
print("1. Domina tu mercado.")
print("2. Elabora un plan de negocios.")
print("3. Define quién es tu cliente.") 
print("4. Escucha a tus futuros compradores.")
print("5. Analiza a tu competencia.")                            
print("6. Invierte en tecnología.")                               
print("7. Busca asesoría y capacitación.")    
print()                                                      
print()
print("El siguiente juego consiste en la creación de una empresa, la cual vas a empezar desde cero con un presupuesto inicial. La idea es que lo administres de la mejor manera, haciendo crecer tu empresa de la mejor manera y evitando la quiebra.")
print()

import os
#Diccionarios en uso
terminar=False

datos_b={"Dinero en posesión": 8000.0, "Comprar Máquinas": 1000,"Gastos de Máquina por mes":30,"Dinero obtenido por Máquina": 250, "Paga Empleado":10,"Empleados requeridos por Máquina": 10}
maq_emp={"Maquinas totales": 0, "Empleados totales": 0}

datos_rb=datos_b.copy()
maq_empp=maq_emp.copy()

def empleado():
  empleadostu=(maq_emp.get("Maquinas totales")* datos_b.get("Empleados requeridos por Máquina"))
  maq_emp["Empleados totales"]=empleadostu

#Función para imprimir dinero y ganancias pr maquina

def tabla_b():
  for key in datos_b:
    print (key, ":", datos_b[key])

#Función de calculo de ganancias + aumento o reducción de dinero en posesión
def ganancias():
  global ganancias_t
  ganancias_t= maq_emp.get("Maquinas totales")* (datos_b.get("Dinero obtenido por Máquina") - datos_b.get("Gastos de Máquina por mes")) - maq_emp.get("Empleados totales")* datos_b.get("Paga Empleado")
  print("Tu posible ganancia total a obtener :",ganancias_t)


def sumganan():
  datos_b["Dinero en posesión"]= datos_b["Dinero en posesión"] + ganancias_t
  
  
#Función para mostrar preguntas
#listas y diccionarios a usar
#cambios=["inversion","aumentoacomprar", "aumentodinero", "aumentopaga", "aumentoepleados"]
  
preguntas=["\nUn auto estrelló la fachada la empresa(-400).\nPresiona a,b,c o d para seguir.","\nTe han llegado varias propuestas para mejorar la producción de tus dispositivos y tienes que decidir si quieres o no aplicar alguna de estas propuestas.\na) No aplicar ninguna propuesta.\nb) Modernizar maquinaria con nuevas tecnologías (costo de inversión 2000) ( + 20 producción por máquina) ( + 60 compra de máquinas).\nc) Cambiar toda la maquinaria por nueva y más productora (costo de inversión 1100 por máquina) (+100 producción por máquina) (+ 300 por compra de máquina) (+ 3 empleados más por máquina).\nd) Añadir a las máquina un nuevo dispositivo capaz de aumentar producción (costo de inversión 50 por máquina) (+ 10 de producción por máquina) (+50 por compra de máquinas)","\nTus empleados están pidiendo un aumento de paga debido a que piensan que están sobrecargados, un estudio que realizaste demuestra que en efecto tienen sobrecarga, ¿que vas a hacer?.\na) Nada, seguir como vamos.\nb) aumentar el salario a los empleados en 2.\nc) aumentar el salario a los empleados en 5.\nd) Dar 1 hora más de descanso a los empleados.","\nTu esposa termino contigo y se llevó un tercio de tus ganancias totales.\nPresiona a,b,c o d para seguir.","La planta de energía de la empresa se averió y si no la arreglas no se podrá continuar con la producción.(-4000).\nPresiona a,b,c o d para seguir.","\n¿Quieres cambiar las máquinas a operar con tres empleados más? su inversión es 1200 y aumenta tu producción de máquina en 20.\n a) Sí \nb) No\nc) No \nd) No","\nHas sido estafado con dos máquinas, el reemplazo te salió caro(-3000).\nPresiona a,b,c o d para seguir."]

contador=0
#Función que muestra la pregunta y arregla en lista soluciones
def pregunta():
  global contador
  a=[[400,0,0,0,0],[0,0,0,0,0],[0,0,-40,0,0,],[(datos_b.get("Dinero en posesión")/2),0,0,0,0],[4000,0,0,0,0],[1200,0,20,0,3],[3000,0,0,0,0]]
  b=[[400,0,0,0,0,],[2000,60,20,0,0],[0,0,0,2,0],[(datos_b.get("Dinero en posesión")/2),0,0,0,0],[4000,0,0,0,0],[0,0,0,0,0],[3000,0,0,0,0]]
  c=[[400,0,0,0,0],[(1100* maq_emp.get("Maquinas totales")),300,100,0,3],[0,0,0,5,0],[(datos_b.get("Dinero en posesión")/2),0,0,0,0],[4000,0,0,0,0],[0,0,0,0,0],[3000,0,0,0,0]]
  d=[[400,0,0,0,0],[(50* maq_emp.get("Maquinas totales")),50,10,0,0],[0,0,-20,0,0],[(datos_b.get("Dinero en posesión")/2),0,0,0,0],[4000,0,0,0,0],[0,0,0,0,0],[3000,0,0,0,0]]
  global cambios
  cambios=[]
  print (preguntas[contador])
  solucion=input("Marca tu respuesta //: ")
  if solucion=="a":
    for i in a[contador]:
      cambios.append(i)
  elif solucion=="b":
    for i in b[contador]:
      cambios.append(i)
  elif solucion=="c":
    for i in c[contador]:
      cambios.append(i)
  elif solucion=="d":
    for i in d[contador]:
      cambios.append(i)
  else:
    print()
    print("solución no valida vuelve a intentar")
    print()
    pregunta()
  contador=contador+1
  print()

#aplicación de las consecuencias de las preguntas
def consecuencia():
  datos_b["Dinero en posesión"]=datos_b["Dinero en posesión"] - cambios[0]
  datos_b["Comprar Máquinas"]=datos_b["Comprar Máquinas"] + cambios[1]
  datos_b["Dinero obtenido por Máquina"]=datos_b["Dinero obtenido por Máquina"] + cambios[2]
  datos_b["Paga Empleado"]=datos_b["Paga Empleado"] + cambios[3]
  datos_b["Empleados requeridos por Máquina"]=datos_b["Empleados requeridos por Máquina"] + cambios[4]



#primera pregunta
preguntai="\n¿cuántos máquinas y empleados piensas conseguir?:\na) 8 máquinas con 80 empleados\nb) 5 máquinas con 50 empleados\nc) 2 máquinas con 20 empleados"

o=(8, 80)
p=(5,50)
q=(2,20)

def primerp():
  print(preguntai)
  solauno=input("Marca tu respuesta //: ")
  if solauno=="a":
    maq_emp["Maquinas totales"]=maq_emp["Maquinas totales"]+ o[0] 
    maq_emp["Empleados totales"]=maq_emp["Empleados totales"]+ o[1]
    datos_b["Dinero en posesión"]=datos_b["Dinero en posesión"] - (o[0]* datos_b.get("Comprar Máquinas"))
  elif solauno=="b":
    maq_emp["Maquinas totales"]=maq_emp["Maquinas totales"]+ p[0] 
    maq_emp["Empleados totales"]=maq_emp["Empleados totales"]+ p[1]
    datos_b["Dinero en posesión"]=datos_b["Dinero en posesión"] - (p[0]* datos_b.get("Comprar Máquinas"))
  elif solauno=="c":
    maq_emp["Maquinas totales"]=maq_emp["Maquinas totales"]+ q[0] 
    maq_emp["Empleados totales"]=maq_emp["Empleados totales"]+ q[1]
    datos_b["Dinero en posesión"]=datos_b["Dinero en posesión"] - (q[0]* datos_b.get("Comprar Máquinas"))
  else:
    print()
    print("solución no valida vuelve a intentar")
    print()
    primerp()

#pregunta repetitiva
preguntac="preguntac"

def pregrep():
  print("\nPon el numero de maquinas que quieres comprar, si no quieres comprar ninguna pon 0")
  masmaqui=int(input("Marca tu respuesta //: "))
  maq_emp["Maquinas totales"]=maq_emp["Maquinas totales"]+ masmaqui 
  datos_b["Dinero en posesión"]=datos_b["Dinero en posesión"] - (masmaqui* datos_b.get("Comprar Máquinas"))

def inicios():  
  tabla_b() 
  ganancias()
  print() 
  primerp()
  print()
  sumganan()
  tabla_b()
  ganancias()
  print (maq_emp)
  print()
  wait=input("presiona una tecla para continuar.")
  os.system ("clear")
  print()
  sumganan()
  tabla_b()
  print (maq_emp)

def repetp():
  global terminar
  if terminar:
    return
  pregrep()
  print()
  tabla_b()
  empleado()
  ganancias()
  print (maq_emp)
  print()
  wait=input("Presiona una tecla para continuar.")
  os.system ("clear")
  if datos_b.get("Dinero en posesión")<0:
    print("Pagaste más de lo que tenías. Pierdes por bancarrota.")
    terminar=True
  else:
    sumganan()
    tabla_b()
    print (maq_emp)


def mpregunta():
  global terminar
  if terminar:
    return
  pregunta()
  consecuencia()
  tabla_b()
  empleado()
  ganancias()
  print (maq_emp)
  wait=input("Presiona una tecla para continuar.")
  os.system ("clear")
  if datos_b.get("Dinero en posesión")<0:
    print("Pagaste más de lo que tenías. Pierdes por bancarrota.")
    terminar=True
  else:
    sumganan()
    tabla_b()
    print (maq_emp)

def preguntasra():
  repetp()
  repetp()
  repetp()

def cuadra():
  mpregunta()
  preguntasra()

def repetidera():
  print("si quieres volver a intentar escribe (si), si no escribe (no)")
  repetid=input("//: ")
  global datos_b
  global maq_emp
  global terminar
  global contador
  if repetid=="si":
    terminar=False
    datos_b=datos_rb.copy()
    maq_emp=maq_empp.copy()
    contador=0


while terminar==False :
  inicios()
  repetp()
  for  i in range(7):
    cuadra()
  repetidera()