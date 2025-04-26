import random as rd
import tkinter as tk
import os.path


TAILLE_CASE = 100
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

score = 0
best_score = 0
liste_carre = []
canvas = None
left_button = None
right_button = None
up_button = None
down_button = None
best_score_label = None
score_label = None

# permet d'initialiser le jeu
def start():
    global score, score_label, best_score, best_score_label, liste_carre, canvas, left_button, right_button, up_button, down_button

    best_score = read_best_score()
    best_score_label.config(text = "Meilleur score : " + str(best_score))

    init_grid()
    get_random_free_cell()["valeur"] = 2
    get_random_free_cell()["valeur"] = 2
    update_grid_labels()

def build_game_interface(fenetre):
    global score_label, best_score_label, canvas, left_button, right_button, up_button, down_button
    canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")

    left_button = tk.Button(fenetre, text="←", fg = "black", font=("Arial","15"), command=gauche)
    right_button = tk.Button(fenetre, text="→", fg = "black", font=("Arial","15"), command=droite)
    up_button = tk.Button(fenetre, text="↑",  fg = "black", font=("Arial","15"), command=haut)
    down_button = tk.Button(fenetre, text="↓", fg = "black", font=("Arial","15"), command=bas)
    
    left_button.place(relx=0.80, rely=0.5, anchor="center")
    right_button.place(relx=0.90, rely=0.5, anchor="center")
    up_button.place(relx=0.85, rely=0.42, anchor="center")
    down_button.place(relx=0.85, rely=0.58, anchor="center")

    # Ajouter le canevas à la fenêtre
    canvas.pack(expand=True)

    best_score_label = tk.Label(fenetre,text="-", font = ("helvetica", "20"))
    best_score_label.pack()
    score_label = tk.Label(fenetre, text="Score : 0", font = ("helvetica", "20"))
    score_label.pack()



# Fonctions de déplacements
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

# permet de mettre à jour les cases 
def update_grid_labels(): 
    for carre in liste_carre:
        if carre["valeur"] < 2:
            carre["label"].config(text = str("") , bg =COULEURS_CASES[0])
        else:
            couleur = COULEURS_CASES.get(carre["valeur"])
            
            texte_couleur = "#776e65"
            carre["label"].config(text = str(carre["valeur"]), bg = couleur,fg=texte_couleur)



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
        print("remplir aléatoirement à 2 ou 4 une case ")
    elif is_game_over():
        game_over()
    if score > best_score:
        best_score = score
        print("new best score")
        write_best_score(best_score)
        best_score_label.config(text = "Meilleur score : " + str(best_score))

    update_grid_labels() #mise à jour d'affichage 
    score_label.config(text = "Score : " + str(score))

#scores management
def read_best_score():
    if os.path.isfile("score")== False:
        return 0
    
    file = open("score","r")
    best_score = int(file.read())
    file.close()
    return best_score

def write_best_score(best_score):
    file = open("score","w")
    file.write(str(best_score))
    file.close()

#affiche partie terminée
def afficher_message_fin():
    msg = tk.Label(canvas, text="Partie terminée !", font=("Arial", 32), fg="red", bg="white")
    msg.place(relx=0.5, rely=0.5, anchor="center")

#verifié les cases pour voir si on peut encore fusionné 
def is_game_over():
    if not is_complete_grid():
        return False

    for y in range(4):
        for x in range(4):
            current_value = liste_carre[x + y * 4]['valeur']
            if x < 3:
                right_value = liste_carre[(x + 1) + y * 4]['valeur']
                if current_value == right_value:
                    return False
            if y < 3:
                down_value = liste_carre[x + (y + 1) * 4]['valeur']
                if current_value == down_value:
                    return False
    return True


#affiche une pop up avec le bouton quitter et la partie est terminée
def game_over():
    def restart():
        global score, score_label, best_score, best_score_label, liste_carre, canvas, left_button, right_button, up_button, down_button

        for case in liste_carre:
            case["valeur"] = 0

        score = 0
        score_label.config(text = "Score : " + str(score))
        get_random_free_cell()["valeur"] = 2
        get_random_free_cell()["valeur"] = 2
        update_grid_labels()
        popup.destroy()

    popup = tk.Toplevel()
    popup.title("Fin de la partie")
    tk.Label(popup, text="Partie terminée !", font=("Helvetica", 20)).pack(padx=20, pady=20)
    tk.Button(popup, text="Rejouer", command=restart).pack(pady=10)

