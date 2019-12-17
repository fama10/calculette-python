import os
from addition import *
from soustraction import *
from multiplication import *
from division import *

a= input("Entrer la valeur de a : ")
b= input("Entrer la valeur de b : ")
i= input("Taper la valeur -1, -2, 3, 1 : ")
a = int(a)
b = int(b)
i = int(i)
# test de la fonction calcul
if(i==-1):
    addition(a, b)
if(i==-2):
    soustraction(a,b)
if(i==3):
    multiplication(a*b)
if(i==1):
    division(a,b)
os.system("pause")