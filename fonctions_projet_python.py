# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:34:26 2024

@author: i50031073
"""

import numpy as np
import pandas as pd
import os

# Charger les données depuis le fichier CSV
fichier_xlsx = "male_players_triés.xlsx"  
data = pd.read_excel(fichier_xlsx)

"Le but de ces fonctions est de déterminer le meilleur joueur dans chaque catégorie et dans chaque position"


# Caractéristiques attribuées à chaque bloc

caracteristiques_par_blocs = {
    'Gardien': ['Jumping','Defending','Standing','Physicality'],
    'Defense': ['Defending', 'Heading', 'Strength', 'Standing Tackle', 'Stamina',  'Strength', 'Sliding', 'Standing','Physicality'], 
    'Milieu': ['Interceptions','Vision', 'Dribbling', 'Passing', 'Pace', 'Crossing', 'Stamina','Agression','Agility'], 
    'Attaque': ['Positioning','Penalties','Vision', 'Agility', 'Aggression','Dribbling', 'Passing', 'Shooting','Acceleration', 'Finishing']
}


# Fonction pour trouver  les 100 meilleurs joueurs par blocs et générer un parmi eux de manière aléatoire

        
def generer_top_joueurs(data, categorie, blocs, caracteristiques_par_blocs, n_top=100):
    categorie_data = data[data['Catégorie'] == categorie]
    blocs_data = categorie_data[categorie_data['Blocs'] == blocs]
    caracteristiques = caracteristiques_par_blocs[blocs]

    # Ajouter une colonne 'Score' en calculant la somme des caractéristiques pour chaque joueur
    blocs_data['Score'] = blocs_data[caracteristiques].sum(axis=1)

    # Générer une liste aléatoire des indices des 100 meilleurs joueurs
    top_indices = blocs_data.nlargest(n_top, 'Score').index.tolist()

    # Sélectionner un indice aléatoire parmi les 100 meilleurs joueurs
    indice_aleatoire = np.random.choice(top_indices)

    # Récupérer le nom du joueur correspondant à l'indice aléatoire
    nom_joueur_aleatoire = blocs_data.loc[indice_aleatoire, 'Name']

    return nom_joueur_aleatoire





