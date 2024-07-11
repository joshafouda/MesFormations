import streamlit as st


# --- HERO SECTION ---
col1, col2 = st.columns(2, vertical_alignment="center")
with col1:
    st.image("assets/linkedin_profil.png", width=500)
with col2:
    st.title("Josué AFOUDA", anchor=False)
    st.markdown("""
#### Data Scientist Senior, accompagnant les entreprises dans la prise de décisions basées sur l'analyse et la moélisations des données ainsi que le développement de *Data Products*.

Passionné par l'analyse de données, je suis spécilaiste dans la DataViz, l'Apprentissage Automatique, la construction d'applications Data Science et l'automatisation des processus. 

Mon parcours professionnel inclut des rôles variés tels que Data Scientist, Développeur R & R Shiny, Data Analyst, Machine Learning Engineer et Développeur Python pour de grandes entreprises. 

Je suis également passionné par le partage du savoir, ce qui m'a conduit à créer une chaîne YouTube : [JADATATECHCONSULTING](https://www.youtube.com/c/JADATATECHCONSULTING). Les professionnels et passionnés de data peuvent aussi me retrouver sur LinkedIn : [Josué Afouda](https://www.linkedin.com/in/josué-afouda).

En dehors de la data, je suis très heureux dans ma vie de père de famille avec ma femme et mon petit garçon. J'adore voyager et aller au cinéma, ce qui me permet de maintenir un bon équilibre entre vie professionnelle et personnelle.
""")
    

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
exp_col, skills_col = st.columns(2)

with exp_col:
    st.subheader("Expérience & Qualifications", anchor=False)
    st.write(
        """
        - Plus de 10 ans d'expériences en Analyse des données
        - Expertise pratique solide et connaissances approfondies de Python, R et SQL
        - Expertise en Développement et Déploiement d'applications orientées DATA
        - Expertise en Automatisation et Optimisation des Processus Métier 
        - Excellent esprit d'équipe et grande autonomie dans la gestion des Projets
        """
    )

with skills_col:
    st.subheader("Compétences Techniques", anchor=False)
    st.write(
        """
        - Programmation : Python (Scikit-learn, Pandas, PySpark, ...), R (Tidyverse, Sparklyr, ...), SQL
        - Visualisation des données : R Shiny, ggplot2, Plotly, Tableau, PowerBI
        - Modélisation : Machine Learning, Deep Learning, modèles de séries temporelles
        - Bases de données : PostgreSQL, Oracle, MongoDB, MySQL. InfluxDB
        - Développement Web, APIs et Cloud : Streamlit, Flask, FastAPI, Azure, Databricks
        """
    )