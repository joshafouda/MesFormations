# **Programme de Formation : Analyses de Données avec SQL et Tableaux de Bord R Shiny pour la Prise de Décisions Commerciales**

## **Introduction**

Bienvenue à notre formation pratique conçue pour aspirants Data Analysts et professionnels. Apprenez à utiliser SQL pour l'analyse exploratoire des données et maîtrisez la création de dashboards interactifs avec R Shiny et Shinydashboard. Ce programme vous guidera à travers chaque étape, de l'analyse de données brutes à la création de visualisations interactives pour des décisions business éclairées.

A travers cette formation, vous apprendrez à :

- Créer une *database* PostgreSQL et utiliser l'interface graphique pgAdmin4 pour une exploration rapide des données ;

- Etablir une connexion entre PostgreSQL et RStudio pour réaliser des analyses avancées ;

- Comprendre et utiliser les requêtes SQL simples et avancées pour extraire et analyser des données afin de répondre à des questions commerciales ;

- Réaliser un Rapport d'analyse exploratoire des données comprenant des tables et graphiques en utilisant RMarkdown ;

- Utiliser le package ***shinydashboard*** pour la construction de tableaux de bords ;

- Structurer correctement un projet de construction de tableau de bord Multi-Menus avec les packages shiny et shinydashboard ;

- Réaliser un tableau de bord interactif pour restituer vos travaux d'analyses Business dans le cadre d'une mission en tant que Consultant(e) Business Intelligence. 


## **Public Cible :**

- Aspirants Data Analysts 

- Professionnels de Business Intelligence souhaitant améliorer leurs compétences

- Toute personne intéressée par l’analyse de données et la création de visualisations interactives

## **Pré-requis :**

Afin de suivre cette formation dans de bonnes conditions, vos devez avoir des :

- Connaissances de base en SQL avec n'importe quel SGBDR (Système de Gestion de Bases de Données Relationnelles) tels que SQLite, MySQL, PostgreSQL, etc. 

- Connaissances de base en programmation avec R (pas obligatoire).

- Notions de base en statistiques descriptives.


## **Module 1: Analyse Exploratoire des Données et Reporting avec SQL et R**

### **Objectif**

Apprendre à exploiter les bases de données pour répondre à des questions business cruciales grâce à SQL (principalement) et R.

### **Contenu**

1. **Introduction à la Problématique Business**

   - Présentation du Scénario

   - Présentation des questions commerciales et des livrables attendus ;

   - Elaboration d'un Document de Conception pour le Rapport d'analyse exploratoire et le Tableau de Bord

2. **Exploration de la Base de Données de la Société de Location de Films**

   - Comprendre la structure de la base de données

   - Introduction aux tables et aux relations

3. **Analyse Exploratoire avec SQL**

   - Filtrer et agréger les données

   - Joindre plusieurs tables pour une analyse approfondie (LEFT JOIN INNER JOIN, etc.)

   - Utilisation des fonctions d'agrégation (SUM, AVG, COUNT, etc.)

   - Groupement et tri des données (GROUP BY, ORDER BY) 

   - Requêtes SQL avancées avec CUBE, ROLLUP, GROUPING SETS, etc.

4. **Études de Cas Business**

   - Analyse des revenus mensuels

   - Identification des meilleurs clients

   - Étude des tendances de location par genre et par pays

5. **Reporting**

   - Rapport de l'analyse aux formats html, pdf et PowerPoint


## **Module 2: Création de Dashboards Interactifs avec Shinydashboard**

### **Objectif:**

Développer des dashboards interactifs et professionnels avec Shiny et Shinydashboard pour des visualisations de données dynamiques.

### **Contenu:**

1. **Introduction à Shiny et Shinydashboard**

   - Concepts de base de Shiny

   - Structure d'une application Shiny

   - Introduction à Shinydashboard

2. **Composants d'un tableau de bord avec shinydashboard**

   - En-tête (Header)

   - Panneau latéral (Sidebar)

   - Partie principal du tableau de bord (Body)

3. **Créez votre premier Tableau de Bord avec shinydashboard**

   - Structurer l'interface Utilisateur (UI)

   - Création des sorties (tables, graphiques) dans la partie serveur

   - Ajoutez des éléments interactifs et dynamiques dans le tableau de bord.

4. **Template d'un Dashboard Multi-Menu**

   - Structurer un projet *.Rproj* pour la construire d'une Multi-App Shiny

   - Construire un template que vous pourrez utiliser dans n'importe quel projet


## **Module 3: Construction d’un Dashboard pour une Société de Location de Films**

### **Objectif:**

Appliquer les compétences acquises pour construire un dashboard complet pour une société de location de films, de l'extraction des données à la visualisation interactive.

### **Contenu:**

1. **Conception du Dashboard**

   - Structurer et organiser le code du projet 

   - Planification des besoins en visualisation et en interactivité

2. **Développement du Dashboard**

   - Intégration des analyses SQL pour extraire les données nécessaires

   - Construction de visualisations Plotly pour les différentes sections (revenus, clients, tendances)

   - Mise en place des filtres et des sélections pour une interactivité utilisateur maximale

3. **Finalisation et Optimisation**

   - Ajout de fonctionnalités avancées (bar charts, scatter plots, pie charts)

   - Optimisation de la performance et de la réactivité du dashboard

   - Conseils et meilleures pratiques pour un code Shiny propre et maintenable

Voici les images de quelques pages du dashboard que vous allez construire :

![](https://github.com/joshafouda/MesFormations/blob/main/assets/menu1.png?raw=true)

![](https://github.com/joshafouda/MesFormations/blob/main/assets/menu2.png?raw=true)

![](https://github.com/joshafouda/MesFormations/blob/main/assets/menu3.png?raw=true)

## Bonus : Projet à réaliser

Pour pratiquer tout ce que vous avez appris lors de cette formation, vous aurez un projet à réaliser. Vous soumettrez votre réalisation à la correction du Formateur afin de recevoir des conseils d'amélioration et de vous débloquer en cas de blocage.

## **Compétences Acquises à l'Issue de la Formation**

À l'issue de cette formation, vous aurez acquis les compétences suivantes :

1. **Maîtrise du SQL pour l'Analyse Exploratoire des Données**

   - Capacité à interroger des bases de données relationnelles pour extraire des informations pertinentes.

   - Compétence dans l'utilisation des fonctions d'agrégation et de groupement pour analyser les données.

   - Aptitude à réaliser des analyses exploratoires pour répondre à des questions business spécifiques.

2. **Création de Dashboards Interactifs avec Shiny et Shinydashboard**

   - Connaissance approfondie de Shiny et de Shinydashboard pour créer des applications web interactives.

   - Compétence dans la conception et la mise en œuvre de dashboards avec une interface utilisateur intuitive.

   - Expertise dans l'intégration de visualisations Plotly pour des graphiques interactifs et dynamiques.

3. **Développement de Dashboards Complets pour des Cas Pratiques**

   - Capacité à structurer et organiser le code pour un projet de dashboard complexe.

   - Compétence dans l'extraction des données nécessaires et la construction de visualisations adaptées.

   - Aptitude à optimiser la performance et la réactivité des dashboards pour une meilleure expérience utilisateur.

4. **Interprétation des Données et Prise de Décisions Éclairées**

   - Capacité à extraire des insights pertinents à partir des données analysées.

   - Compétence dans la création de visualisations interactives qui facilitent la prise de décision.

   - Expertise dans l'analyse des relations entre différentes variables pour identifier les tendances et les comportements clés.

Rejoignez-nous pour cette formation et transformez votre manière d'analyser et de visualiser les données pour des décisions business stratégiques.


## Modalités de Participation à la formation

Cette formation se déroulera en ligne sous forme d'une réunion avec tous les participant(e)s et le Formateur. C'est pour cela, il est très important de povoir disposer d'une bonne connexion Internet. Pour participer :

- S'inscrire en remplissant ce [Formulaire d'inscription](https://forms.gle/oZsH5Er8923jHShWA). Veuillez renseigner une adresse e-mail car c'est sur cette adresse que le lien de la réunion vous sera communiqué.

- Payez les frais de participation en cliquant sur ce [Lien de Paiement sécurisé Stripe](https://buy.stripe.com/fZeaIGaVw4EG80w28u). Les frais de formation doivent être réglés au plus tard 24 heures avant le début de la formation (Le Jour et l'Heure de la formation sont mentionnées dans le formulaire d'inscription).

Après confirmation de votre paiement, vous verrez instantanément le lien de la réunion. Ce lien vous sera également envoyé dans votre boîte Mail.


## **Conclusion**

Cette formation vous fournira les compétences nécessaires pour devenir un Data Analyst efficace, capable d'extraire des insights pertinents des données et de les visualiser de manière interactive pour répondre aux besoins business. Vous serez en mesure de créer des dashboards professionnels qui apporteront une valeur ajoutée significative à toute organisation.

![](https://github.com/joshafouda/MesFormations/blob/main/assets/formation1.png?raw=true)