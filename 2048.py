## JEU 2048 ##

#Djessim Bouiche
#Gabriel Levy
#Yacine Boulachgour
#Namsai Souvanthong

#### MODULES / BIBLIOTHEQUES 

import tkinter as tk
import random as rd

taille_case = 100

#### PARTIE INTERFACE #####

import tkinter as tk




fenetre = tk.Tk()
fenetre.title('2048')
label_title = tk.Label(fenetre, text = "2048", font = ("Arial", 20), bg = "#df9d97", fg = "white")
label_title.pack()

fenetre.geometry("800x800") 


canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")

taille_case = 100
liste_carre = []
liste_carre_disponible = []

def draw(): 
    """Dessiner le carré avec des dimensions de taille_casextaille_case pixels pour chaque case"""
    for i in range(4):
        for j in range(4):
            carre = canvas.create_rectangle(i*taille_case, j*taille_case, (i+1)*taille_case, (j+1)*taille_case)
            liste_carre.append(canvas.coords(carre))

# Boutons
left_button = tk.Button(fenetre, text="←", fg = "black", font=("Arial","15"))  #command=gauche
right_button = tk.Button(fenetre, text="→", fg = "black", font=("Arial","15")) #command=droite
up_button = tk.Button(fenetre, text="↑",  fg = "black", font=("Arial","15")) #command=haut
down_button = tk.Button(fenetre, text="↓", fg = "black", font=("Arial","15"))#command=bas

def gauche():
    return

def droite():
    return

def haut():
    return

def bas():
    return

left_button.place(relx=0.80, rely=0.5, anchor="center")   # command = gauche
right_button.place(relx=0.90, rely=0.5, anchor="center")  # command = droite
up_button.place(relx=0.85, rely=0.42, anchor="center")    # command = haut
down_button.place(relx=0.85, rely=0.58, anchor="center")  #command = bas


draw() #appelle la fonction qui dessine les cases

# Ajouter le canevas à la fenêtre
canvas.pack(expand=True)

liste_carre_disponible = [[i,j,0] for i in range(4) for j in range(4)]



fenetre.mainloop()
