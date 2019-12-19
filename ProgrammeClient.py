import socket


hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

    
a = input("Entrer la valeur de a :")
b = input("Entrer la valeur de b :")
op = input("Entrer l'opération : ")
    # Peut planter si vous tapez des caractères spéciaux
    
    # On envoie le message
a = a.encode()
b = b.encode()
op = op.encode()

connexion_avec_serveur.send(a)
connexion_avec_serveur.send(b)   
connexion_avec_serveur.send(op)   

valeurfinal_recu = connexion_avec_serveur.recv(1024)


print("la valeur du calcul de" , a.decode() ,"+", b.decode() ,"=",valeurfinal_recu.decode())

print("Fermeture de la connexion")
connexion_avec_serveur.close()