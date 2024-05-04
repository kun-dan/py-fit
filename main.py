import mysql.connector as mycon
import random
import csv
import time
from datetime import date, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
from os import get_terminal_size




con = mycon.connect(
    host="localhost",
    user="root",
    passwd="0000"
)

if con.is_connected():
    print("[LOGS] : Database Connected")
    

cur = con.cursor()

def signup():
    global username                                                     # This will be the global username
    global doj                                                          # This will be the join date
    while True:
        print("╔═════════════════════════════════════════════╗")
        print("║         Enter your desired username:        ║")
        print("╚═════════════════════════════════════════════╝")
        username = input("INPUT:")
        with open("data.csv", "r") as file:
            read = csv.reader(file)
            user_row = list(read)
            items = [row[0] for row in user_row]

        if username in items:
            time.sleep(0.18)
            print("╔═════════════════════════════════════════════╗")
            print("║           Username already exists.          ║")
            print("╚═════════════════════════════════════════════╝")
            continue
        
        if len(username) > 20:
            time.sleep(0.18)
            print("╔═════════════════════════════════════════════╗")
            print("║         Username should be of max.          ║")
            print("║               20 characters                 ║")
            print("╚═════════════════════════════════════════════╝")
            continue
        
        break
    

    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║        Enter a valid password:        ║")
        print("╚═══════════════════════════════════════╝")





            # Code in Progress
            
            
        
        

    

def welcome():
    while True:
        print("╔════════════════════════════════════════════╗")
        print(r"║     ______  __            ________________ ║")
        print(r"║    / __ \ \/ /           / ____/  _/_  __/ ║")
        print(r"║   / /_/ /\  /  ______   / /_   / /  / /    ║")
        print(r"║  / ____/ / /  /_____/  / __/ _/ /  / /     ║")
        print(r"║ /_/     /_/           /_/   /___/ /_/      ║")
        print(r"║                                            ║")
        print(r"╚════════════════════════════════════════════╝")
        time.sleep(0.2)
        print("╔═════════════════════════════════════════════╗")
        print("║  Welcome! What Would You Like to do Today   ║")
        print("╚═════════════════════════════════════════════╝")
        time.sleep(0.2)
        print("╔═════════════════════════════════════════════╗")
        print("║            1. Create an Account             ║")
        print("║       2. Log In to an Existing Account      ║")
        print("║              3. Exit the App                ║")
        print("╚═════════════════════════════════════════════╝")


        choice = input("Enter Your Choice: ")
        if choice == "1":

            return
        elif choice == "2":
            return
        elif choice == "3":
            print("╔════════════════════════════════════════════╗")
            print(r"║     ______  __            ________________ ║")
            print(r"║    / __ \ \/ /           / ____/  _/_  __/ ║")
            print(r"║   / /_/ /\  /  ______   / /_   / /  / /    ║")
            print(r"║  / ____/ / /  /_____/  / __/ _/ /  / /     ║")
            print(r"║ /_/     /_/           /_/   /___/ /_/      ║")
            print(r"║                                            ║")
            print(r"╚════════════════════════════════════════════╝")
            time.sleep(0.2)
            print("╔═════════════════════════════════════════════╗")
            print("║        Thank You For Using PY - FIT         ║")
            print("╚═════════════════════════════════════════════╝")
            quit()
        else:
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid input. Please choose a number ║")
            print("║             from 1 to 3.              ║")
            print("╚═══════════════════════════════════════╝")




welcome()

