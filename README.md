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
#### Launch :
* [Download](https://github.com/Holiten/P5_OCR) github repo
* Install packages (pip install -r requirements.txt)
* Launch (python main.py)
___
#### Features :

+ Search food in bdd with API [Open Food Fact](https://fr.openfoodfacts.org/)
    * Data recovery via Python script
    * Creation of database (if not exist) via a Python script
+ User interraction via terminal
+ Error handling (bad input)
+ Search via SQL
+ Save
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
* _Version 2.0 - 09/03/2020 - Oliten : New Github branch (For POO)_
* _Version 1.5 - 24/02/2020 - Oliten : Pre final version_
* _Version 1.4 - 10/02/2020 - Oliten : Code Optimisation & delete function inutiles_
* _Version 1.3 - 06/02/2020 - Oliten : PEP8 Optimisation_
* _Version 1.2.1 - 06/02/2020 - Oliten : Update after mentor meeting_ 
* _Version 1.2 - 13/01/2020 - Oliten : Update after mentor meeting_  
* _Version 1.0 - 09/01/2020 - Oliten : First version_ 