import socket
import math
import os
from addition import *
from soustraction import *

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

   
msg_recu1 = int(connexion_avec_client.recv(1024))
msg_recu2 = int(connexion_avec_client.recv(1024))
msg_recu3 = connexion_avec_client.recv(1024).decode()
    
if msg_recu3 =="+":
    valeurfinal_recu = addition(msg_recu1,msg_recu2)       
    print("la valeur de l'Addition de " , msg_recu1, " +" ,msg_recu2,"= " ,valeurfinal_recu)
    connexion_avec_client.send(str(valeurfinal_recu).encode())

if msg_recu3 =="-":
    valeurfinal_recu = Soustraction(msg_recu1,msg_recu2)       
    print("la valeur de Soustraction de " , msg_recu1, " +" ,msg_recu2,"= " ,valeurfinal_recu)
    connexion_avec_client.send(str(valeurfinal_recu).encode())

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()