___
### PUR BEURRE
___
###### *Project 5 - OpenClassRoom - DA Python*
___

![PUR BEURRE](https://static.passeportsante.net/i85826-.jpeg)
___
#### Requirements :
* Python 3 ([installation](https://www.python.org/downloads/release/python-382/))
* SQL Database & connexion SQL server (like [XAMPP](https://www.apachefriends.org/fr/index.html))
___
#### Lancement du programme :
* [Download](https://github.com/Holiten/P5_OCR) le repo github
* Installation des packages (pip install -r requirements.txt)
* Lancer le programme (python main.py)
___
#### Fonctionnalités :

+ Recherche d'aliments dans la base [Open Food Fact](https://fr.openfoodfacts.org/)
    * Récuperation des données via un script
    * Creation d'une bdd (si celle ci n'existe pas) via un script
+ Interraction de l'utilisateur via le terminal ou interface graphique (amélioration future)
+ Gestion des erreurs (mauvais input)
+ Recherche via SQL
+ Enregistrement
---
#### User stories :

##### __*Démarrage du programme*__

* User1 lance le programme pour la premiere fois :
    * Creation de la bdd
    * Creation des tables de la bdd
    * Récupération des données de l'API Open Food Fact
    * Insertion des données dans la bdd
    * Accés au menu principal
    
* User2 a deja utilisé le programme :
    * Vérification de la bdd et des données
    * Accés au menu principal

##### __*Menu principal (3 propositions)*__

* User1 choisi de remplacé un produit :
    * User1 choisit une catégories parmit celles proposées
    * User1 choisit un produit parmit ceux de la catégorie choisie
    * User1 Sauvegarde son choix et son produit substituant
    * User1 choisit de revenir au menu principal ou de quitter le programme
    
* User2 choisi de consulter ses produits sauvegardés :
    * User2 consulte ses produits sauvegardés et revient au menu principal
    
* User3 choisit de quitter le programme
    * User3 ferme le programme

___
#### Versions :
* _Version 2.1 - 11/03/2020 - Oliten : Final version_
* _Version 2.0 - 09/03/2020 - Oliten : Nouvelle branche (Pour POO)_
* _Version 1.5 - 24/02/2020 - Oliten : Pre final version_
* _Version 1.4 - 10/02/2020 - Oliten : Code Optimisation & suppresion function inutiles_
* _Version 1.3 - 06/02/2020 - Oliten : PEP8 Optimisation_
* _Version 1.2.1 - 06/02/2020 - Oliten : Mise à jour suivant mentor_ 
* _Version 1.2 - 13/01/2020 - Oliten : Mise à jour suivant mentor_ 
* _Version 1.1 - 09/01/2020 - Oliten : Ajout "Idées diverses" & "Versions"_ 
* _Version 1.0 - 09/01/2020 - Oliten : Premiére diffusion_ 