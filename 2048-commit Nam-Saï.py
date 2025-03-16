#couleur des cases
colors = {
        2: "#EDE7DC",   # Beige doux
        4: "#ECE0C8",   # Crème
        8: "#F4A261",   # Orange pâle
        16: "#F68C5F",  # Orange plus foncé
        32: "#F76E4E",  # Rouge-orangé
        64: "#F65032",  # Rouge vif
        128: "#E8C35C", # Jaune doré
        256: "#E8B94A", # Jaune plus foncé
        512: "#E8AE3D", # Jaune orangé
        1024: "#E89C20", # Or
        2048: "#E88C0E", # Doré intense
        4096: "#3D3A33", # Gris foncé (valeurs élevées)
        8192: "#2C2B25",
        }

def ajouter_nouvelle_tuile():
    """Ajoute une nouvelle tuile (2 ou 4) à une position vide dans la grille."""
    cases_vides = [(ligne, colonne) for ligne in range(TAILLE_GRILLE) for colonne in range(TAILLE_GRILLE) if grille[ligne][colonne] == 0]
    if cases_vides:
        ligne, colonne = random.choice(cases_vides)
        grille[ligne][colonne] = random.choice([2, 4])

dessiner_gridlle()



