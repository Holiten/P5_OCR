"""Main program with menus"""

import sys
from bdd import Bdd
from constants import CAT_1, CAT_2, CAT_3

BDD = Bdd()

print("Welcome to Pur Beurre")
BDD.bdd_exist()
BDD.load_data()
BDD.bdd_create()
BDD.bdd_use()
BDD.bdd_tables()
BDD.apidata_to_bdd()

def main_menu():
    """Main menu"""
    print("1 - Choose a product")
    print("2 - See favs products")
    print("Q - Quit")

    uc_main = input(" >> ")

    if uc_main == "1":
        cat_menu()

    elif uc_main == "2":
        BDD.get_saved()
        main_menu()

    elif uc_main == "Q" or "q":
        quit_pb()

    else: #fonctionne pas
        print("Choose a number or a letter corresponding to a choice")

def cat_menu(): # preferable : dictionnaire
    """Categories menu"""
    print("Y - Yaourts")
    print("F - Fromages")
    print("B - Boissons")
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_cat = input(" >> ")

    if uc_cat == "F" or "f":
        BDD.bdd_use()
        BDD.get_cat(CAT_2)
        BDD.get_product(CAT_2)
        BDD.substitute()
        if BDD.user_save == "Y":
            BDD.save_product()
            sauv_menu()
        elif BDD.user_save == "N":
            main_menu()

    elif uc_cat == "Y":
        BDD.bdd_use()
        BDD.get_cat(CAT_3)
        BDD.get_product(CAT_3)
        BDD.substitute()
        if BDD.user_save == "Y":
            BDD.save_product()
            sauv_menu()
        elif BDD.user_save == "N":
            main_menu()

    elif uc_cat == "B":
        BDD.bdd_use()
        BDD.get_cat(CAT_1)
        BDD.get_product(CAT_1)
        BDD.substitute()
        if BDD.user_save == "Y":
            BDD.save_product()
            sauv_menu()
        elif BDD.user_save == "N":
            main_menu()

    elif uc_cat == "9":
        main_menu()

    elif uc_cat == "Q":
        quit_pb()
    else:
        print("Choose a number or a letter corresponding to a choice")
        cat_menu()

def sauv_menu():
    """Save menu"""
    print("Product saved")
    print("9 - Back to main menu")
    print("0 - Quit")

    uc_sauv = input(" >> ")

    if uc_sauv == "9":
        main_menu()

    elif uc_sauv == "Q":
        quit_pb()

def back_or_quit():
    """Back or save menu"""
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_bq = input(" >> ")

    if uc_bq == "9":
        main_menu()

    elif uc_bq == "0":
        quit_pb()

def back():
    """Back menu"""
    main_menu()

def quit_pb():
    """Quit menu"""
    sys.exit("Thank you see :=)")

main_menu()
