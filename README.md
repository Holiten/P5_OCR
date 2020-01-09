___
### PUR BEURRE
___
###### *Project 5 - OpenClassRoom - DA Python*
___
*Work in progress*

![PUR BEURRE](https://static.passeportsante.net/i85826-.jpeg)
___
#### Fonctionnalités :

+ Recherche d'aliments dans la base [Open Food Fact](https://fr.openfoodfacts.org/)
    * Récuperation des données via un script
    * Creation d'une bdd (si celle ci n'existe pas) via un script
+ Interraction de l'utilisateur via le terminal ou interface graphique
+ Gestion des erreurs (mauvais input)
+ Recherche via SQL
+ Enregistrement (via un systeme de user & bdd)
---
#### User stories :

##### __*Accueil*__

* Creer un nouveau profil
* Se connecter 
* Nouvelle recherche
* Voir mes recherches enregistrées (nécessite un compte)
* Quitter
    
##### __*Creer un nouveau profil*__

* Information a entrer par l'utilisateur 
    * Input -- Nom d'utilisateur (pas de chiffre, pas de caractéres spéciaux)
    * Input -- Mail
    * Input -- Mot de passe 
    * Input -- Valider -- Y or N (gestion des erreurs) (Retour à l'acceuil aprés Y)
    * Retour à l'accueil

##### __*Se connecter*__

* Nom d'utilisateur
* Mot de passe
* Retour à l'accueil

##### __*Nouvelle recherche*__

* Choix de la catégorie (Parmis 5 max.)
    * Catégorie N°1
        * Aliment N°1 --- Substitut + Description + Magasin + lien vers Open Food Fact
        * Etc...
    * Catégorie N°2
        * Aliment N°1 --- Substitut + Description + Magasin + lien vers Open Food Fact
        * Etc...
    * Catégorie N°3
        * Aliment N°1 --- Substitut + Description + Magasin + lien vers Open Food Fact
        * Etc...
    * Catégorie N°4
        * Aliment N°1 --- Substitut + Description + Magasin + lien vers Open Food Fact
        * Etc...
    * Catégorie N°5
        * Aliment N°1 --- Substitut + Description + Magasin + lien vers Open Food Fact
        * Etc...

##### __*Voir mes recherches enregistrées (nécessite un compte)*__

* Recherche(s) enregistrée(s)
    * Recherche 1
    * Etc...
    
##### __*Quitter*__

* Fermeture du programme

---
#### Idées diverses (libs) :

Relation SQL <> Python :
* Lib Sqlite3
* mysql-connector

Recupération des données d'Open Fact Food :
* Scrappy (récup de données HTML en JSON)
* requests (requetes sur API en JSON)
* json (Encodage et décodage fichier JSON)
---
#### Versions :
* _Version 1.1 - 09/01/2020 - Oliten : Ajout "Idées diverses" & "Versions"_ 
* _Version 1.0 - 09/01/2020 - Oliten : Premiére diffusion_ 