## JEU 2048 ##

# Djessim Bouiche
# Yacine Boulachgour

#### MODULES / BIBLIOTHEQUES 
import tkinter as tk
import game

def afficher_page_accueil(fenetre):
    page_accueil = tk.Frame(fenetre, bg="#FFC300")
    page_accueil.pack(expand=True, fill="both")

    label_title = tk.Label(page_accueil, text="2048", font=("Arial", 40, "bold"), bg="#FFC300", fg="white")
    label_title.pack(pady=50)

    bouton_jouer = tk.Button(page_accueil, text="Jouer", font=("Helvetica", 18), width=20,bg="#4CAF50", fg="white",command=lambda: lancer_jeu(fenetre, page_accueil))
    bouton_jouer.pack(pady=10)

    bouton_best = tk.Button(page_accueil, text="Meilleur Score", font=("Helvetica", 18), width=20,command=afficher_best_score_popup)
    bouton_best.pack(pady=10)

    bouton_quitter = tk.Button(page_accueil, text="Quitter", font=("Helvetica", 18), width=20,bg="#f44336", fg="white", command=fenetre.destroy)
    bouton_quitter.pack(pady=10)

def afficher_best_score_popup():
    score = game.read_best_score()
    popup = tk.Toplevel()
    popup.title("Meilleur Score")
    tk.Label(popup, text="Meilleur score : " + str(score), font=("Helvetica", 16)).pack(padx=20, pady=20)
    tk.Button(popup, text="Fermer", command=popup.destroy).pack(pady=10)

def lancer_jeu(fenetre, page_accueil):
    page_accueil.destroy()
    game.build_game_interface(fenetre)
    game.start()
    fenetre.bind("<Left>", lambda event: game.gauche())
    fenetre.bind("<Right>", lambda event: game.droite())
    fenetre.bind("<Up>", lambda event: game.haut())
    fenetre.bind("<Down>", lambda event: game.bas())

fenetre = tk.Tk()
fenetre.title('2048')
fenetre.geometry("800x800")

afficher_page_accueil(fenetre)

fenetre.mainloop()
