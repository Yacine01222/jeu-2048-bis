## JEU 2048 ##

#Djessim Bouiche
#Yacine Boulachgour

#### MODULES / BIBLIOTHEQUES 
import tkinter as tk
import random as rd
import tkinter as tk
import os.path

TAILLE_CASE = 100


def gauche():
    global score 
    for y in range(4):
        for x in range(3): #fusion
            valeur = liste_carre[x + y * 4]['valeur']
            if valeur > 0:
                x2 = x + 1
                while x2 < 4 and liste_carre[x2 + y * 4]['valeur'] == 0: x2 += 1
                if x2 < 4 and liste_carre[x2 + y * 4]['valeur'] == valeur:
                    liste_carre[x + y * 4]['valeur'] *= 2
                    liste_carre[x2 + y * 4]['valeur'] = 0
                    score += valeur

        for _ in range(3):
            for x in range(3, 0, -1):
                actuel_id, voisine_id = x + y * 4, x + y * 4 - 1
                if liste_carre[voisine_id]['valeur'] == 0:
                    liste_carre[voisine_id]['valeur'] = liste_carre[actuel_id]['valeur']
                    liste_carre[actuel_id]['valeur'] = 0

    turn()


def droite():
    global score 
    for y in range(4):
        for x in range(3, 0, -1): #fusion
            valeur = liste_carre[x + y * 4]['valeur']
            if valeur > 0:
                x2 = x - 1
                while x2 > -1 and liste_carre[x2 + y * 4]['valeur'] == 0: x2 -= 1
                if x2 > -1 and liste_carre[x2 + y * 4]['valeur'] == valeur:
                    liste_carre[x + y * 4]['valeur'] *= 2
                    liste_carre[x2 + y * 4]['valeur'] = 0
                    score += valeur

        for _ in range(3):
            for x in range(3): #glissement
                actuel_id, voisine_id = x + y * 4, x + y * 4 + 1
                if liste_carre[voisine_id]['valeur'] == 0:
                    liste_carre[voisine_id]['valeur'] = liste_carre[actuel_id]['valeur']
                    liste_carre[actuel_id]['valeur'] = 0
    turn()
        
def haut():
    global score 
    for x in range(4):
        for y in range(3): #fusion
            valeur = liste_carre[x + y * 4]['valeur']
            if valeur > 0:
                y2 = y + 1
                while y2 < 4 and liste_carre[x + y2 * 4]['valeur'] == 0: y2 += 1
                if y2 < 4 and liste_carre[x + y2 * 4]['valeur'] == valeur:
                    liste_carre[x + y * 4]['valeur'] *= 2
                    liste_carre[x + y2 * 4]['valeur'] = 0
                    score += valeur

        for _ in range(3):
            for y in range(3, 0, -1): #glissement
                actuel_id, voisine_id = x + y * 4, x + (y - 1) * 4
                if liste_carre[voisine_id]['valeur'] == 0:
                    liste_carre[voisine_id]['valeur'] = liste_carre[actuel_id]['valeur']
                    liste_carre[actuel_id]['valeur'] = 0

    turn() 



def bas():
    global score 
    for x in range(4):
        for y in range(3, 0, -1): #fusion
            valeur = liste_carre[x + y * 4]['valeur']
            if valeur > 0:
                y2 = y - 1
                while y2 > -1 and liste_carre[x + y2 * 4]['valeur'] == 0: y2 -= 1
                if y2 > -1 and liste_carre[x + y2 * 4]['valeur'] == valeur:
                    liste_carre[x + y * 4]['valeur'] *= 2
                    liste_carre[x + y2 * 4]['valeur'] = 0
                    score += valeur

        for _ in range(3):
            for y in range(3): #glissement
                actuel_id, voisine_id = x + y * 4, x + (y + 1) * 4
                if liste_carre[voisine_id]['valeur'] == 0:
                    liste_carre[voisine_id]['valeur'] = liste_carre[actuel_id]['valeur']
                    liste_carre[actuel_id]['valeur'] = 0
    turn()

# Choisir de manière aléatoire une case vide 
def get_random_free_cell():
    case_libre = []
    for carre in liste_carre:
        if carre["valeur"]==0:
            case_libre.append(carre)
    
    return case_libre[rd.randint(0, len(case_libre) - 1)]


# permet de vérifier si toutes les cases sont remplies 
def is_complete_grid() -> bool:
    for carre in liste_carre:
        if carre["valeur"] == 0:
            return False
        
    return True

COULEURS_CASES = {
    0: "#d2c8a3",    
    2: "#e2d9b1",   
    4: "#e2d1a1",   
    8: "#f1a764",    
    16: "#f48750",   
    32: "#f75f50",   
    64: "#f75c32",   
    128: "#e0ca5e", 
    256: "#e0c34f",  
    512: "#e0b444",  
    1024: "#e0a030",
    2048: "#e08c1f", 
  
}


# permet de mettre à jour les cases 
def update_labels(): 
    for carre in liste_carre:
        if carre["valeur"] < 2:
            carre["label"].config(text = str("") , bg =COULEURS_CASES[0])
        else:
            couleur = COULEURS_CASES.get(carre["valeur"])
            
            texte_couleur = "#776e65"
            carre["label"].config(text = str(carre["valeur"]), bg = couleur,fg=texte_couleur)

# permet d'initialiser le jeu
def start():
    init_grid()
    get_random_free_cell()["valeur"] = 2
    get_random_free_cell()["valeur"] = 2
    update_labels()

# permet de générer la grille
def init_grid():
    """Dessiner le carré avec des dimensions de taille_case*taille_case pixels pour chaque case"""
    for y in range(4):
        for x in range(4):
            canvas.create_rectangle(x * TAILLE_CASE, y * TAILLE_CASE, (y+1) * TAILLE_CASE, (x+1) * TAILLE_CASE)
            text_carre = tk.Label(canvas, font = ("Arial",64),fg = "white")
            liste_carre.append({
                "valeur": 0,
                "label": text_carre
            })
            text_carre.place(x=x * TAILLE_CASE + 1, y=y * TAILLE_CASE + 1, width=TAILLE_CASE -2 , height=TAILLE_CASE -2)


#effectue un tour de jeux 
def turn():
    global best_score
    if is_complete_grid() == False:
        get_random_free_cell()["valeur"] = 2 if rd.randint(0,100) < 90  else 4
    elif score > best_score:
        best_score = score
        write_best_score(best_score)
        best_score_label.config(text = "Meilleur Score : " + str(best_score))
    update_labels() #mise à jour d'affichage 
    score_label.config(text = "Score : " + str(score))



def read_best_score():
    if os.path.isfile("score")== False:
        return 0
    file = open("score","r")
    score = int(file.read())
    file.close()
    return score


def write_best_score(score):
    file = open("score","w")
    file.write(str(score))
    file.close()



#Initailisation du score
score = 0
best_score = read_best_score()




fenetre = tk.Tk()
fenetre.title('2048')
label_title = tk.Label(fenetre, text = "2048", font = ("Arial", 20), bg = "#df9d97", fg = "white")
label_title.pack()

fenetre.geometry("800x800") 


canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")
liste_carre = []

# Boutons
left_button = tk.Button(fenetre, text="←", fg = "black", font=("Arial","15"),command= gauche)
right_button = tk.Button(fenetre, text="→", fg = "black", font=("Arial","15"),command = droite)
up_button = tk.Button(fenetre, text="↑",  fg = "black", font=("Arial","15"),command=haut)
down_button = tk.Button(fenetre, text="↓", fg = "black", font=("Arial","15"),command=bas)

left_button.place(relx=0.80, rely=0.5, anchor="center")
right_button.place(relx=0.90, rely=0.5, anchor="center")
up_button.place(relx=0.85, rely=0.42, anchor="center")
down_button.place(relx=0.85, rely=0.58, anchor="center")

# Ajouter le canevas à la fenêtre
canvas.pack(expand=True)

#afficher label score 

best_score_label = tk.Label(fenetre,text="Meilleur Score : " + str(best_score), font = ("helvetica", "20"))
best_score_label.pack()
score_label = tk.Label(fenetre, text="Score : " + str(score), font = ("helvetica", "20"))
score_label.pack()
start()

fenetre.mainloop()

