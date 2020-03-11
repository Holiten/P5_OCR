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
    run = 1
    while run == 1:
        print("1 - Choose a product")
        print("2 - See favs products")
        print("Q - Quit")

        uc_main = input(" >> ")

        if uc_main == "1":
            cat_menu()
            run = 0

        elif uc_main == "2":
            BDD.get_saved()
            main_menu()
            run = 0

        elif uc_main == "Q" or uc_main == "q":
            quit_pb()
            run = 0

        else:
            print("Choose a number or a letter corresponding to a choice")
            run = 1

def cat_menu():
    """Categories menu"""
    run = 1
    print("Y - Yaourts")
    print("F - Fromages")
    print("S - Soupes")
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_cat = input(" >> ")

    while run == 1:
        if uc_cat == "F" or uc_cat == "f":
            BDD.bdd_use()
            BDD.get_cat(CAT_2)
            BDD.get_product(CAT_2)
            BDD.substitute()
            if BDD.user_save == "Y" or BDD.user_save == "y":
                BDD.save_product()
                sauv_menu()
                run = 0
            elif BDD.user_save == "N" or BDD.user_save == "n":
                main_menu()
                run = 0
            else:
                print("Choose a number or a letter corresponding to a choice")
                run = 1

        elif uc_cat == "Y" or uc_cat == "y":
            BDD.bdd_use()
            BDD.get_cat(CAT_3)
            BDD.get_product(CAT_3)
            BDD.substitute()
            if BDD.user_save == "Y" or BDD.user_save == "y":
                BDD.save_product()
                sauv_menu()
                run = 0
            elif BDD.user_save == "N" or BDD.user_save == "n":
                main_menu()
                run = 0
            else:
                print("Please choose a valid choice")
                run = 1

        elif uc_cat == "S" or uc_cat == "s":
            BDD.bdd_use()
            BDD.get_cat(CAT_1)
            BDD.get_product(CAT_1)
            BDD.substitute()
            if BDD.user_save == "Y" or BDD.user_save == "y":
                BDD.save_product()
                sauv_menu()
                run = 0
            elif BDD.user_save == "N" or BDD.user_save == "n":
                main_menu()
                run = 0
            else:
                print("Please choose a valid choice")
                run = 1

        elif uc_cat == "9":
            main_menu()

        elif uc_cat == "Q" or uc_cat == "q":
            quit_pb()
            run = 0
        else:
            print("Choose a number or a letter corresponding to a choice")
            run = 1

def sauv_menu():
    """Save menu"""
    run = 1
    print("Product saved")
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_sauv = input(" >> ")

    while run == 1:
        if uc_sauv == "9":
            main_menu()
            run = 0

        elif uc_sauv == "Q" or uc_sauv == "q":
            quit_pb()
            run = 0

        else:
            print("Please choose a valid choice")
            run = 1

def back_or_quit():
    """Back or save menu"""
    run = 1
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_bq = input(" >> ")
    while run == 1:
        if uc_bq == "9":
            main_menu()
            run = 0

        elif uc_bq == "Q" or uc_bq == "q":
            quit_pb()
            run = 0

        else:
            print("Please choose a valid choice")
            run = 1

def back():
    """Back menu"""
    main_menu()

def quit_pb():
    """Quit menu"""
    sys.exit("Thank you see :=)")

main_menu()
