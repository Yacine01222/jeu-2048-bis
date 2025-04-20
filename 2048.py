## JEU 2048 ##

#Djessim Bouiche
#Yacine Boulachgour

#### MODULES / BIBLIOTHEQUES 
import tkinter as tk
import game


#Initailisation du score
fenetre = tk.Tk()
fenetre.title('2048')

label_title = tk.Label(fenetre, text = "2048", font = ("Arial", 20), bg = "#df9d97", fg = "white")
label_title.pack()

fenetre.geometry("800x800")

game.build_game_interface(fenetre)
game.start()


fenetre.mainloop()

