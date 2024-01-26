# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:33:09 2024

@author: i50031073
"""

import pandas as pd
import os
from fonctions_projet_python import * #lancer la première partie du code avant

# Charger les données depuis le fichier Excel
fichier_xlsx = "male_players.xlsx"  
data = pd.read_excel(fichier_xlsx)

# Définir les points de coupure pour répartir également les joueurs
points_de_coupe = [0, data['Overall'].quantile(0.25), data['Overall'].quantile(0.5),
                   data['Overall'].quantile(0.75), float('inf')]

# Classer les joueurs en fonction de leur classement général
data['Catégorie'] = pd.cut(data['Overall'], bins=points_de_coupe,
                           labels=['Facile', 'Moyen', 'Difficile', 'Expert'], right=False)

# Sauvegarder le résultat dans un nouveau fichier Excel
nouveau_fichier_excel = "male_players_triés.xlsx"  # Remplacez cela par le chemin réel de votre nouveau fichier Excel
data.to_excel(nouveau_fichier_excel, index=False)

print("Les joueurs ont été classés avec succès.")

# Charger les données depuis le fichier CSV
fichier_xlsx = "male_players_triés.xlsx"  
data = pd.read_excel(fichier_xlsx)

# Trier les positions en fonction des blocs

bloc_gardien = ['GK']
bloc_defensif = ['LH', 'SW','RH','RB','LB','LCB','CB','CH','RCB','LWB','RWB','WB']
bloc_milieu = ['DM','CDM','LW','LM','CAM','CM','M','RM','RW','AMR','WF','AML','AMC','AM']
bloc_offensif = ['LS','RS','LF','SS','RF','ST','CF']

# Ajouter une colonne 'Blocs' en fonction de la position

data['Blocs'] = data['Position'].apply(lambda x: 
                                        'Defense' if x in bloc_defensif 
                                        else ('Milieu' if x in bloc_milieu 
                                              else ('Attaque' if x in bloc_offensif
                                                    else 'Gardien')))


data_sorted = data.sort_values(by=['Blocs', 'Position'])

# Enregistrer la DataFrame triée
data.to_excel("male_players_triés.xlsx", index=False)

print("Les joueurs ont été triés par blocs.")


# Test de la fonction qui donne un nom aléatoire d'un des 100 meilleurs joueurs en fonction de la catégorie et du bloc
caracteristiques_par_blocs = {
    'Gardien': ['Jumping','Defending','Standing','Physicality'],
    'Defense': ['Defending', 'Heading', 'Strength', 'Stamina', 'Jumping', 'Strength', 'Sliding', 'Standing', 'Physicality'],
    'Milieu': ['Interceptions', 'Vision', 'Dribbling', 'Passing', 'Pace', 'Crossing', 'Stamina', 'Aggression', 'Agility'],
    'Attaque': ['Positioning', 'Penalties', 'Vision', 'Agility', 'Aggression', 'Dribbling', 'Passing', 'Shooting', 'Acceleration', 'Finishing']
}


# 'Facile', 'Moyen', 'Difficile', 'Expert' sont les catégories possibles
# 'Gardien', 'Defense', 'Milieu' et 'Attaque' sont les blocs possibles

nom_joueur_aleatoire = generer_top_joueurs(data, 'Expert', 'Gardien', caracteristiques_par_blocs)

# Afficher le nom du joueur aléatoire
print(f"Nom du joueur aléatoire - Catégorie: Expert, Bloc: Gardien: {nom_joueur_aleatoire}")




        
