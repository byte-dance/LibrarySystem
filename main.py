# -*- coding = uft-8 -*-
# @File: main.py.py
# @Software: PyCharm
from transaction import *


def MainMenu():
    print("-----------MAIN MENU-----------")
    while True:
        print("1.Reader")
        print("2.Administrative")
        print("3.Quit")
        identity = input("Please enter 1 or 2:")
        if identity == "1":
            card_number = input("Your card number:")
            # todo 检验卡号是否存在
            ReaderFunctionsMenu(card_number)
        elif identity == "2":
            id = input("Your ID:")
            password = input("Your password:")
            # todo 检验账号密码是否正确
            AdministrativeFunctionsMenu(id, password)
        elif identity == "3":
            break
        else:
            print("error input")


def ReaderFunctionsMenu(card_number):
    print("-----------Dear Reader-" + card_number + ", welcome-----------")
    while True:
        print("1.Search a document by ID, title, or publisher name")
        print("2.Document checkout")
        print("3.Document return")
        print("4.Document reserve")
        print("5.Compute fine for a document copy borrowed by a reader based on the current date")
        print("6.Print the list of documents reserved by a reader and their status")
        print("7.Print the document id and document titles of documents published by a publisher")
        print("8.Quit")
        mode = input("Please enter a single number between 1 and 8:")
        if mode == "1":
            # todo
            continue
        elif mode == "2":
            # todo
            continue
        elif mode == "3":
            # todo
            title = input("please enter the title of the document you want to return")
            document_return(title, card_number)
            continue
        elif mode == "4":
            # todo
            title = input("please enter the title of the document you want to reserve")
            document_reserve(title,card_number)
            continue
        elif mode == "5":
            # todo
            continue
        elif mode == "6":
            # todo
            continue
        elif mode == "7":
            # todo
            continue
        elif mode == "8":
            print("Sign out successfully.")
            continue
        else:
            print("error input")


def AdministrativeFunctionsMenu(id, password):
    print("-----------Dear Administrator, welcome-----------")
    while True:
        print("1.Add a document copy")
        print("2.Search document copy and check its status")
        print("3.Add new reader")
        print("4.Print branch information (name and location)")
        print("5.Print top 10 most frequent borrowers in a branch and the number of books each has borrowed")
        print("6.Print top 10 most borrowed books in a branch")
        print("7.Print the 10 most popular books of the year")
        print("8.Find the average fine paid per reader")
        print("9.Quit")
        mode = input("Please enter a single number between 1 and 8:")
        if mode == "1":
            # todo
            continue
        elif mode == "2":
            # todo
            continue
        elif mode == "3":
            # todo
            continue
        elif mode == "4":
            # todo
            continue
        elif mode == "5":
            # todo
            continue
        elif mode == "6":
            # todo
            continue
        elif mode == "7":
            # todo
            continue
        elif mode == "8":
            # todo
            continue
        elif mode == "9":
            print("Sign out successfully.")
            continue
        else:
            print("error input")


if __name__ == '__main__':
    MainMenu()


