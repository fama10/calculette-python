import os
from addition import *
from soustraction import *
from multiplication import *
from division import *

a= input("Entrer la valeur de a : ")
b= input("Entrer la valeur de b : ")
i= input("Taper le signe de l'opération : ")
a = int(a)
b = int(b)

# test de la fonction calcul
if(i== "+"):
    resultat = addition(a, b)
if(i=="-"):
    resultat = soustraction(a,b)
if(i=="*"):
    resultat = multiplication(a*b)
if(i=="/"):
    resultat = division(a,b)
print("le resultat de l'operation est :", resultat)
