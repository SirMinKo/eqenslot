# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:23:44 2019

@author: MinKo
@Mineko
"""

import time, random, sys

# Variables----------------------------------------------------------

nivel = 1
exp = 0
expmax = 100

#Inventario:

dinero = 20
cobre= 0
plata=0
oro=0
diamante=0

#Herramientas

pico = True
rifle = True

# -------------------------------------------------------------------



#Selector de opciones------------------------------------------------

def selector():
    opc = input("Deseo... ")
    print (" ")
    if opc == "stats":
        stats()
    elif opc == "minar":
        mineria()
        
    elif opc == "exit":
        exit
        
    elif opc == "tienda":
        tienda()
        
    elif opc == "comandos":
        print("stats/minar/cazar/tienda/exit")
        print ("OP: exp/money")
        selector()
        
    elif opc == "cazar":
        caza()
        
    elif opc =="exp":
        OPexp()
        
    elif opc =="money":
        OPmoney()
        
    else: 
        print ("No se puede reconocer ese comando, vuelve a intentarlo")
        
        selector()
    
#Checkear Nivel--------------------------------------------------------
        
def checklevel():
    global exp
    global nivel
    global expmax
    while exp>expmax:
        exp = exp-100
        nivel = nivel+1
        expmax = expmax + 100*nivel
        print ("¡Enhorabuena! Has subido al nivel: ", nivel)
        
    
#Stats-----------------------------------------------------------------
     
def stats():
    print (" ")
    print ("Nivel: ",nivel)
    print ("Experiencia: ",exp,"/",expmax)
    print ("Inventario:")
    print ("Tienes: ",dinero,"$")
    print ("Minerales:",cobre,"pieza/s de cobre", 
           plata,"pieza/s de plata", oro,"pieza/s de oro", diamante, "pieza/s de diamante")  
    
    selector()

#Mineria---------------------------------------------------------------

def mineria():
    global exp
    global nivel
    global cobre
    global plata
    global oro
    global diamante
    global pico
    if pico is False:
        print ("Minero: ¡Necesitas un pico para minar aquí muchacho!")
        print ("Minero: Seguro que en la tienda pueden ayudarte")
        selector()
    else:
        print ("Minando", end="")
        time.sleep(random.randint(0, 1))
        print (".", end="")
        time.sleep(random.randint(0, 1))
        print (".", end="")
        time.sleep(random.randint(0, 1))
        print (".")
        mineral = random.randint(0,95)
        if mineral < 60:
            print ("¡Has encontrado cobre!, ganas 1 punto de experiencia")
            exp = exp+50
            cobre = cobre+1
            checklevel()
        elif mineral >60 and mineral<80:
            print ("¡Has encontrado plata!, ganas 3 puntos de experiencia")
            exp = exp+3
            plata = plata+1
            checklevel()
        elif mineral >80 and mineral<90:
            print ("¡Has encontrado oro!, ganas 5 puntos de experiencia")
            exp = exp+5
            oro = oro+1
            checklevel()
        elif mineral >90:
            print ("¡Has encontrado diamante!, ganas 10 puntos de experiencia")
            exp = exp+10
            diamante = diamante+1
            checklevel()
        selector()
    
#Caza---------------------------------------------------------------------

def caza():
    print ("El silencio sepulcral del bosque te da la bienvenida")
    if rifle is False:
        print ("¡¿Estás loco?! ¡No puedes venir al bosque desarmado!")
        selector()
    else:
        print ("Buscando una presa", end="")
        time.sleep(2)
        print (".", end="")
        time.sleep(2)
        print (".", end="")
        time.sleep(2)
        print (".", end="")
        time.sleep(2)
        print (".")
        caza = random.randint(1, 10)
        if caza <6:
            print ("No se ha encontrado ningún animal")
            selector()
        else: 
            print ("¡Has encontrado un ciervo! ¿Quieres intentar cazarlo o huir? (d/h)")
            caza = input()
            if caza == "d":
                 print ("Apuntando", end="")
                 time.sleep(2)
                 print (".", end="")
                 time.sleep(2)
                 print (".", end="")
                 time.sleep(2)
                 print (".")
                 print ("¡Fuego!")
                 
        
        
    
#Tienda----------------------------------------------------------------------    

def tienda():
    global exp
    global nivel
    global cobre
    global plata
    global oro
    global diamante
    global pico
    global dinero
    print ("Tendero: ¡Bienvenido a la tienda!")
    tienda = input("Tendero: ¿Qué deseas? ¿Comprar o vender? (c/v) ")
    if tienda == "c":
        print ("Tendero: Dime, ¿Qué te interesa?")
        print ("pico: 5$, rifle de caza: 120$")
        comprar = input()
        if comprar == "pico":
            if pico is False:
                print ("Tendero: ¡Gracias! ¡Vuelve Pronto!")
                pico = True
                dinero = dinero-5
            else:
                print ("Tendero: ya tienes un pico")
                selector()
        else:
            print ("Tendero: Lo siento chico, no te he entendido")
        selector()
        
#Vender:
        
    elif tienda == "v":
        print ("Tendero: ¿Qué tienes para mi?")
        vender = input("(cobre/plata/oro/diamante)")
        cantidad = int(input())
        
    else: 
        print ("¿Cómo? no te he entendido")
        tienda()

#OPexp---------------------------------------------------------------------

def OPexp():
    global exp
    opexp= int(input("Puntos de experiencia:"))
    print ("Puntos de experiencia adquiridos")
    exp = exp+opexp
    checklevel()
    selector()
#OPmoney----------------------------------------------------------------------
    
def OPmoney():
    global dinero
    opmoney= int(input("$"))
    print ("Dinero adquirido")
    dinero = dinero+opmoney
    selector()
    
    
print ("¡Bienvenido a Mineko 1.0 Alpha!")
selector()