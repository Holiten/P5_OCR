"""
Main program with menus
"""

from bdd import Bdd
from constants import CAT_1, CAT_2, CAT_3

bdd = Bdd()

print("Welcome to Pur Beurre")
bdd.api_temp()
bdd.create_db()
bdd.create_tables()
bdd.send_cat_to_db()
bdd.send_product_to_db()

def main_menu():
    """
    Main menu
    """
    print("1 - Choose a product")
    print("2 - See favs products")
    print("Q - Quit")

    uc_main = input(" >> ")

    if uc_main == "1":
        cat_menu()

    elif uc_main == "2":
        bdd.get_save_product()
        main_menu()

    elif uc_main == "Q" or "q":
        quit()

    else:
        main_menu()

def cat_menu():
    """
    Categories menu
    """
    print("Y - Yaourts")
    print("F - Fromages")
    print("B - Boissons")
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_cat = input(" >> ")

    if uc_cat == "F":
        bdd.get_cat(CAT_2)
        bdd.get_product(CAT_2)
        bdd.substitute()
        if bdd.user_save == "Y":
            sauv_menu()
        elif bdd.user_save == "N":
            main_menu()

    elif uc_cat == "Y":
        bdd.get_cat(CAT_3)
        bdd.get_product(CAT_3)
        bdd.substitute()
        if bdd.user_save == "Y":
            sauv_menu()
        elif bdd.user_save == "N":
            main_menu()

    elif uc_cat == "B":
        bdd.get_cat(CAT_1)
        bdd.get_product(CAT_1)
        bdd.substitute()
        if bdd.user_save == "Y":
            sauv_menu()
        elif bdd.user_save == "N":
            main_menu()

    elif uc_cat == "9":
        main_menu()

    elif uc_cat == "Q":
        quit()

def sauv_menu():
    """
    Save menu
    """
    print("S - Save product")
    print("9 - Back to main menu")
    print("0 - Quit")

    uc_sauv = input(" >> ")

    if uc_sauv == "S":
        bdd.save_product()
        print("Product saved")
        main_menu()

    elif uc_sauv == "9":
        main_menu()

    elif uc_sauv == "Q":
        quit()

def back_or_quit():
    """
    Back or save menu
    """
    print("9 - Back to main menu")
    print("Q - Quit")

    uc_bq = input(" >> ")

    if uc_bq == "9":
        main_menu()

    elif uc_bq == "0":
        quit()

def back():
    """
    Back menu
    """
    main_menu()

def quit():
    """
    Quit menu
    """
    print("Thank you ! See ya ;)")
    exit(1)

main_menu()


