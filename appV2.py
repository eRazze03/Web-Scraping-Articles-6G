from src.extraction import *
import pandas as pd
import streamlit as st

articles = grep_articles("6g", 10)
df = pd.DataFrame(articles)
df.to_excel("articles.xlsx")


# Charger les données à partir du fichier Excel
df = pd.read_excel("articles.xlsx")  # On charge le fichier xlsx qui contient les informations sur les articles


# Filtres Sidebar 
st.sidebar.header("Options de filtres : ")
id_filtre = st.sidebar.multiselect("Filtrer les articles que vous souhaitez :", options=df['id'].unique(), default=df['id'].unique())
Annee_filtre = st.sidebar.multiselect("Filtrer les dates :", options=df['Annee'].unique(), default=df['Annee'].unique())

# Application des filtres
donnees_filtres = df[(df["id"].isin(id_filtre)) ]
donnees_filtres = df[(df["Annee"].isin(Annee_filtre)) ]

# Affichage du titre de la page avec Streamlit
st.title("Tableau de bord : Articles sur la 6G")  # Crée un titre principal pour l'application

# Affichage des données filtrées
st.subheader("DataFrame obtenu après l'extraction de 10 articles")
st.write("(Double-cliquer sur une case pour voir tout son contenu)")
st.dataframe(donnees_filtres)   # Affiche le DataFrame sous forme de tableau interactif dans l'application

st.subheader("Exemple de diagramme")
st.write("Diagramme en bâtons montrant le nb d'articles produits par année")

# Création d'un graphique pour visualiser la fréquence des dates de publication
st.bar_chart(df['Annee'].value_counts())  # Crée un graphique à barres qui montre la fréquence de publication des articles

# Footer
st.markdown("---")
st.caption("Prenez nous en stage par pitié !")